#!/usr/bin/env python
"""
__license__ = "SPDX-License-Identifier: MIT"
__copyright__ = "Copyright (C) 2021 VMware, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in the
Software without restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

===

Handles CVE-2021-44228 exploit for VMware vCenter Server for both Virtual
Appliance and Microsoft Windows environments. This script automates the guidance
found under https://kb.vmware.com/s/article/87081 and
https://kb.vmware.com/s/article/87096

This script can run in its default remediation mode or in dry run scan mode.
Remediation mode applies fixes to the vCenter configuration and library code.
Dry run scan mode is used to identify vulnerable files and validate the fixes
from a remediation run.

The steps in the remediation mode are:
1. Stop all services to unlock all configuration and library files that may
   need remediation. This step uses "service-control --stop --all" command.
2. Scan Java library files (*.jar and *.war) for "JndiLookup.class" and remove it.
3. Based on the vCenter system version, deployment flavour and OS type scans the
   configuration files for "-Dlog4j2.formatMsgNoLookups=true" configuration
   option and adds it as needed.
4. Start all services using "service-control --start --all"

In the remediation mode any modified files are backed up. The backup location
needs to be set with "-b" option or will default to a temporary folder that must
be backed up immediately after running the script.

In dry run scan mode the script will only examine the files from steps 2 and 3
above and report any potentially vulnerable files. No service stop and start is
needed in dry run mode. The dry run mode is activated with "-r".

The script produces detailed log file under the VMWARE_LOG_DIR folder.
"""

import os
import sys
import shutil
from distutils.file_util import copy_file
import zipfile
import codecs
import tempfile
import subprocess
import logging
import argparse
import hashlib
import json
from datetime import datetime
from itertools import chain
import re

LOG = logging.getLogger(__name__)

# exit code constants
COMPLETED_OK = 0
ERROR_USER_INPUT = 1
ERROR_STOPING_SERVICES = 2
ERROR_STARTING_SERVICES = 3
ERROR_PATH_NOT_A_DIRECTORY = 4
ERROR_UNHANDLED_EXCEPTION = 5
ERROR_VCHA_ENABLED = 6
ERROR_MISSING_IMPORT = 7

sys.path.append(os.environ['VMWARE_PYTHON_PATH'])
try:
    from cis.tools import get_install_parameter
    from cis.exceptions import InstallParameterException
except ImportError:
    class InstallParameterException(Exception):
        """Imitates missing InstallParameterException class"""

if sys.platform in ['win32', 'cygwin', 'windows']:
    try:
        from six.moves import winreg
    except ImportError:
        import _winreg as winreg

    try:
        import win32security
        import win32api
    except ImportError:
        LOG.error("Unable to import win32security and/or win32api")
        sys.exit(ERROR_MISSING_IMPORT)

SCRIPT_VERSION = "1.6.0"
JNDI_PATH = "org/apache/logging/log4j/core/lookup/JndiLookup.class"
BACKUP_DIR = ""  # This is initialized below
LOG_DIR = os.environ.get('VMWARE_LOG_DIR')
LOG_NAME = "vmsa-2021-0028"
HASHING_CHUNK_SIZE = 1024 * 1024
SAFE_SHA256_HASHES = [
    '085e0b34e40533015ba6a73e85933472702654e471c32f276e76cffcf7b13869', # log4j-core-2.16.0.jar from apache.org
    '5d241620b10e3f1475320bc9552cf7bcfa27eeb9b1b6a891449e76db4b4a02a8'  # log4j-core-2.16.0.jar from mvnrepository/build-artifactory
]

# Deployment types
DEPLOY_TYPE_PSC = "infrastructure"
DEPLOY_TYPE_EMBEDDED = "embedded"
DEPLOY_TYPE_MANAGEMENT = "management"

