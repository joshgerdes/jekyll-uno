---
title:  "Entity Framework Performance Cheat Sheet"
date:   2012-08-01
canonical: http://blog.staticvoid.co.nz/2012/7/17/entity_framework-navigation_property_basics_with_code_first
redirect_from:
  - 2012/7/17/entity_framework-navigation_property_basics_with_code_first
---
<span style="background-color: white; font-size: large;">So what is a navigation property</span>

Navigation properties are Entity Frameworks way of representing Foreign Key relationships inside the database. Navigation properties allow you to define relationships between entities (rows in your database) in a way that makes sense in an object oriented language. Consider the following database:

<div class="separator" style="clear: both; text-align: center;">
<a href="http://2.bp.blogspot.com/-Hy0QyoqH4bM/T7N37OQ5EVI/AAAAAAAAAO4/vNT5gsZaWg4/s1600/user_post_relationship.PNG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://2.bp.blogspot.com/-Hy0QyoqH4bM/T7N37OQ5EVI/AAAAAAAAAO4/vNT5gsZaWg4/s1600/user_post_relationship.PNG" /></a></div>
<div class="separator" style="clear: both; text-align: center;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
As you can see a post has an author and that is&nbsp;relationaly&nbsp;linked inside our database. So how would we represent this same structure inside of an application (if we ignore the way this is&nbsp;implemented&nbsp;in a relational database)? It seems sensible that we would model this same structure with something like the following:</div>
<br />
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">class</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">User</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; {<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">string</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> Name { </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">get</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">set</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; }<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; }<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<br /></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">class</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">Post</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; {<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">User</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> Author { </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">get</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">set</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; }<o:p></o:p></span></div>
<div class="MsoNormal">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">&nbsp;&nbsp;&nbsp; }</span></div>
<div class="MsoNormal">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;"><br /></span></div>
<div class="MsoNormal">
<span style="text-align: left;">Which means we can use it in code like this:</span></div>
<div class="MsoNormal">
<span style="text-align: left;"><br /></span></div>
<div class="MsoNormal">
</div>
<div class="MsoNormal">
<span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">&nbsp; &nbsp;&nbsp;String</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">.Format(</span><span style="background-color: white; color: maroon; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">"{0} wrote
this post"</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">, post.Author.Name);</span></div>
<div class="MsoNormal" style="text-align: left;">
<br /></div>
<div class="MsoNormal" style="text-align: left;">
What Entity Framework navigation&nbsp;proprieties&nbsp;do is to allow us to do just this with our database models. For example the above database structure could be represented as:</div>
<div class="MsoNormal" style="text-align: left;">
<br /></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">class</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">User</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; {<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">int</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> Id { </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">get</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">set</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; }<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">string</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> Name { </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">get</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">set</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; }<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; }<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<br /></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">class</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">Post</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; {<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">int</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> Id { </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">get</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">set</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; }<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">User</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> Author { </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">get</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">set</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; }<o:p></o:p></span></div>
<div class="MsoNormal">
<o:p></o:p></div>
<div class="MsoNormal" style="text-align: left;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">&nbsp; &nbsp;&nbsp;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">}</span>&nbsp;</div>
<div class="MsoNormal" style="text-align: left;">
<br /></div>
<div class="MsoNormal" style="text-align: left;">
<span style="font-size: large;">So how do Navigation Properties work?</span></div>
<div class="MsoNormal" style="text-align: left;">
<br /></div>
<div class="MsoNormal" style="text-align: left;">
When you are using navigation properties in your code you are asking Entity Framework to automatically perform a SQL join between your two tables. For example:</div>
<div class="MsoNormal" style="text-align: left;">
<br /></div>
<div class="MsoNormal" style="text-align: left;">
</div>
<div class="MsoNormal">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">&nbsp; &nbsp;&nbsp;context.Posts.Where(p =&gt; p.Author.Name
== </span><span style="background-color: white; color: maroon; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">"Luke"</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">);</span></div>
<br />
<div class="MsoNormal" style="text-align: left;">
will be translated into the following SQL*:</div>
<div class="MsoNormal" style="text-align: left;">
<br /></div>
<div class="MsoNormal" style="text-align: left;">
</div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">SELECT</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> <o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp; &nbsp; p.</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">Id</span><span style="background-color: white; color: grey; font-family: Consolas; font-size: 9.5pt;">,</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> <o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp; &nbsp; p.</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">Author_Id</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">FROM</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp; </span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">Posts&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">AS</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;p<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: grey; font-family: Consolas; font-size: 9.5pt;">INNER</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: grey; font-family: Consolas; font-size: 9.5pt;">JOIN</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">Users&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">AS</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> u </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">ON</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;p.</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">Author_Id&nbsp;</span><span style="background-color: white; color: grey; font-family: Consolas; font-size: 9.5pt;">=</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;u.</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">Id<o:p></o:p></span></div>
<div class="MsoNormal">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">WHERE</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">&nbsp;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">u.</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">Name</span><o:p></o:p><span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 14px;">&nbsp;</span><span style="background-color: white; color: grey; font-family: Consolas; font-size: 9.5pt; line-height: 14px;">=</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 14px;">&nbsp;</span><span style="background-color: white; color: red; font-family: Consolas; font-size: 9.5pt; line-height: 14px;">N'Luke'</span></div>
<br />
<div class="MsoNormal" style="text-align: left;">
As you can see our relationship in c# has been converted into the equivalent SQL join.</div>
<div class="MsoNormal" style="text-align: left;">
<br /></div>
<div class="MsoNormal" style="text-align: left;">
<span style="font-size: large;">So how do I load my properties (Why is my navigation property null)?</span></div>
<div class="MsoNormal" style="text-align: left;">
<br /></div>
<div class="MsoNormal" style="text-align: left;">
Navigation properties are not loaded by default, so its important to know how and when you need to&nbsp;load&nbsp;navigation properties. So lets look at some scenarios and see what entity framework will give us. These scenarios are based off the following data:<br />
<br />
<table border="1" cellpadding="0" cellspacing="0" class="MsoTableGrid" style="border-collapse: collapse; border: none; mso-border-alt: solid windowtext .5pt; mso-padding-alt: 0cm 5.4pt 0cm 5.4pt; mso-yfti-tbllook: 1184;">
 <tbody>
<tr>
  <td colspan="2" style="border: solid windowtext 1.0pt; mso-border-alt: solid windowtext .5pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 90.45pt;" valign="top" width="121"><div class="MsoNormal" style="margin-bottom: 0.0001pt;">
User<o:p></o:p></div>
</td>
 </tr>
<tr>
  <td style="border-top: none; border: solid windowtext 1.0pt; mso-border-alt: solid windowtext .5pt; mso-border-top-alt: solid windowtext .5pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 47.95pt;" valign="top" width="64"><div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<b>Id<o:p></o:p></b></div>
</td>
  <td style="border-bottom: solid windowtext 1.0pt; border-left: none; border-right: solid windowtext 1.0pt; border-top: none; mso-border-alt: solid windowtext .5pt; mso-border-left-alt: solid windowtext .5pt; mso-border-top-alt: solid windowtext .5pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 42.5pt;" valign="top" width="57"><div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<b>Name<o:p></o:p></b></div>
</td>
 </tr>
<tr>
  <td style="border-top: none; border: solid windowtext 1.0pt; mso-border-alt: solid windowtext .5pt; mso-border-top-alt: solid windowtext .5pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 47.95pt;" valign="top" width="64"><div class="MsoNormal" style="margin-bottom: 0.0001pt;">
1<o:p></o:p></div>
</td>
  <td style="border-bottom: solid windowtext 1.0pt; border-left: none; border-right: solid windowtext 1.0pt; border-top: none; mso-border-alt: solid windowtext .5pt; mso-border-left-alt: solid windowtext .5pt; mso-border-top-alt: solid windowtext .5pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 42.5pt;" valign="top" width="57"><div class="MsoNormal" style="margin-bottom: 0.0001pt;">
Luke<o:p></o:p></div>
</td>
 </tr>
<tr>
  <td style="border-top: none; border: solid windowtext 1.0pt; mso-border-alt: solid windowtext .5pt; mso-border-top-alt: solid windowtext .5pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 47.95pt;" valign="top" width="64"><div class="MsoNormal" style="margin-bottom: 0.0001pt;">
2<o:p></o:p></div>
</td>
  <td style="border-bottom: solid windowtext 1.0pt; border-left: none; border-right: solid windowtext 1.0pt; border-top: none; mso-border-alt: solid windowtext .5pt; mso-border-left-alt: solid windowtext .5pt; mso-border-top-alt: solid windowtext .5pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 42.5pt;" valign="top" width="57"><div class="MsoNormal" style="margin-bottom: 0.0001pt;">
Bob<o:p></o:p></div>
</td>
 </tr>
</tbody></table>
<br />
<table border="1" cellpadding="0" cellspacing="0" class="MsoTableGrid" style="border-collapse: collapse; border: none; mso-border-alt: solid windowtext .5pt; mso-padding-alt: 0cm 5.4pt 0cm 5.4pt; mso-yfti-tbllook: 1184;">
 <tbody>
<tr>
  <td colspan="2" style="border: solid windowtext 1.0pt; mso-border-alt: solid windowtext .5pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 90.45pt;" valign="top" width="121"><div class="MsoNormal" style="margin-bottom: 0.0001pt;">
Post<o:p></o:p></div>
</td>
 </tr>
<tr>
  <td style="border-top: none; border: solid windowtext 1.0pt; mso-border-alt: solid windowtext .5pt; mso-border-top-alt: solid windowtext .5pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 47.95pt;" valign="top" width="64"><div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<b>Id<o:p></o:p></b></div>
</td>
  <td style="border-bottom: solid windowtext 1.0pt; border-left: none; border-right: solid windowtext 1.0pt; border-top: none; mso-border-alt: solid windowtext .5pt; mso-border-left-alt: solid windowtext .5pt; mso-border-top-alt: solid windowtext .5pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 42.5pt;" valign="top" width="57"><div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<b>Author_Id<o:p></o:p></b></div>
</td>
 </tr>
<tr>
  <td style="border-top: none; border: solid windowtext 1.0pt; mso-border-alt: solid windowtext .5pt; mso-border-top-alt: solid windowtext .5pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 47.95pt;" valign="top" width="64"><div class="MsoNormal" style="margin-bottom: 0.0001pt;">
1<o:p></o:p></div>
</td>
  <td style="border-bottom: solid windowtext 1.0pt; border-left: none; border-right: solid windowtext 1.0pt; border-top: none; mso-border-alt: solid windowtext .5pt; mso-border-left-alt: solid windowtext .5pt; mso-border-top-alt: solid windowtext .5pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 42.5pt;" valign="top" width="57"><div class="MsoNormal" style="margin-bottom: 0.0001pt;">
1<o:p></o:p></div>
</td>
 </tr>
<tr>
  <td style="border-top: none; border: solid windowtext 1.0pt; mso-border-alt: solid windowtext .5pt; mso-border-top-alt: solid windowtext .5pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 47.95pt;" valign="top" width="64"><div class="MsoNormal" style="margin-bottom: 0.0001pt;">
2<o:p></o:p></div>
</td>
  <td style="border-bottom: solid windowtext 1.0pt; border-left: none; border-right: solid windowtext 1.0pt; border-top: none; mso-border-alt: solid windowtext .5pt; mso-border-left-alt: solid windowtext .5pt; mso-border-top-alt: solid windowtext .5pt; padding: 0cm 5.4pt 0cm 5.4pt; width: 42.5pt;" valign="top" width="57"><div class="MsoNormal" style="margin-bottom: 0.0001pt;">
2<o:p></o:p></div>
</td>
 </tr>
</tbody></table>
<div style="text-align: -webkit-auto;">
<br /></div>
<b>Case 1 :&nbsp;</b><br />
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;"><br /></span><br />
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">&nbsp; &nbsp; context.Posts.ToArray();</span><br />
<br />
When we make this request we get&nbsp;the following:<br />
<div class="MsoNormal">
<o:p></o:p></div>
<br />
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp;&nbsp;&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">ArrayOfPost</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Post</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Id</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">1</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Id</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Author</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">null</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Author</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Post</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Post</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Id</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">2</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Id</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Author</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">null</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Author</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Post</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">ArrayOfPost</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<br />
As you can see we have retrieved all the posts but&nbsp;haven't received&nbsp;any of the linked authors.<br />
<br /></div>
<div class="MsoNormal" style="text-align: left;">
<b>Case 2:</b><br />
<br />
<div class="MsoNormal">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">&nbsp; &nbsp;&nbsp;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">context.Posts.Where(p =&gt; p.Author.Name == </span><span style="background-color: white; color: maroon; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">"Luke"</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">).ToArray();</span><span style="font-family: Consolas; font-size: 9.5pt; line-height: 115%;"><o:p></o:p></span></div>
<br />
When we make this request we get&nbsp;the following:
<br />
<br />
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp;&nbsp;&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">ArrayOfPost</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Post</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Id</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">1</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Id</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Author</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">null</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Author</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Post</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">ArrayOfPost</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<br />
In this case the <i>where </i>clause successfully interacts with the author to filter by name, however when the results are returned the author is still not linked.<br />
<br />
<b>Case 3:</b><br />
<br />
<div class="MsoNormal">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">&nbsp; &nbsp;&nbsp;using</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;"> System.Data.Entity;</span><o:p></o:p><span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">&nbsp;</span><span style="background-color: white; color: green; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">//this is required for .Include</span></div>
<div class="MsoNormal">
<br /></div>
<div class="MsoNormal">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">&nbsp; &nbsp;&nbsp;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">context.Posts.Include(p =&gt; p.Author).ToArray();</span><span style="font-family: Consolas; font-size: 9.5pt; line-height: 115%;"><o:p></o:p></span></div>
<div class="MsoNormal">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;"><br /></span></div>
<br />
When we make this request we get the following:
<br />
<br />
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp;&nbsp;&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">ArrayOfPost</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Post</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Id</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">1</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Id</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Author</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Id</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">1</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Id</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Name</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">Luke</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Name</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Author</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Post</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Post</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Id</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">2</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Id</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Author</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Id</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">2</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Id</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Name</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">Bob</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Name</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Author</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt;">Post</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">&gt;</span></div>
<div class="MsoNormal">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">&nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 13px;">&lt;</span><span style="background-color: white; color: #a31515; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">ArrayOfPost</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">&gt;</span></div>
<br />
As you can see by adding a&nbsp;
<span style="background-color: white; font-family: Consolas; font-size: 13px; line-height: 14px;">.Include</span>&nbsp;statement we are able to fetch the linked authors.<br />
<br />
<b>A note on lazy loading</b><br />
<br />
Lazy loading is also an alternative to using the .Include syntax, however I recommend against using it in almost all cases as it makes it very easy to introduce subtle performance issues into your application. in addition using the include syntax makes it much more obvious what queries your code performs so&nbsp;increases&nbsp;readability.<br />
<br />
<span style="font-size: large;">How does Entity Framework detect Navigation Properties</span><br />
<br />
When entity framework examines a class which is attached to the context it finds other complex type properties on the class and assumes that they are a foreign key to that table. Entity framework then creates a foreign key with the name <i>[PropertyName]_[PropertyIdName]</i> for example in the case of the post class the <i>Author </i>is <i>[PropertyName]</i>&nbsp;and in the user table <i>Id</i> is the Id. This means <i>Author_Id</i> is generated as the foreign key name.<br />
<br />
The rules around navigation properties what's&nbsp;acceptable and how they are generated are defined by a set of conventions. Im not going to go into any more detail on how these work but for more information you can take a look at the following pages:<br />
<ul>
<li><a href="http://blogs.msdn.com/b/adonet/archive/2011/01/10/ef-feature-ctp5-pluggable-conventions.aspx">EF Feature CTP5: Pluggable Conventions</a></li>
<li><a href="http://msdn.microsoft.com/en-us/library/system.data.entity.modelconfiguration.conventions(v=vs.103).aspx">MSDN -&nbsp;System.Data.Entity.ModelConfiguration.Conventions Namespace</a></li>
<li><a href="http://stackoverflow.com/a/11081568/1070291">Entity Framework Navigation Property generation rules</a></li>
</ul>
<br />
<div>
<span style="background-color: white; font-size: large;">More than the defaults with the Model Builder</span></div>
<div>
<br /></div>
<div>
Entity framework provides a mechanism to configure additional information about navigation properties. This additional configuration can be done using the Model Builder. The model builder allows control over how Entity Framework represents the database, one of the features of the model builder allows for control over how foreign keys in the database are translated to Navigation Properties in the Entity Framework Model.<br />
<br />
To get access to the model builder you will need to override the&nbsp;<i>OnModelCreating </i>method on your <i>DbContext</i>. You can then use the <i>modelBuilder </i>argument to structure your Entity Framework Model.<br />
<br />
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">class</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">MyContext</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> : </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">DbContext</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; {</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">protected</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">override</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">void</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> OnModelCreating(</span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">DbModelBuilder</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> modelBuilder)<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {</span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }&nbsp;&nbsp;&nbsp;
<o:p></o:p></span></div>
<div class="MsoNormal">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">&nbsp;&nbsp;&nbsp; }</span><o:p></o:p></div>
<br />
The Model Builder uses a two part fluent expression to define navigation properties within the model. The first part of the expression defines the navigation property on the current entity, the second part of the&nbsp;expression&nbsp;defines the reverse navigation&nbsp;property. Navigation properties properties can be either <b>Optional </b>(ie <i>0..1 to x</i>), <b>Required </b>(ie <i>1 to x</i>) or <b>Many </b>(ie <i>* to x</i>). So lets take a look at some examples:<br />
<h4>






<span style="background-color: white;">Optional relationship</span></h4>
<span style="background-color: white;">If you have the following classes:</span><br />
<div class="separator" style="clear: both; text-align: left;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
</div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
</div>
<div class="MsoNormal" style="margin: 0cm 0cm 0.0001pt 36pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">class</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">Entity1</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin: 0cm 0cm 0.0001pt 36pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">{<o:p></o:p></span></div>
<div class="MsoNormal" style="margin: 0cm 0cm 0.0001pt 36pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">int</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> Id { </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">get</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">set</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; }<o:p></o:p></span></div>
<div class="MsoNormal" style="margin: 0cm 0cm 0.0001pt 36pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">}<o:p></o:p></span></div>
<div class="MsoNormal" style="margin: 0cm 0cm 0.0001pt 36pt;">
<br /></div>
<div class="MsoNormal" style="margin: 0cm 0cm 0.0001pt 36pt;">
<span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">class</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">Entity2</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin: 0cm 0cm 0.0001pt 36pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">{<o:p></o:p></span></div>
<div class="MsoNormal" style="margin: 0cm 0cm 0.0001pt 36pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">int</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> Id { </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">get</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">set</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; }<o:p></o:p></span></div>
<div class="MsoNormal" style="margin: 0cm 0cm 0.0001pt 36pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">Entity1</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> Entity1 { </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">get</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">set</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; }<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-left: 36.0pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">}</span><o:p></o:p></div>
<br />
<div class="separator" style="clear: both;">
Using the following model builder statement</div>
<div class="separator" style="clear: both;">
<br /></div>
<div class="separator" style="clear: both;">
</div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">protected</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">override</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">void</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;OnModelCreating(</span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">DbModelBuilder</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;modelBuilder)<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; modelBuilder.Entity&lt;</span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">Entity2</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&gt;().HasOptional(e =&gt; e.Entity1).WithMany();<o:p></o:p></span></div>
<div class="MsoNormal">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 14px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }&nbsp; &nbsp;&nbsp;</span><span style="font-family: Consolas; font-size: 9.5pt; line-height: 14px;"><o:p></o:p></span><br />
<div>
<br /></div>
</div>
<span style="background-color: white;">Will create the following relationship</span><br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://4.bp.blogspot.com/-nWRNq4Pc9nw/UAF10k6-u2I/AAAAAAAAAPY/ga95LuYl0bg/s1600/Optional+relationship.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="129" src="http://4.bp.blogspot.com/-nWRNq4Pc9nw/UAF10k6-u2I/AAAAAAAAAPY/ga95LuYl0bg/s320/Optional+relationship.png" width="320" /></a></div>
<div class="separator" style="clear: both; text-align: center;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
<b>Note </b>the two parts of the query the first to define Entity1 navigation property, the first part defines an optional&nbsp;relationship&nbsp;(ie a&nbsp;nullable&nbsp;foreign key) and the second part <i>.WithMany()</i> defines the remote&nbsp;entity's&nbsp;(<i>Entity1</i>) multiplicity. Using <i>.WithMany()</i> with no argument tells Entity Framework that the relationship does not have a remote navigation property.</div>
<h4>






Required Relationship</h4>
<div class="separator" style="clear: both; text-align: left;">
<span style="background-color: white;">If you have the following classes:</span></div>
<div class="separator" style="clear: both; text-align: left;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
</div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">class</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">Entity1</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; {<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">int</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> Id { </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">get</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">set</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; }<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">List</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&lt;</span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">Entity2</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&gt; Entity2s { </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">get</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">set</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; }<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; }<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<br /></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">class</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">Entity2</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; {<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">int</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> Id { </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">get</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">set</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; }<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">Entity1</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> Entity1 { </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">get</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">set</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; }<o:p></o:p></span></div>
<div class="MsoNormal">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">&nbsp;&nbsp;&nbsp; }</span><span style="font-family: Consolas; font-size: 9.5pt; line-height: 115%;"><o:p></o:p></span></div>
<br />
<div class="separator" style="clear: both; text-align: left;">
Using the following model builder statement
</div>
<div class="separator" style="clear: both; text-align: left;">
<br /></div>
<div class="separator" style="clear: both; text-align: left;">
</div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
</div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">protected</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">override</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">void</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> OnModelCreating(</span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">DbModelBuilder</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> modelBuilder)<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; modelBuilder.Entity&lt;</span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">Entity2</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&gt;().HasRequired(e
=&gt; e.Entity1)<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; .WithMany(e =&gt; e.Entity2s);<o:p></o:p></span></div>
<div class="MsoNormal">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }&nbsp; &nbsp;</span></div>
<div class="MsoNormal">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;"><br /></span></div>
<div class="MsoNormal">
Will create the following relationship</div>
<div class="separator" style="clear: both; text-align: center;">
</div>
<div class="separator" style="clear: both; text-align: center;">
<a href="http://1.bp.blogspot.com/-Bu_ECVx_wE0/UAKQf3IQhCI/AAAAAAAAAPs/_O20SiwxAtA/s1600/Required+Relationship.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="142" src="http://1.bp.blogspot.com/-Bu_ECVx_wE0/UAKQf3IQhCI/AAAAAAAAAPs/_O20SiwxAtA/s320/Required+Relationship.png" width="320" /></a></div>
<br />
<b>Note </b>that in this example we have specified a remote collection for the relationship. This means that you can use the <i>Entity2s </i>property to find all linked entities.</div>
<h4>






