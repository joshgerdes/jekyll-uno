---
title:  "Adding a custom verb to all web parts in SharePoint"
date:   2010-08-16
redirect_from:
  - 2010/8/16/adding_a_custom_verb_to_all_web_parts_in_sharepoint
  - 2010/08/adding-custom-verb-to-all-web-parts-in.html
---
So I was trying to add a menu item to all web parts in a SharePoint 2007 site collection. Surely such a thing should be simple to achieve. I expected it to be implemented in a similar way to adding to the ECB drop downs in a document library or something like the site actions menu. However menu items on web parts are implemented by the base ASP.Net web part framework using a concept called verbs.

The verbs for a web part are stored on the `System.Web.UI.WebControls.WebParts.WebPart` class in a read only property. From my research an posts on the MSFT developer forums there's no good way to break into this collection. So basically I was left with a problem, how do I get my own menu item into this list. I thought of two basic ways to do this, firstly use reflection to write to the property or secondly use JavaScript to add the menu item to the page on the fly.

It turns out that the Verbs property on WebPart simply returns an empty collection. This makes it difficult, so it was down to the JavaScript option. It turns out that the default menu options on a web part aren't returned from the verbs property. Instead there are other properties control the visibility of these default items. The defaults are written to the bottom of the page in a hidden section and conditionally rendered into the dropdown.

This can be done with JQuery and a couple of web services. I created a delegate control containing my script and injected it into the page head. Running the line below on page load will inject a custom menu item into all WebPart dropdowns on the page.

``` javascript
$('#MSOMenu_WebPartMenu').append('<ie:menuitem hello="" id="Menu_MyMenuItem" onclick="javascript:alert(" type="option" world");"=""> Hello World</ie:menuitem>');
```

There are however a few limitations to this, Firstly it only works in IE, other browsers render verbs in a completely different way (no dropdown even), and secondly it will only work with javascript enabled.

If anyone has any other approaches to this problem I would love to hear about them