class Environment:
    """
    Collect VMware environment specific information
    """
    def __init__(self):
        """
        Computes the vCenter version. Use on vCenter 6.5 and later only
        """
        self.__gateway = False

        LOG.debug("Determining vCenter version and type")

        self.__is_windows = sys.platform in ['win32', 'cygwin', 'windows']

        if self.__is_windows:
            reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
            key = winreg.OpenKey(reg, r"SOFTWARE\VMware, Inc.\vCenter Server")
            self.__build = winreg.QueryValueEx(key, 'BuildNumber')[0]
            self.__version = winreg.QueryValueEx(key, 'ProductVersion')[0]
        else:
            with open("/etc/applmgmt/appliance/update.conf", 'r') as file_descriptor:
                data = json.load(file_descriptor)
            self.__build = data['build']
            with open("/etc/issue", 'r') as file_descriptor:
                for line in file_descriptor:
                    if not line.strip():
                        continue
                    version = line
                    if "Gateway" in line:
                        self.__gateway = True
                    break
            version = version.rsplit(' ', 1)[1]
            self.__version = version.strip()
        try:
            LOG.debug("Getting deploy type")
            self.__deploytype = get_install_parameter('deployment.node.type', quiet=True)
        except (InstallParameterException, NameError):
            try:
                file = os.path.join(os.environ['VMWARE_CFG_DIR'], 'deployment.node.type')
                with open(file, 'r') as file_descriptor:
                    self.__deploytype = file_descriptor.read()
            except Exception as e:
                LOG.error("Unhandled exception occurred while trying "
                          "to get system deployment type from configuration file: %s", e)
        except Exception as e:
            LOG.error("Unhandled exception occurred while trying "
                      "to get system deployment type using python script: %s", e)

        self.__has_vcha = os.path.isfile("/etc/vmware-vcha/vcha.cfg")

        LOG.debug("Computed version: %s", str(self))

    def __str__(self):
        return ("Version: %s; Build: %s; Deployment type: %s; "
                "Gateway: %s; VCHA: %s; Windows: %s;" \
                    % (self.__version, self.__build, self.__deploytype,
                       self.__gateway, self.__has_vcha, self.__is_windows))


    def is_7(self):
        """Checks if current environment is version 7.x"""
        return self.__version.startswith("7.")

    def is_6(self):
        """Checks if current environment is version 6.x"""
        return self.__version.startswith("6.")

    def is_65(self):
        """Checks if current environment is version 6.5.x"""
        return self.__version.startswith("6.5.")

    def is_gateway(self):
        """Checks if current environment is gateway"""
        return self.__gateway

    def has_identity_svcs(self):
        """Checks if current environment has identity services"""
        return self.__deploytype in [DEPLOY_TYPE_EMBEDDED, DEPLOY_TYPE_PSC]

    def has_mgmt_svcs(self):
        """Checks if current environment has appliance management services"""
        return self.__deploytype in [DEPLOY_TYPE_EMBEDDED, DEPLOY_TYPE_MANAGEMENT]

    def has_vcha(self):
        """Checks if current environment has HA enabled"""
        return self.__has_vcha

    def is_windows(self):
        """Checks if current environment is windows OS"""
        return self.__is_windows

ENV = Environment()


class Services(object):
    """Helper class for start/stop all services using service-control"""

    def __init__(self):
        if ENV.is_windows():
            self.service_control = \
                os.path.join(os.environ['VMWARE_CIS_HOME'], 'bin', 'service-control.bat')
        else:
            self.service_control = "/usr/bin/service-control"

    @classmethod
    def run_command(cls, cmd):
        """
        execute a command with the given input and return the return code and output
        """
        LOG.debug("Running command: %s", str(cmd))

        # Note: close_fds is always set to False for windows. This is because
        # stdin/stdout flags don't work with close_fds on Windows.

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   close_fds=False)
        stdout, stderr = process.communicate()
        ret = process.returncode
        LOG.debug("Done running command")
        if isinstance(stdout, str):
            stdout = stdout.decode(sys.getfilesystemencoding())
        if isinstance(stderr, str):
            stderr = stderr.decode(sys.getfilesystemencoding())
        if ret != 0:
            LOG.error("RC = %s\nStdout = %s\nStderr = %s", ret, stdout, stderr)
        return ret, stdout, stderr

    def stop(self):
        """
        Runs external script which stops system services
        """
        LOG.info("stopping services")

        cmd = [self.service_control, '--stop', '--all']
        ret, stdout, _ = Services.run_command(cmd)

        if ret != 0:
            LOG.error("error occurred while trying to stop vmware services")
            sys.exit(ERROR_STOPING_SERVICES)

        LOG.debug(stdout)

    def start(self):
        """
        Runs external script which start system services
        """
        LOG.info("starting services")
        cmd = [self.service_control, '--start', '--all']
        ret, stdout, _ = Services.run_command(cmd)

        if ret != 0:
            LOG.error("error occurred while trying to start services")
            sys.exit(ERROR_STARTING_SERVICES)

        LOG.debug(stdout)


