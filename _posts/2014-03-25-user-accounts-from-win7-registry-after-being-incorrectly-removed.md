---
title: How to remove user accounts from Windows 7 registry after being incorrectly removed
permalink: /win/user-accounts-from-win7-registry-after-being-incorrectly-removed/
categories:
  - Windows
---
_Note: This usually needs to be done when the Windows 7 profile has been manually deleted and not properly removed – as Windows 7 uses a security identifier attached to the user account in the registry and this needs to be cleared as well_

_Note: It is also recommend making a backup of the registry before this change – and you may need to restart the PC for the registry entry to be able to be removed.
_ _

  1. Press Windows Key + R to open the **Run** dialog window.
  2. Type in: **regedit** and press Enter or click Ok
  3. Press yes to accept UAC prompt.
  4. Navigate to: **HKEY\_LOCAL\_MACHINESOFTWAREMicrosoftWindows NTCurrentVersionProfileList******
  5. ******This lists the SID (security identifier) that is linked to your account – scroll down the list and on the right hand side under CentralProfile and ProfileImagePath find the correct user profile you would like to remove.******
  6. ******Once you have found the correct one – right click the SID key you would like to remove and select Delete.******
  7. **Exit out of the Registry Editor and restart the workstation – the user should now be able to login and generate a new profile folder and security identifier.**
