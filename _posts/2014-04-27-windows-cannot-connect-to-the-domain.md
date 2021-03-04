---
title: Windows cannot connect to the domain
permalink: /win/windows-cannot-connect-to-the-domain/
categories:
  - Windows
---
  1. Open **Active Directory Users & Computers**
  2. Right click **Computers**
  3. **Search** for the **computer** **name** you would like to remove and **right** **click** and select **Reset**
  4. Now on the **computer** **logon **using a local computer account.
  5. **Right** **click** Computer/My **Computer**
  6. Select **Properties**
  7. **Click** **Computer** **Name** tab and select **Change**
  8. **Click** on **Member of** &#8211; and **change** from **Domain** to **Workgroup** and click Ok
  9. Windows will prompt you to restart your Computer &#8211; select **Restart** **later**
 10. **Select** **Domain** and enter in the domain name you wish to reconnect to and click **Ok**
 11. **Enter** in your domain **credentials** to add the workstation back to the domain and click **Ok** **to** **restart** the computer.

Note: The benefit of doing the Reset in Active Directory first &#8211; allows you to maintain the computer groups and security identifier without loosing it.

You can also use the following Powershell command on the local PC to restore the secure channel to the domain: `Test-ComputerSecureChannel -Repair`