class Log4jCommandFlagPatcher(object):
    """
    Contains common functionality for patching log4j flag option in both
    linux and windows
    """
    def __init__(self, dryrun):
        self.dryrun = dryrun
        self.cfgdir = os.path.join(os.environ['VMWARE_CFG_DIR'], 'vmware-vmon', 'svcCfgfiles')
        self.runtime_dir = os.environ['VMWARE_RUNTIME_DATA_DIR']
        self.home = os.environ['VMWARE_CIS_HOME']
        self.results = []
        self.issues = []

    @classmethod
    def _workaround_exists(cls, filename):
        return Log4jCommandFlagPatcher._file_contains(filename, "formatMsgNoLookups")

    @classmethod
    def _file_contains(cls, filename, str_val):
        LOG.debug("Checking %s for '%s'", filename, str_val)
        with open(filename, 'r') as file_descriptor:
            data = file_descriptor.read()
        if str_val in data:
            LOG.debug("Found.")
            return True

        LOG.debug("Not found.")
        return False

    def _add_to_results(self, filename):
        if filename not in self.results:
            self.results.append(filename)

    def _patch_file(self, filename, replace_func):
        if Log4jCommandFlagPatcher._workaround_exists(filename):
            return

        LOG.info("Found VULNERABLE FILE: %s", filename)
        self._add_to_results(filename)

        if self.dryrun:
            return

        LOG.debug("Patching file: %s", filename)
        backup_file(filename)

        Log4jCommandFlagPatcher._replace_file_content(
            filename,
            replace_func)

    @classmethod
    def _replace_file_content(cls, filename, replace_func):
        stat = os.stat(filename)
        try:
            with open(filename, 'r', encoding='utf-8') as in_file:
                content = in_file.read()
        except Exception:
            with codecs.open(filename, 'r', encoding='utf-8') as in_file:
                content = in_file.read()

        content = replace_func(content)

        try:
            with open(filename, 'w', encoding='utf-8') as out_file:
                out_file.write(content)
        except Exception:
            with codecs.open(filename, 'w', encoding='utf-8') as out_file:
                out_file.write(content)
        set_file_perms(filename, stat)

    def patch(self):
        """Main function to run configuration file patching mechanism"""
        LOG.error("Unimplemented Base method")

class Log4jCommandFlagWindowsPatcher(Log4jCommandFlagPatcher):
    """
    patches vCenter windows specific content
    """

    def _patch_wrapper(self, filename):
        def patch_replace_func(content):
            max_line = 0
            lines = content.splitlines()
            for line in lines:
                if "wrapper.java.additional" not in line:
                    continue

                line = line.split("=", 1)[0]
                try:
                    val = int(line.rsplit(".", 1)[1])
                    if val > max_line:
                        max_line = val
                except ValueError:
                    continue

            if max_line == 0:
                msg = ("Cannot find wrapper.java.additional in the "
                       "cofiguration file: %s. Skipping modifing configuration." % filename)
                self.issues.append(msg)
                LOG.error(msg)
                return content

            latest_param = "wrapper.java.additional.%s=" % max_line
            new_param = \
                "\nwrapper.java.additional.%s=\"-Dlog4j2.formatMsgNoLookups=true\"\n" \
                    % (max_line + 1)


            new_lines = []
            for line in lines:
                if latest_param in line.replace(" ",""):
                    line = line + new_param
                new_lines.append(line)

            return "\n".join(new_lines)

        self._patch_file(filename, patch_replace_func)

    @classmethod
    def _contains_startargs(cls, filename):
        with open(filename) as file_descriptor:
            if re.search(r'StartCommand.*\/java', file_descriptor.read()):
                LOG.debug("Java vMON file: %s", filename)
                return True
        LOG.debug("Not a Java vMON file: %s", filename)
        return False

    def patch_vmon_confs(self):
        """patches vMON configuration"""
        LOG.debug("Executing vMON service configurations check")

        if not os.path.exists(self.cfgdir):
            msg = ("vMON configuration not found: %s."
                   " Cannot perform automated remediation on this file. " % self.cfgdir)
            self.issues.append(msg)
            LOG.error("%s Please follow the manual steps described in "
                      "https://kb.vmware.com/s/article/87096", msg)
            return

        for cfgfile in [f for f in os.listdir(self.cfgdir) if f.endswith('.json')]:
            filename = os.path.join(self.cfgdir, cfgfile)
            if Log4jCommandFlagPatcher._workaround_exists(filename) \
                    or not Log4jCommandFlagWindowsPatcher._contains_startargs(filename):
                continue

            LOG.info("Found VULNERABLE FILE: %s", filename)
            self._add_to_results(filename)

            if self.dryrun:
                continue

            backup_file(filename)

            def add_log4j_flag(text):
                content = json.loads("\n".join(line for line in text.splitlines() \
                                if not line.lstrip().startswith("//")))

                command = content.get('StartCommand')
                if command and (command.endswith('bin/java') or command.endswith('bin/java.exe')):
                    content['StartCommandArgs'].insert(
                        0,
                        '-Dlog4j2.formatMsgNoLookups=true')

                return json.dumps(content, sort_keys=True, indent=4)

            Log4jCommandFlagPatcher._replace_file_content(filename, add_log4j_flag)

    def patch_psc_client(self):
        """patches PSX Client configuration"""
        LOG.debug("Executing PSC Client configuration check")
        filename = os.path.join(self.runtime_dir, 'vmware-psc-client', 'conf', 'wrapper.conf')

        if not os.path.exists(filename):
            msg = ("Cannot locate the PSC Client configuration at: %s."
                   ". Cannot perform automated remediation on this file. ", filename)
            self.issues.append(msg)
            LOG.error("%s Please follow the manual steps described in "
                      "https://kb.vmware.com/s/article/87096", msg)
            return

        self._patch_wrapper(filename)

    def patch_sts(self):
        """patches Secure Token Services configuration"""
        LOG.debug("Executing Secure Token Services (STS) configuration check")
        filename = os.path.join(self.runtime_dir, 'VMwareSTSService', 'conf', 'wrapper.conf')

        if not os.path.exists(filename):
            filename = os.path.join(self.home,'VMware Identity Services', 'wrapper', 'conf', 'wrapper.conf')
            if not os.path.exists(filename):
                msg = ("Cannot locate the STS configuration at : %s."
                       "Cannot perform automated remediation." % filename)
                self.issues.append(msg)
                LOG.error("%s Please follow the manual steps described in "
                          "https://kb.vmware.com/s/article/87096", msg)
                return
        
        self._patch_wrapper(filename)

    def patch_perfcharts(self):
        """patches perjcharts configuration"""
        LOG.debug("Executing perfcharts check")
        filename = os.path.join(self.home, 'perfcharts', 'wrapper', 'conf', 'wrapper.conf')

        if not os.path.exists(filename):
            msg = ("Cannot locate the perfcharts configuration at: %s."
                   " Cannot perform automated remediation." % filename)
            self.issues.append(msg)
            LOG.error("%s Please follow the manual steps described in "
                      "https://kb.vmware.com/s/article/87096", msg)
            return

        self._patch_wrapper(filename)

    def patch_idmd(self):
        """patches Identity Management Service configuration"""
        LOG.debug("Executing Identity Management Service check")
        regkey = r'HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation' \
                 + r'\Procrun 2.0\VMwareIdentityMgmtService\Parameters\Java'
        try:
            with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as reg:
                with winreg.OpenKey(
                        reg,
                        r"SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0" \
                            + r"\VMwareIdentityMgmtService\Parameters\Java",
                        0,
                        winreg.KEY_ALL_ACCESS) as key:

                    win32security.AdjustTokenPrivileges(
                        win32security.OpenProcessToken(
                            win32api.GetCurrentProcess(),
                            40),
                        0,
                        [(win32security.LookupPrivilegeValue(None, 'SeBackupPrivilege'), 2)])
                    options = winreg.QueryValueEx(key, 'Options')[0]

                    if "-Dlog4j2.formatMsgNoLookups=true" in options:
                        # already handled
                        return

                    LOG.info("Found a VULNERABLE component:  RegKey %s", regkey)
                    self._add_to_results(r'RegKey: HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node'
                                         r'\Apache Software Foundation\Procrun 2.0'
                                         r'\VMwareIdentityMgmtService\Parameters\Java')

                    if self.dryrun:
                        return

                    regkeybackuppath = os.path.join(BACKUP_DIR, "IDMD_REG_BACKUP")
                    winreg.SaveKey(key, regkeybackuppath)
                    options.append("-Dlog4j2.formatMsgNoLookups=true")
                    winreg.SetValueEx(key, "Options", 0, winreg.REG_MULTI_SZ, options)
                    LOG.info("VULNERABLE REGKEY: %s backed up to %s", regkey, regkeybackuppath)
        except Exception as e:
            msg = ("Cannot perform automated remediation of Identity "
                   "Management Service configuration. Unhandled exception occurred: %s" % e)
            self.issues.append(msg)
            LOG.error("%s Please follow the manual steps described in "
                      "https://kb.vmware.com/s/article/87096", msg)


    def patch(self):
        """patches all windows vulnerable configurations"""
        self.patch_vmon_confs()
        if ENV.has_identity_svcs():
            self.patch_sts()
            self.patch_idmd()
            if ENV.is_65():
                self.patch_psc_client()
        return self.results, self.issues


