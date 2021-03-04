---
title: A program on your computer has corrupted IE8 default search provider settings
  fix
date: 2012-09-06 06:09:37 +12:00
permalink: "/win/search-provider-settings-fix/"
categories:
- Windows
id: 838
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=838
dsq_thread_id:
- '2432265137'
omc_review_enable:
- '0'
omc_user_ratings_visibility:
- '0'
omc_review_type:
- stars
omc_criteria_display:
- n
omc_featured_post:
- '0'
omc_comment_type:
- wp
mfn-post-love:
- '0'
post_views_count:
- '7'
---

Nothing causes more frustration, then when your favorite Internet Explorer search engine keeps resetting. This is how you fix it.

&#8221; IE8 will reset the search provider setting to default setting of xxx search. IE8 will open the search provider dialog where you can change your search provider&#8221;.

  1. Close any instances of Internet Explorer you have open
  2. Click **Start**.
  3. Click **Run**.
  4. Type in **regedit** and press enter
  5. In the editor, expand and navigate to the following registry key: _**HKEY\_CURRENT\_USERSoftwareMicrosoftWindowsCurrentVersionExplorer**_<wbr>_**User**_</wbr>
  6. **Right** **click** User **Shell** Folders
  7. Select **New** and then **Expandable** **String** value.
  8. A new value is added in right pane
  9. Type in **AppData** and press enter
 10. Double click AppData
 11. Under value **data** type in_** %USERPROFILE%Application Dat**_**a**.  _Note: If there is already AppData in the right pane, double click and correct it to %USERPROFILE%Application Data_
 12. **Exit** Registry Editor
 13. **Open** **Internet** Explorer