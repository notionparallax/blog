---
layout: post
title: Trying to capture a 'Save to Pocket' event
date: 2016-05-20 10:08:27   PDT
type: post
published: true
status: publish
categories: []
tags: []

#this goes on the index page, and into facebook shares
description: How to fire a GA event when someone saves your page to Pocket (in Chrome).

# This is what twitter will pick up if someone tweets the link to this page 
# 110 marker 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
twitter-body: Here's how I fire a GA event when someone saves my page to Pocket (in Chrome).
#Twitter and facebook will pick up this image. you can also use it in a post with:
# ![alt text]({{ site.baseurl }}/assets/{{page.featuredimg}}) 
featuredimg: 16/pocket.jpg
---

I wanted to be able to track how many people save articles to Pocket from this site. I thought that given how much [I use](http://notionparallax.co.uk/2014/offline-reading) [Pocket](https://getpocket.com/@ben.doherty), other people who read my stuff might do the same.

I contacted Pocket support and they said that their browser extensions don't emit an event when it's clicked[^1]. I was hoping to be able to drive a Google analytics goal when that happened.

Pocket suggests that I look at their [Publisher stats][2], which is nice, but it's two sources of information. I wanted to be able to do it all in Google Analytics.

I hacked the following together from the [MDN MutationObserver][1] docs, but it relies on Pocket not changing the classname of their UI. (And leaving it in the DOM, not as a separate overlay.) I left it [on Stack Overflow](http://stackoverflow.com/questions/37036606/can-a-save-to-pocket-be-detected) for a week to see if anyone was going to call me out for being a chump. They didn't; I guess the internet had better things to do this week.


~~~ js
document.addEventListener('DOMContentLoaded', function() {
  //your other events events...
  //ga('send', 'event', [eventCategory], [eventAction], [eventLabel], [eventValue], [fieldsObject]);

  function registerPocketSave() {
    console.log("looking for Pocket saves");
    // This is for Chrome only :(
    var target = document.querySelector('body');

    // create an observer instance
    var observer = new MutationObserver(function(mutations) {
      mutations.forEach(function(mutation) {
        //console.log(mutation);
        let a = document.getElementById('pkt_ext_master');
        if (a) {
          console.log(a, "found a Pocket save - firing a GA event!");
          ga('send', 'event', 'Pocketed', document.title);
          observer.disconnect(); //once we've saved to Pocket, stop so that we don't get ghost versions
        }
      });
    });

    // configuration of the observer:
    var config = { attributes: true, childList: true, characterData: true };

    // pass in the target node, as well as the observer options
    observer.observe(target, config);
  }
  registerPocketSave();
});
~~~

It's actually running on this page right now, and it sort of works. It's only for Chrome. The Chrome extension mofifies the DOM and injects a popup, but the Firefox extension uses the new DOM provided by the extension's own little window.

If anyone has any suggestions then I'd love to hear about it!

  [1]: https://developer.mozilla.org/en/docs/Web/API/MutationObserver
  [2]: http://getpocket.com/publisher/

  [^1]: Actually I only asked about their Chrome extension, but I'm guessing that's common to Firefox too. Pocket support were actually really helpful about this.