class Log4jCommandFlagVCSAPatcher(Log4jCommandFlagPatcher):
    """
    Patches vCenter Virtual Appliance specific configuration
    """

    def patch_vmon(self):
        """patches vMON service configuration"""
        LOG.debug("Executing vMON service configurations check")
        filename = "/usr/lib/vmware-vmon/java-wrapper-vmon"

        if not os.path.exists(filename):
            msg = ("Cannot locate the vMON configuration at: %s."
                   " Cannot perform automated remediation on this file." % filename)
            self.issues.append(msg)
            LOG.error("%s Please follow the manual steps described in "
                      "https://kb.vmware.com/s/article/87081", msg)
            return

        if Log4jCommandFlagPatcher._workaround_exists(filename):
            return

        checkstring1 = 'exec $java_start_bin $jvm_dynargs "$@"'
        new_config_entries1 = 'log4j_arg="-Dlog4j2.formatMsgNoLookups=true"' \
            + "\n" \
            + 'exec $java_start_bin $jvm_dynargs $log4j_arg "$@"'

        checkstring2 = 'exec $java_start_bin $jvm_dynargs $security_dynargs $original_args'
        new_config_entries2 = 'log4j_arg="-Dlog4j2.formatMsgNoLookups=true"' \
            + "\n" \
            + 'exec $java_start_bin $jvm_dynargs $log4j_arg $security_dynargs $original_args'

        if Log4jCommandFlagPatcher._file_contains(filename, checkstring1):
            self._patch_file(
                filename,
                lambda content: content.replace(checkstring1, new_config_entries1))

        elif Log4jCommandFlagPatcher._file_contains(filename, checkstring2):
            self._patch_file(
                filename,
                lambda content: content.replace(checkstring2, new_config_entries2))
        else:
            msg = ("vMON script exists and vulnerability marker were " + \
                   "not found on file: %s. Please, verify this is expected." % filename)
            self.issues.append(msg)
            LOG.error("%s Please follow the manual steps described in "
                      "https://kb.vmware.com/s/article/87081", msg)


    def patch_psc_client(self):
        """patches PSC client configuration"""
        LOG.debug("Executing PSC Client configuration check")
        filename = "/etc/rc.d/init.d/vmware-psc-client"

        if not os.path.exists(filename):
            msg = ("Cannot locate the PSC Client configuration at: %s."
                   " Cannot perform automated remediation on this file." % filename)
            self.issues.append(msg)
            LOG.error("%s Please follow the manual steps described in "
                      "https://kb.vmware.com/s/article/87081", msg)
            return

        new_config_entries = '-Dlog4j2.formatMsgNoLookups=true \\\n' \
            + '             $DAEMON_CLASS start'
        self._patch_file(
            filename,
            lambda content: content.replace('$DAEMON_CLASS start', new_config_entries))

    def patch_sts(self):
        """patches Secure Token Service configuration"""
        LOG.debug("Executing Secure Token Service (STS) check")
        filename = "/etc/rc.d/init.d/vmware-stsd"

        if not os.path.exists(filename):
            msg = ("Cannot locate the STS configuration at: %s."
                   " Cannot perform automated remediation on this file." % filename)
            self.issues.append(msg)
            LOG.error("%s Please follow the manual steps described in "
                      "https://kb.vmware.com/s/article/87081", msg)
            return

        new_config_entries = '-Dlog4j2.formatMsgNoLookups=true \\\n' \
            + '            $DAEMON_CLASS start'
        self._patch_file(
            filename,
            lambda content: content.replace('$DAEMON_CLASS start', new_config_entries))

    def patch_idmd(self):
        """patches Identity Management Service configuration"""
        LOG.debug("Executing Identity Management Service configuration check")
        filename = "/etc/rc.d/init.d/vmware-sts-idmd"

        if not os.path.exists(filename):
            msg = ("Cannot locate the Identity Management Service configuration at: %s."
                   " Cannot perform automated remediation on this file." % filename)
            self.issues.append(msg)
            LOG.error("%s Please follow the manual steps described in "
                      "https://kb.vmware.com/s/article/87081", msg)
            return

        new_config_entries = '-Dlog4j2.formatMsgNoLookups=true \\\n' \
            + '                  $DEBUG_OPTS'
        self._patch_file(
            filename,
            lambda content: content.replace("$DEBUG_OPTS", new_config_entries))

    def patch_vum(self):
        """patches Update Manager service configuration"""
        LOG.debug("Executing Update Manager Service configuration check")
        filename = "/usr/lib/vmware-updatemgr/bin/jetty/start.ini"

        if not os.path.exists(filename):
            msg = ("Cannot locate the Update Manager Service configuration at: %s."
                   " Cannot perform automated remediation on this file." % filename)
            self.issues.append(msg)
            LOG.error("%s Please follow the manual steps described in "
                      "https://kb.vmware.com/s/article/87081")
            return

        if Log4jCommandFlagPatcher._workaround_exists(filename):
            return

        LOG.info("Found a VULNERABLE FILE: %s", filename)
        self._add_to_results(filename)

        if self.dryrun:
            return

        LOG.debug("Patching VUM file: %s", filename)
        backup_file(filename)

        with open(filename, 'a') as file_descriptor:
            file_descriptor.write("-Dlog4j2.formatMsgNoLookups=true")

    def patch(self):
        """patches all VC appliance vulnerable configurations"""
        self.patch_vmon()
        if ENV.has_identity_svcs():
            if ENV.is_65():
                self.patch_psc_client()
            if ENV.is_6():
                self.patch_sts()
                self.patch_idmd()
        if ENV.has_mgmt_svcs() and ENV.is_7() and not ENV.is_gateway():
            self.patch_vum()
        return self.results, self.issues


