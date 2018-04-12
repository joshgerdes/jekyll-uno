---
id: 1172
title: iATKOS v2.0i Installation
date: 2012-03-31T20:04:59+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1172
permalink: /osx/iatkos-v2-0i-installation/
dsq_thread_id:
  - "4856287622"
omc_review_enable:
  - "0"
omc_user_ratings_visibility:
  - "0"
omc_review_type:
  - stars
omc_criteria_display:
  - 'n'
omc_featured_post:
  - "0"
omc_comment_type:
  - wp
mfn-post-love:
  - "0"
post_views_count:
  - "27"
categories:
  - Mac OSX
---
_ Credits goes to Apple and OSX86 community. This is just the instructions for the install._
  
Attention:

1- This DVD is designed for Intel architectures.
  
Minimum requirements: Intel SSE3 CPU, 512MB RAM, 12GB free space on target partition.

2- This DVD includes Apple&#8217;s OS X Leopard 10.5.2 (9C7010) installation.

3- Make sure that the md5 checksum of your iATKOS iso image matches the one posted on our website. Otherwise you may have a faulty DVD image. Use quality media/burner and burn slowly.
  
Information:

&#8211; This release supports GPT (Guid Partition Table) partition map scheme. You can change your partition table type to GPT via Disk Utility or some other partition managers. We advice Parted Magic Live CD which is based on GParted.

&#8211; This release also includes Darwin EFI emulation boot for MBR (Master Boot Record) harddrives. Intel Core CPUs can use stock kernel and stock ACPIPlatform with EFI emulation on MBR and with GPT. This increases stability and performance.

&#8211; Intel CoreDuo Processors have appropriate SpeedStep Technology which is stable in OS X. If you have such processor, you can enable throttling feature using the &#8220;SpeedStep&#8221; package which you can find under system drivers section. Note that speedstep kernel is included in iATKOS main system, so don&#8217;t select any of the kernels with speedstep support if you don&#8217;t want to have kernel panic.

&#8211; There are some boot options for some various hardware. Boot DVD, press F8 and enter:
  
nforce -v
  
for nForce motherboards with intel SSE3 CPU
  
nforce_core -v
  
for nForce motherboards with Intel Core CPU
  
toh -v
  
for booting with ToH 9.2.0 kernel which works nice on many types of hardware
  
Installation:

1- Run Disk Utility via Utilities menu and erase the target partition for clean install. Do partitioning if you need to.

a- You can choose MBR (Master Boot Record) or GPT (Guid Partition Table) via partitioning options. If you want to change your existing partition table type, know that all your existing data on disk will be gone.
  
b- For Windows fellows that has not tested this amazing system yet and that does not want to loose their windows software, porn and virus&trojan archive on D:, should use Parted Magic Live CD for preparing an active primary target partition and after that, just erase it via diskutil. Jump to Step 2.

2- Select the destination for installation.

3- Click customize and select what you need.

4- Click Install.

Install time is about 20 minutes.

&nbsp;

Multiboot:

iATKOS 2.0i has no integrated procedure for multibooting but preparing a multiboot GPT or MBR system with this release is easier than ever.

Here is a &#8221;How To&#8221; for GPT and MBR triple boot including Mac-Vista-Linux.

&#8211; MBR (Master Boot Record) triple boot &#8211;

&#8211; Change your partition table type to MBR (msdos type) and create 3 primary partitions by using Parted Magic Live CD or iATKOS Disk Utility. HFS+ format for OS X target, Fat32 for the others.
  
Note: %99.99999 of the PC harddrives already have MBR partition map scheme (msdos type) which you can change it to GPT via Parted Magic CD or iATKOS Disk Utility if you like to.

&#8211; Add boot flag to Vista or Linux target and install the OS&#8217; in any order you like. For linux, do not install bootloader to MBR, install it to linux root.

&#8211; Boot iATKOS 2.0i DVD and install OS X to its target as usual.

&#8211; Now you need to repair Vista. Add boot flag to Vista partition, boot Vista DVD, select repair, add boot flag to OS X partition, thats all.

Now you have triple boot on MBR.

Note: Adding boot flag to MBR partitions: Boot Parted Magic Live CD, right click to partition, select flags and click to boot.

&#8211; GPT (Guid Partition Table) triple boot &#8211;

&#8211; Change your partition table type to GPT (Guid Partition Table) and create 3 partitions by using Parted Magic Live CD or iATKOS Disk Utility. HFS+ format for OS X target, Fat32 (msdos) for the others.

&#8211; Boot iATKOS 2.0i DVD, install only bootloader to OS X target. \***

&#8211; Boot Vista DVD and install it to first Fat32 partition.
  
(Note: System marks first Fat32 partition or booting Foreign OS&#8217;. If you choose other than first Fat32 as target for Vista, then during installation, system will not continue install process at first Vista boot.)

&#8211; Boot Linux media and install the OS. Install the bootloader to linux root.
  
(Note: Some live linux cd stuff (knoppix, kanotix, parsix etc.) has built-in installer applications and they use gparted for partitioning and formatting targets. At this point, formatting target to linux fs via Gparted is not a good choice, use fdisk just for changing the target partition type from &#8221;c0&#8221; to &#8221;83&#8221; which is linux partition type and then continue installation.)

&#8211; Boot iATKOS 2.0i DVD and install OS X as usual.

Now you have triple boot on GPT, thats all.

As you see, preparing multiboot system on GPT is more practical and easier.
  
Darwin on GPT will see other OS&#8217; as Foreign Boot.

\*** For pro-users: You can re-install Darwin bootloader by booting the iATKOS DVD with -s. Boot with -s and enter darwin command, follow the instructions. For MBR HD, you can add boot flag via fdisk after darwin installation.
  
Known Issues:

1- Jmicron IDE controllers are known to have issues with OS X.

2- Some 965 chipset MSI and ASUS motherboards (desktop and laptop) have issues with this OS. ACPI errors while booting with DVD and also with hd. There will be patches for those uncompatible devices and there is also a patch for 1.0ir2.

3- This dvd may not include all the necessary drivers required by your setup. Additional steps may be needed to be taken by the user to setup and use such components.

4- Be sure that the labels of your hfs+ partitions are not similar. ie. Mac 1, MacOS or Leopard X, Leopard Y. Installer may fail to determine the target partition to install the system if the labels match.
  
Unsuccessful Installation and Related Symptoms:
  
1- I get the error &#8220;com.apple.Boot.plist is not found&#8221; while booting the DVD

&#8211;> You are probably trying to boot from an unsupported controller.
  
~ You should use usb dvd rom drive, or you may need sata-ide convertor for your dvd rom drive (jmicron).

2- System freezes at grey screen by booting the DVD.

&#8211;> You probably have an unsupported chipset.
  
*965 chipset ASUS or MSI motherboard/laptop
  
*many VIA, SIS, ATI chipset motherboards
  
~ Change your hardware
  
~ A patch can be possible for 965 ASUS/MSI hardware, so keep on watching this community.

\***\***\***\***\***\***\***\***\***\***\***\***\***\****

For additional Help and instructions, here is the website and irc channel.

web: http://www.uphuck.com
  
IRC: irc.atlantis-irc.net #uphuck.DVD #osx86.turk

\***\***\***\***\***\***\***\***\***\***\***\***\***\***