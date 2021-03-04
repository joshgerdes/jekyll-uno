---
title: Basic HTML Cheatsheet
permalink: /misc/basic-html-cheatsheet/
categories:
  - Misc
---
Handy little HTML cheat-sheet for use when developing your website.

**HTML**

_**Basic Tags**_
  
<html></html> Creates an HTML document
  
<head></head> Sets off the title and other information that isn&#8217;t displayed on the Web page itself
  
<body></body> Sets off the visible portion of the document
  
Body Attributes
  
<body bgcolor=&#8221;pink&#8221;> Sets the background color, using name or hex value
  
<body text=&#8221;black&#8221;> Sets the text color, using name or hex value
  
<body link=&#8221;blue&#8221;> Sets the color of links, using name or hex value
  
<body vlink=&#8221;#ff0000&#8243;> Sets the color of followed links, using name or hex value
  
<body alink=&#8221;#00ff00&#8243;> Sets the color of links on click
  
<body ondragstart=&#8221;return false&#8221; onselectstart=&#8221;return false&#8221;> Disallows text selection with the mouse and keyboard

_**Text Tags**_
  
<pre></pre> Creates preformatted text
  
<hl></hl> Creates the largest headline
  
<h6></h6> Creates the smallest headline
  
<b></b> Creates bold text
  
<i></i> Creates italic text
  
<tt></tt> Creates teletype, or typewriter-style text
  
<cite></cite> Creates a citation, usually italic
  
<em></em> Emphasizes a word (with italic or bold)
  
<strong></strong> Emphasizes a word (with italic or bold)
  
<font size=&#8221;3&#8243;></font> Sets size of font, from 1 to 7
  
<font color=&#8221;green&#8221;></font> Sets font color, using name or hex value

_**Links**_
  
<a href=&#8221;URL&#8221;></a> Creates a hyperlink
  
<a href=&#8221;mailto:EMAIL&#8221;></a> Creates a mailto link
  
<a href=&#8221;URL&#8221;><img src=&#8221;URL&#8221;> </a> Creates an image/link
  
<a name=&#8221;NAME&#8221;></a> Creates a target location within a document
  
<a href=&#8221;#NAME&#8221;></a> Links to that target location from elsewhere in the document

_**Formatting**_
  
<p></p> Creates a new paragraph
  
<p align=&#8221;left&#8221;> Aligns a paragraph to the left (default), right, or center.
  
<br> Inserts a line break
  
<blockquote></blockquote> Indents text from both sides
  
<dl></dl> Creates a definition list
  
<dt> Precedes each definition term
  
<dd> Precedes each definition
  
<ol></ol> Creates a numbered list
  
<ul></ul> Creates a bulleted list
  
<li></li> Precedes each list item, and adds a number or symbol depending upon the type of list selected
  
<div align=&#8221;left&#8221;> A generic tag used to format large blocks of HTML, also used for stylesheets
  
<img src=&#8221;name&#8221;> Adds an image
  
<img rajaram=&#8221;name&#8221; align=&#8221;left&#8221;> Aligns an image: left, right, center; bottom, top, middle
  
<img src=&#8221;name&#8221; border=&#8221;1&#8243;> Sets size of border around an image
  
<hr /> Inserts a horizontal rule
  
<hr size=&#8221;3&#8243; /> Sets size (height) of rule
  
<hr width=&#8221;80%&#8221; /> Sets width of rule, in percentage or absolute value
  
<hr noshade /> Creates a rule without a shadow

**CSS**

font-family <selector> {font-family:<value>} <family-name> (specify) or <generic-family>~ [serif, sans-serif\*, cursive\*, fantasy*, monospace]
  
font-style <selector> {font-style:<value>} normal, italic
  
font-weight <selector> {font-weight:<value>} normal\*, bold, 100\*, 200\*, 300\*, 400\*, 500\*, 600\*, 700\*, 800\*, 900\*
  
font-size <selector> {font-size:<value>} <absolute-size>, <relative-size>*, <length>~~, <percentage>
  
color <selector> {color:<value>}
  
<color> (see [/webmonkey/stylesheets/reference/units.html &#8220;Units of Measure&#8221;)]
  
background-color <selector> {background-color:<value>}
  
<color> (see [/webmonkey/stylesheets/reference/units.html &#8220;Units of Measure&#8221;)]
  
background-image <selector> {background-image:url(<value>)} URL (relative or absolute path

margin $ <selector>{margin:<value>} <length>\*\*, <percentage>\*\*, auto(sequence:t r b l)
  
margin-top <selector>{margin-top:<value>} <length>**, <percentage>, auto
  
Margin-right <selector>{margin-right:<value>} <length>, <percentage>, auto
  
margin-bottom\* <selector>{margin-bottom:<value>} <length>\*, <percentage>\*, auto\*
  
margin-left <selector>{margin-left:<value>} <length>, <percentage>, auto
  
padding $\* <selector>{padding:<value>} <length>\*, <percentage>*, (sequence:t r b l)
  
padding-top\* <selector>{padding-top:<value>} <length>\*, <percentage>*
  
padding-right\* <selector>{padding-right:<value>} <length>\*, <percentage>*
  
padding-bottom\* <selector>{padding-bottom:<value>} <length>\*, <percentage>*
  
padding-left\* <selector>{padding-left:<value>} <length>\*, <percentage>*
  
border-color\* <selector>{border-color:<value>} <color>\*
  
border-style\* <selector>{border-style:<value>} solid\*, double\*, groove\*, ridge\*, inset\*, outset*
  
border $\* <selector>{border:<value>} <border-width>\*, <border-style>*, <color>