def prompt_service_restart(accept_services_restart, start=False):
    """
    Prompts user that a service stop and start operations would be required
    """
    service_action = Services()
    if not start:
        user_choice = 'y'
        if not accept_services_restart:
            try:
                user_choice = \
                    raw_input("A service stop and start is required to "
                              "complete this operation.  Continue?[y]")
            except NameError:
                user_choice = \
                    input("A service stop and start is required to "
                          "complete this operation.  Continue?[y]")
            LOG.debug("User chose '%s'", user_choice)
        else:
            LOG.debug("Skipping user choice and assuming stop and start of services")

        if user_choice.lower() == 'y':
            service_action.stop()
        else:
            LOG.info("Cannot continue without stopping services. Exiting...")
            sys.exit(ERROR_USER_INPUT)
    else:
        service_action.start()

def patch_configuration(dryrun):
    """
    Apply configuration file patching functionality
    """
    if ENV.is_windows():
        return Log4jCommandFlagWindowsPatcher(dryrun).patch()
    return Log4jCommandFlagVCSAPatcher(dryrun).patch()


def setup_logging(log_dir):
    """
    Sets logging to write to vmware log system directory, current working directory, and console
    """

    def set_handler(handler, loglevel):
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(funcName)s: %(message)s",
            datefmt='%Y-%m-%dT%H:%M:%S')
        handler.setFormatter(formatter)
        handler.setLevel(loglevel)
        LOG.addHandler(handler)

    LOG.setLevel(logging.DEBUG)

    file_name = LOG_NAME + "_" + datetime.utcnow().strftime("%Y_%m_%d_%H_%M_%S") + '.log'
    if log_dir:
        # User specified log directory
        file_path = os.path.join(log_dir, file_name)
    elif LOG_DIR:
        # LOG for support bundles
        file_path = os.path.join(LOG_DIR, file_name)
    else:
        # LOG in current working directory
        file_path = os.path.join(os.getcwd(), file_name)
    file_handler = logging.FileHandler(file_path)
    set_handler(file_handler, logging.DEBUG)

    # console handler
    console_handler = logging.StreamHandler(sys.stdout)
    set_handler(console_handler, logging.INFO)


