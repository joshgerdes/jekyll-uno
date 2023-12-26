---
title: How to forcefully clear the Trash in Linux
categories:
  - Linux
date: 2012-03-05 00:00:00 +1300
---
<p class="Style1">
  The Trash stores your recently deleted files and folders which you can usually Right click and clear to clear the Trash in Linux  – however I have ran into problems where even though you clear the Trash the files and folders you want deleted remain. Good news is that you can force the Trash to be cleared by using the Linux terminal.
</p>

  1. Open your Linux Terminal
  2. Copy these commands and paste them into the terminal and press Enter _(this will clear the Trash completely – anything in the Trash is unable to be recovered)_

&nbsp;

**`rm -rf ~/.local/share/Trash`**

<p class="Style1">
  <b><code>mkdir ~/.local/share/Trash</code></b>
</p>

<p class="Style1">
  <b><code>mkdir ~/.local/share/Trash/expunged</code></b>
</p>

<p class="Style1">
  <b><code>mkdir ~/.local/share/Trash/files</code></b>
</p>

<p class="Style1">
  <b><code>mkdir ~/.local/share/Trash/info</code></b>
</p>

<p class="Style1">
  <b> </b>
</p>

<p class="Style1">
  Note: Tested in Debian/Ubuntu variant – other Linux distributions may have the Trash location changed and you will need to find the Trash location on your Linux distribution.
</p>