<span style="background-color: white;">Many Relationship</span></h4>
If you have the following classes:<br />
<br />
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">class</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">Entity1</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; {<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">int</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> Id { </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">get</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">set</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; }<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">List</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&lt;</span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">Entity2</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&gt; Entity2s { </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">get</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">set</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; }<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; }<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<br /></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">class</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">Entity2</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"><o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp; {<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">int</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> Id { </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">get</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">set</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; }<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">public</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">List</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&lt;</span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">Entity1</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&gt; Entity1s { </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">get</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">set</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">; }<o:p></o:p></span></div>
<div class="MsoNormal">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">&nbsp;&nbsp;&nbsp; }</span><b><span style="font-family: Consolas; font-size: 9.5pt; line-height: 115%;"><o:p></o:p></span></b></div>
<br />
Using the following model builder statement<br />
<br />
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">protected</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">override</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> </span><span style="background-color: white; color: blue; font-family: Consolas; font-size: 9.5pt;">void</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> OnModelCreating(</span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">DbModelBuilder</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;"> modelBuilder)<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; modelBuilder.Entity&lt;</span><span style="background-color: white; color: #2b91af; font-family: Consolas; font-size: 9.5pt;">Entity2</span><span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&gt;().HasMany(e
=&gt; e.Entity1s)<o:p></o:p></span></div>
<div class="MsoNormal" style="margin-bottom: 0.0001pt;">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; .WithMany(e =&gt; e.Entity2s);<o:p></o:p></span></div>
<div class="MsoNormal">
<span style="background-color: white; font-family: Consolas; font-size: 9.5pt; line-height: 115%;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; }</span><b><span style="font-family: Consolas; font-size: 9.5pt; line-height: 115%;"><o:p></o:p></span></b></div>
<br />
Will produce the following relationship<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://3.bp.blogspot.com/-xgSvkQvatvU/UAU9Jk689gI/AAAAAAAAAQA/SyO6w4kOVRI/s1600/ManyRelationship.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="132" src="http://3.bp.blogspot.com/-xgSvkQvatvU/UAU9Jk689gI/AAAAAAAAAQA/SyO6w4kOVRI/s320/ManyRelationship.png" width="320" /></a></div>
With the following database tables<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="http://4.bp.blogspot.com/-fGUlwgElwR4/UAU9I7uqgYI/AAAAAAAAAP4/Cs-fNFadhS0/s1600/ManyDatabaseRelationship.PNG" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="155" src="http://4.bp.blogspot.com/-fGUlwgElwR4/UAU9I7uqgYI/AAAAAAAAAP4/Cs-fNFadhS0/s320/ManyDatabaseRelationship.PNG" width="320" /></a></div>
<div class="separator" style="clear: both; text-align: center;">
<br /></div>
<b>Note </b>that here we have chained two <i>.Many</i> statements to produce a many to many relationship. As you can see the Entity Framework has created a link table in the database but the actual link in the model is created as two collections (without a link table) which makes more sense in c#.<br />
<br />
<span style="font-size: large;">Wrapping up</span><br />
<br />
In this post we have looked in detail at navigation properties, what they are, how they are detected and how they are configured. As with many ORMs Entity Framework provides an abstraction over database Foreign Keys. As with any abstraction its really important to understand its limitations. I hope this post helps you better understand how Navigation Properties work and enables you to make good decisions when dealing with Entity Framework.</div>