def is_java_archive(filename):
    """
    Return true if the given filename ends with either .jar or .war
    :type filename: str
    :rtype: bool
    """
    return filename.lower().endswith((".jar", ".war"))


def find_zip_files(dirnames, parent_type=None, dryrun=False):
    """
    Find and process all files under given dirnames to find the offending log4j
    class.
    :type dirnames: list[str]
    :param parent_type: whether the parent of these dirnames come from a .war file.
        The value is only "war" or None.
    :type parent_type: str
    :param dryrun: A boolean to indicate whether the archive should be mitigated.
        False means to mitigate it.
    :type dryrun: bool
    :return: List of filepaths that have been processed
    :rtype: list[str]
    """
    if not isinstance(dirnames, list):
        dirnames = [dirnames]
    processed_files = []
    for root, _, files in chain.from_iterable(os.walk(path) for path in dirnames):
        for file_name in files:
            if is_java_archive(file_name):
                if not os.path.getsize(os.path.join(root, file_name)) == 0:
                    processed = process_archive(file_name, root, parent_type, dryrun)
                    if processed is not None:
                        processed_files.append(processed)
                else:
                    LOG.debug("File: %s is 0 bytes in size.  Skipping...", file_name)
                    continue
    return processed_files


def has_vulnerable_class(filename):
    """
    Returns true if given filepath contains the offending log4j class.
    :param filename: name of a zip file to process
    :type filename: str
    :rtype: bool
    """
    with zipfile.ZipFile(filename, 'r') as zip_obj:
        # Get list of files names in zip
        list_of_files = zip_obj.namelist()
        return any(f.endswith(JNDI_PATH) for f in list_of_files)


def is_safe_version(filename):
    """
    Returns true if given filepath matches a hash of the known good versions.
    :param filename: name of a zip file to check
    :type filename: str
    :rtype: bool
    """
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as file_descriptor:
        while True:
            chunk = file_descriptor.read(HASHING_CHUNK_SIZE)
            if not chunk:
                break
            sha256.update(chunk)

    LOG.debug("%s, %s", filename, sha256.hexdigest())
    return sha256.hexdigest() in SAFE_SHA256_HASHES


def backup_file(filepath):
    """
    Move given filepath to under BACKUP_DIR with preserving the file hierarchy.
    :type filepath: str
    :return: The backed up filepath under BACKUP_DIR
    :rtype: str
    """
    normpath = os.path.normpath(filepath)
    normpath = os.sep.join(normpath.split(os.sep)[1:])
    backuppath = os.path.join(BACKUP_DIR, normpath + ".bak")
    # move file to .bak and remove original
    try:
        if not os.path.exists(os.path.dirname(backuppath)):
            os.makedirs(os.path.dirname(backuppath))
        copy_file(filepath, backuppath)
        set_file_perms(backuppath, os.stat(filepath))
        LOG.info("VULNERABLE FILE: %s backed up to %s", filepath, backuppath)
    except OSError:
        LOG.error("Failed to create backup of %s. Check if backup already exists.", filepath)
        return None
    return backuppath


def set_file_perms(filepath, stat):
    """
    Setting the given stat to the filepath.
    :type filepath: str
    :type stat: os.stat_result
    """
    os.chmod(filepath, stat.st_mode)
    if not ENV.is_windows():
        os.chown(filepath, stat.st_uid, stat.st_gid)


