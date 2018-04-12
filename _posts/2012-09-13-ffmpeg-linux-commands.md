---
id: 1081
title: ffmpeg Linux commands
date: 2012-09-13T08:17:24+00:00
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1081
permalink: /linux/ffmpeg-linux-commands/
dsq_thread_id:
  - "4987899926"
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
  - "9"
categories:
  - Linux
---
**Getting infos from a video file**

ffmpeg -i video.avi

**Turn X images to a video sequence**

ffmpeg -f image2 -i image%d.jpg video.mpg

_This command will transform all the images from the current directory (named_
  
_image1.jpg, image2.jpg, etc…) to a video file named video.mpg._

**Turn a video to X images**

ffmpeg -i video.mpg image%d.jpg

_This command will generate the files named image1.jpg, image2.jpg, …_

_The following image formats are also availables : PGM, PPM, PAM, PGMYUV, JPEG,_
  
_GIF, PNG, TIFF, SGI._

**Encode a video sequence for the iPod/iPhone**

ffmpeg -i source_video.avi input -acodec aac -ab 128kb -vcodec mpeg4 -b 1200kb
  
-mbd 2 -flags +4mv+trell -aic 2 -cmp 2 -subcmp 2 -s 320&#215;180 -title X
  
final_video.mp4

_Explanations:_

_* Source: source_video.avi_
  
_* Audio codec: aac_
  
_* Audio bitrate: 128kb/s_
  
_* Video codec: mpeg4_
  
_* Video bitrate: 1200kb/s_
  
_* Video size: 320px by 180px_
  
_* Generated video: final_video.mp4_

**Encode video for the PSP**

ffmpeg -i source_video.avi -b 300 -s 320&#215;240 -vcodec xvid -ab 32 -ar 24000
  
-acodec aac final_video.mp4

_Explanations:_

_* Source: source_video.avi_
  
_* Audio codec: aac_
  
_* Audio bitrate: 32kb/s_
  
_* Video codec: xvid_
  
_* Video bitrate: 1200kb/s_
  
_* Video size: 320px by 180px_
  
_* Generated video: final_video.mp4_

**Extracting sound from a video, and save it as Mp3**

ffmpeg -i source_video.avi -vn -ar 44100 -ac 2 -ab 192 -f mp3 sound.mp3

_Explanations:_

_* Source video: source_video.avi_
  
_* Audio bitrate: 192kb/s_
  
_* Output format: mp3_
  
_* Generated sound: sound.mp3_

**Convert a wav file to Mp3**

ffmpeg -i son\_origine.avi -vn -ar 44100 -ac 2 -ab 192 -f mp3 son\_final.mp3

**Convert .avi video to .mpg**

ffmpeg -i video\_origine.avi video\_finale.mpg

**Convert .mpg to .avi**

ffmpeg -i video\_origine.mpg video\_finale.avi

**Convert .avi to animated gif(uncompressed)**

ffmpeg -i video\_origine.avi gif\_anime.gif

**Mix a video with a sound file**

ffmpeg -i son.wav -i video\_origine.avi video\_finale.mpg

**Convert .avi to .flv**

ffmpeg -i video_origine.avi -ab 56 -ar 44100 -b 200 -r 15 -s 320&#215;240 -f flv
  
video_finale.flv

**Convert .avi to dv**

ffmpeg -i video_origine.avi -s pal -r pal -aspect 4:3 -ar 48000 -ac 2
  
video_finale.dv

_or_

ffmpeg -i video\_origine.avi -target pal-dv video\_finale.dv

**Convert .avi to mpeg for dvd players**

ffmpeg -i source_video.avi -target pal-dvd -ps 2000000000 -aspect 16:9
  
finale_video.mpeg

_Explanations:_

_* target pal-dvd: Output format_
  
_* ps 2000000000 maximum size for the output file, in bits (here, 2 Gb)_
  
_* aspect 16:9 : Widescreen_

**Compress .avi to divx**

ffmpeg -i video\_origine.avi -s 320&#215;240 -vcodec msmpeg4v2 video\_finale.avi

**Compress Ogg Theora to Mpeg dvd**

ffmpeg -i film\_sortie\_cinelerra.ogm -s 720&#215;576 -vcodec mpeg2video -acodec mp3
  
film_terminée.mpg

**Compress .avi to SVCD mpeg2**

_**NTSC format:**_

ffmpeg -i video\_origine.avi -target ntsc-svcd video\_finale.mpg

_**PAL format:**_

ffmpeg -i video\_origine.avi -target pal-svcd video\_finale.mpg

**Compress .avi to VCD mpeg2**

_Convert file to Matroska container without re-encoding_

ffmpeg -i input_file.wmv -vcodec copy -sameq -acodec copy -f matroska
  
output_file.mkv

_**NTSC format:**_

ffmpeg -i video\_origine.avi -target ntsc-vcd video\_finale.mpg

_**PAL format:**_

ffmpeg -i video\_origine.avi -target pal-vcd video\_finale.mpg

** Multi-pass encoding with ffmpeg**

ffmpeg -i fichierentree -pass 2 -passlogfile ffmpeg2pass fichiersortie-2

&nbsp;