---
layout: page
title: Archives
permalink: /archives/
---

{% for post in site.posts %}
  {% unless post.draft %}
  * {{ post.date | date_to_string }} &raquo; [ {{ post.title }} ]({{ post.url }})
  {% endunless %}  
{% endfor %}