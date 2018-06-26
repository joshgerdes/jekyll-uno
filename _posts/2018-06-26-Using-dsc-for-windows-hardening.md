---
date: "2018-06-26"
title: Using PowerShell DSC for Windows Hardening
author: Luke
categories:
  - PowerShell
---

I am not a DSC *(Desired State Configuration)* expert, however, the technology
has always interested me and as such, something I like to dabble in.

There are many reasons for using PowerShell DSC and hopefully today, I can help
enlighten you towards some of its use. DSC can be used for things such as:

-   Installing IIS and other Windows Features – and making sure they are
    installed!

-   Installing Apache – Yes – even on Linux!

-   Installing scripts and executables

There are other examples, but essentially Microsoft has some good documentation
around it.

<https://docs.microsoft.com/en-us/powershell/dsc/overview>

Enough about what is PowerShell DSC, one of the benefits of DSC is that you can
use them to set and maintain a certain configuration – one of the good use of
this is hardening.

Using the Windows Server 2016 and Windows 10 ADMX templates hosted on
the [IASE (Information Assurance Support
Environment)](https://iase.disa.mil/stigs/gpo/Pages/index.aspx){:target="_blank"} webpage and the
gpoguy [ADMXToDSC script](https://github.com/gpoguy/ADMXToDSC){:target="_blank"} I was able to
turn the IASE compliant GPOs into DSC files which are a good building block for
hardening.

Note: I take no responsibility for any damage incurred and definitely recommend testing and validating before running this in Production.

The rough guide of the process to replicate this is as follows:

1.  Download the [IASE Group
    Policies](https://iase.disa.mil/stigs/gpo/Pages/index.aspx){:target="_blank"} and
    [ADMXtoDSC](https://github.com/gpoguy/ADMXToDSC){:target="_blank"} script

2.  On Windows Server 2012 R2 Server *(part of an AD Domain)* with Group Policy
    Management console installed to create a new GPO called ‘WindowsServer2016’

3.  Right-click the GPO and select Import Settings

4.  Follow the prompts and import from the folder, where you had extracted the
    ADMX templates to and import the settings for the GPO you want to turn into
    a DSC script

5.  Once completed run the ADMXtoDSC script, parameters include the GPO name and
    output path.

Once done, essentially you have now created a good baseline for Windows Server
or Windows Desktop hardening desired state configuration.

The ones I created are below:

**Windows Server 2016**

{% gist d6d2c753c72f917eb9aeab83e696b578 %}

Note: I added the telnet-client and SMB1 Windows Features to make sure that
these are disabled as part of the hardening and you can easily add anything else as suited to your requirements.

**Windows 10**

{% gist 70d465d069eccda9c2f6bbb25d7b9870 %}

*Note: The Scripts is also hosted on my Github repository. Feel free to
clone/recommend improvements or fork.*

Once you have your DSC scripts you can run them locally on the server by running
the following as Administrator in PowerShell:

{% highlight powershell %}
Start-DscConfiguration -Path ./Server2016 -Wait -Verbose -Force
{% endhighlight %}

Or alternatively use [Microsoft Azure
Automation](https://docs.microsoft.com/en-us/azure/automation/automation-dsc-overview){:target="_blank"}
to set the desired state configuration baseline, apply and maintain the changes
going forward.