def create_archive(pathname, directory):
    """
    Archive given directory to pathname.
    :type pathname: str
    :type directory: str
    """
    orig_dir = os.getcwd()
    os.chdir(directory)
    with zipfile.ZipFile(pathname, 'w') as zip_obj:
        # Iterate over all the files in directory
        for folder_name, _, filenames in os.walk(directory):
            for filename in filenames:
                # create complete filepath of file in directory
                file_path = os.path.join(folder_name, filename)
                # Add file to zip
                zip_obj.write(file_path, file_path.replace(directory, ''))
    os.chdir(orig_dir)


def process_war(filepath, dryrun=False):
    """
    This func processes a .war file by following steps:
    1. Create a temporary dir
    2. Extract the .war to #1
    3. Move .war to BACKUP_DIR
    4. Find and process the files in #1, so the jars will be off of offending class, if any.
    5. Archive the temporary dir #1 back to the original filename
    :type filepath: str
    :param dryrun: A boolean to indicate whether the archive should be mitigated.
        False means to mitigate it.
    :type dryrun: bool
    :return: None if the war does not contain any offending class and was not changed at all;
        the filepath if the war was handled.
    """
    results = None
    # create a temp dir to extract war file
    dirpath = tempfile.mkdtemp()
    try:
        with zipfile.ZipFile(filepath) as war_zip:
            war_zip.extractall(dirpath)
    except (zipfile.error, OSError):
        LOG.warning("Bad zip file: %s", filepath)
        return None
    stat = os.stat(filepath)
    processed_files = find_zip_files(dirpath, 'war', dryrun)
    if len(processed_files) > 0:
        LOG.info("Found a VULNERABLE WAR file with: %s", filepath)
        results = filepath
        if not dryrun:
            backuppath = backup_file(filepath)
            if backuppath is None:
                LOG.error("could not process file %s", filepath)
                return None
            create_archive(filepath, dirpath)
            set_file_perms(filepath, stat)
            LOG.info("VULNERABLE FILE: %s backed up to %s", filepath, backuppath)
    shutil.rmtree(dirpath, ignore_errors=True)
    return results


def process_jar(filepath, parent_type, dryrun):
    """
    Processes a .jar file by:
    1. Proceedes only archive has vulnerable JNDI class or is not log4j version 2.16
    2. Move original file to backup folder
    3. Traverses archive files and writes new archive to original file path by skipping JNDI class
    4. Mimics permissions from original file
    """
    try:
        if not has_vulnerable_class(filepath):
            return None
        if is_safe_version(filepath):
            LOG.info("Found a safe version: %s", filepath)
            return None
    except (zipfile.error, OSError):
        LOG.debug("Bad zip file: %s", filepath)
        return None
    LOG.info("Found a VULNERABLE FILE: %s", filepath)
    if dryrun:
        # if dryrun, we don't want to change the file, just report it.
        return filepath
    stat = os.stat(filepath)
    backuppath = backup_file(filepath)
    if backuppath is None:
        LOG.error("could not process file %s", filepath)
        return None
    zin = zipfile.ZipFile(backuppath, 'r')
    zout = zipfile.ZipFile(filepath, 'w')
    for item in zin.infolist():
        if not item.filename.endswith(JNDI_PATH):
            buffer = zin.read(item.filename)
            zout.writestr(item, buffer)
    set_file_perms(filepath, stat)
    zout.close()
    zin.close()
    # don't keep backups of jar inside war
    if parent_type == 'war':
        os.remove(backuppath)
    else:
        LOG.info("VULNERABLE FILE: %s backed up to %s", filepath, backuppath)
    return filepath


def process_archive(filename, root, parent_type, dryrun=False):
    """
    Processes the filename under root
    :type filename: str
    :type root: str
    :param parent_type: Whether filename comes from a .war, value can only be None or war
    :type parent_type: str
    :param dryrun: A boolean to indicate whether the archive should be mitigated.
        False means to mitigate it.
    :type dryrun: bool
    :return: filepath if it was handled; None otherwise
    """
    filepath = root + os.path.sep + filename
    if filepath.endswith('.war'):
        return process_war(filepath, dryrun)

    return process_jar(filepath, parent_type, dryrun)


def parse_args(args):
    """
    Parse arguments
    """
    parser = argparse.ArgumentParser(description="""
        VMSA-2021-0028 vCenter tool; Version: %s
        This tool deletes the JndiLookup.class file from *.jar and *.war
        files.

        On Windows systems the tool will by default traverse the folders
        identified by the VMWARE_CIS_HOME, VMWARE_CFG_DIR, VMWARE_DATA_DIR
        and VMWARE_RUNTIME_DATA_DIR variables.

        On vCenter Appliances the tool will search by default from the root
        of the filesystem.

        All modified files are backed up if the process needs to be reversed
        due to an error.
    """ % SCRIPT_VERSION)

    parser.add_argument("-d", "--directories",
                        nargs="+",
                        default=[],
                        help="space separated list of directories to check recursively "
                             "for CVE-2021-44228 vulnerable java archive files.",
                        metavar="dirnames")
    parser.add_argument("-a", "--accept-services-restart",
                        action="store_true",
                        help="accept the restart of the services without having "
                             "manual prompt confirmation for the same")
    parser.add_argument("-r", "--dryrun",
                        action="store_true",
                        help="Run the script and log vulnerable files without "
                             "mitigating them. The vCenter services are not "
                             "restarted with this option.")
    parser.add_argument("-b", "--backup-dir",
                        help="Specify a backup directory to store original files.")
    parser.add_argument("-l", "--log-dir",
                        help="Specify a directory to store log files.")
    return parser.parse_args(args)


