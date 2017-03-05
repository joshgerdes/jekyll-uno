---
title:  "OSX General commands"
date:   2017-03-05 09:32:00
categories: [osx]
tags: [commands]
---
Most frequently used OSX commands

## Compress and uncompress files and folders

### ZIP

To compress: `zip -r archive_name.zip folder_to_compress`

To extract: `unzip archive_name.zip`

Exclude `_MACOSX` or `._Filename` and .ds store files, use the “-X” option

`zip -r -X archive_name.zip folder_to_compress`

### TAR.GZ

To compress: `tar -zcvf archive_name.tar.gz .`

To extract: `tar -zxvf archive_name.tar.gz`

Note: Where `.` is the folder

### TAR.BZ2

Better compression than both tar.gz and zip.

To compress: `tar -jcvf archive_name.tar.bz2 folder_to_compress`

To extract: `tar -jxvf archive_name.tar.bz2`
