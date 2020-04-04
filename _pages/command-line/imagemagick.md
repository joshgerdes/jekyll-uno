---
title: Image Magick
layout: page
---

## Setup

### Linux

```
sudo apt-get install imagemagick
```

### MacOS

```
brew install imagemagick
```

## Usage

ImageMagick provides you with two powerful commands: convert and mogrify.

### Mogrify

Mogrify generally takes the same arguments as convert, but allows you to process multiple images and replace them in place.
Therefore it is good habit to backup those images beforehand. This will, for example, resize all images in current folder to 256 * 256.

```
mogrify -resize 256x256 *.jpg
```

### Convert

With convert you can specify a single source and output filename. This will convert the image from PNG to JPG.

```
convert pic.png pic.jpg
```

Mogrify equivalent for that would be:

```
mogrify -format jpg *.png
```


## References

https://hackernoon.com/save-time-by-transforming-images-in-the-command-line-c63c83e53b17