def get_dirnames(args):
    """
    Gets a list of directories to check for exploit.
    If no explicit parameter provided uses root folder for linux
    and a list of environment variables provided folders for windows
    """
    dirnames = args.directories if args.directories is not None else []

    if not dirnames:
        if ENV.is_windows():
            dirnames = []
            for env_var in ['VMWARE_CIS_HOME',
                            'VMWARE_CFG_DIR',
                            'VMWARE_DATA_DIR',
                            'VMWARE_RUNTIME_DATA_DIR']:
                val = os.environ.get(env_var)
                if val is not None:
                    dirnames.append(val)
            if not dirnames:
                dirnames = [os.getcwd()]
        else:
            dirnames = [os.path.abspath(os.sep)]

    for dirname in dirnames:
        if not os.path.isdir(dirname):
            LOG.debug("Error: provided '%s' path is not a directory", dirname)
            sys.exit(ERROR_PATH_NOT_A_DIRECTORY)

    return dirnames


def set_backup_dir(args):
    """
    sets backup folder location
    """
    global BACKUP_DIR

    if args.backup_dir:
        BACKUP_DIR = args.backup_dir
        # make sure BACKUP_DIR exists
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)
    else:
        BACKUP_DIR = tempfile.mkdtemp()


def print_summary(dryrun, zip_processed, flagcheck_processed, issues):
    """
    prints summary of script execution result
    """
    note = """

    NOTE: Running this script again with the --dryrun
    flag should now yield 0 vulnerable files.
    """
    summary = "\n=====     Summary     =====\n"
    if len(zip_processed) + len(flagcheck_processed) > 0:
        if dryrun:
            summary += "List of vulnerable java archive files:\n\n"
        else:
            summary += "Backup Directory: %s\n" % BACKUP_DIR
            summary += "List of processed java archive files:\n\n"
        for file_path in zip_processed:
            summary += "%s\n" % file_path

        if dryrun:
            summary += "\nList of vulnerable configuration files:\n\n"
        else:
            summary += "\nList of processed configuration files:\n\n"
        for file_path in flagcheck_processed:
            summary += "%s\n" % file_path
    elif len(issues) == 0:
        summary += "\nNo vulnerable files found!\n"

    if len(issues) > 0:
        summary += "\nFound following configuration file issues:\n\n"
        for issue in issues:
            summary += "- %s\n" % issue

    if dryrun:
        summary += "\nTotal found: %s" % (len(zip_processed) + len(flagcheck_processed))
    else:
        summary += "\nTotal fixed: %s" % (len(zip_processed) + len(flagcheck_processed))
        summary += note
    summary += "\nLog file: %s\n" % LOG.handlers[0].baseFilename
    summary += "==========================="
    LOG.info(summary)


def main(args):
    """
    Main function, this function should return an int as return code.
    """
    args = parse_args(args)

    setup_logging(args.log_dir)
    LOG.info("Script version: %s", str(SCRIPT_VERSION))
    LOG.info("vCenter type: %s", str(ENV))

    if ENV.has_vcha():
        LOG.error("You need to remove VCHA to apply the workarounds as"
                  " mentioned in Impacts section of KB https://kb.vmware.com/s/article/87081\n")
        sys.exit(ERROR_VCHA_ENABLED)

    if not args.dryrun:
        prompt_service_restart(args.accept_services_restart)
    else:
        LOG.info("Running in dryrun mode.")

    set_backup_dir(args)
    dirnames = get_dirnames(args)

    LOG.debug("Inspecting folders: %s", str(dirnames))
    zip_processed = find_zip_files(dirnames, None, args.dryrun)
    LOG.debug("Found %s vulnerable zip files.", str(len(zip_processed)))

    LOG.debug("Running vCenter Configuration checks for log4j2.formatMsgNoLookups flag.")
    flagcheck_processed, issues = patch_configuration(args.dryrun)
    LOG.debug("Found %s vulnerable configuration files.", str(len(flagcheck_processed)))

    print_summary(args.dryrun, zip_processed, flagcheck_processed, issues)

    if not args.dryrun:
        prompt_service_restart(args.accept_services_restart, start=True)
    LOG.info("Done.")
    return COMPLETED_OK


if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv[1:]))
    except Exception as e:
        LOG.exception("Unhandled exception occurred while running the script: %s", e)
        sys.exit(ERROR_UNHANDLED_EXCEPTION)
