---
title:  "How to Add Subtitles to a Quicktime Movie"
date:   2017-03-12 09:33:00
categories: [multimedia]
tags: [srt]
---
This is a script to add a `srt` subtitle to a movie without loosing quality in the process.

It uses **iconv** to normalize in UTF-8 and **ffmpeg** to add the subtitles inside the video file. tested in MacOSX Sierra

``` bash
#!/usr/bin/env bash

iconv -f WINDOWS-1252 -t UTF-8  *.srt > out.srt
ffmpeg -i *.mp4 -i out.srt -c:v copy -c:a copy -c:s mov_text -metadata:s:s:0 language=esp out.mp4
```
