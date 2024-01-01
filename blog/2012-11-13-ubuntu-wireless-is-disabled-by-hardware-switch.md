---
title: 'Ubuntu &#8211; Wireless is disabled by hardware switch'
date: 2012-11-13 00:00:00 +1300
authors: [Luke]
tags:
  - Linux
---

This commonly occurs right after an upgrade/update to the operating system.

  1. First thing is first – your laptop will probably have a Wireless On & Off feature which is either on the side of the laptop chassis or front usually in the form of a button or switch. If it’s off, turn it on!
  2. If the wireless is turned on and you are still getting an issue open a Terminal and type: `sudo rfkill unblock wifi`
  3. Press Enter
  4. You should now be able to access the wireless.

If neither of the above work – then the problem most likely is you’re wireless on & off switch and it might need to be rewired to be permanently on.