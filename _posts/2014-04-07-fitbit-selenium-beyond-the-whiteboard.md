---
layout: post
title: Fitbit → Selenium → Beyond the Whiteboard
date: 2014-04-07 01:16:45.000000000 +10:00
type: post
published: true
status: publish
categories: []
tags: []
description:
meta:
  _wpas_mess: Fitbit → Selenium → Beyond the Whiteboard
  dsq_thread_id: '4503553438'

---
<p><a href="https://www.fitbit.com/au/aria?gclid=CM7Pr-2Vzb0CFYWXvQodJqAAYw"><img class="alignright" alt="" src="{{ site.baseurl }}/assets/simple.b-dis-png.h90165c3211e4edcba5f3ffc6f98427ad.pack?items=%2Fcontent%2Fassets%2Fonezip%2Fimages%2Fproducts%2Faria%2Fwhite_top.png" width="190" height="165" /></a>I use <a href="http://beyondthewhiteboard.com/">Beyond the Whiteboard</a> to track my workouts, it's really good, but for some reason they don't publish an API. I also have a <a href="https://www.fitbit.com/au/aria">Fitbit Aria</a> that records my considerable attraction to this nice planet of ours. Fitbit _do_ have an API, but in a short bit of faffing about I couldn't get it to work[1. I was using <a href="http://Temboo.com">Temboo</a> which seems like a pretty cool thing], but they also have a csv download[1. as a one off thing, if you want to do it again you need to pay them $60 a year - arseholes.].</p>
<p>We're just moving to using <a href="http://en.wikipedia.org/wiki/Selenium_(software)">Selenium</a> based functional tests at work, so I figured that a good way to clear my hangover was to learn a little bit of Selenium.</p>
<p>So I have a place that I can store my weight and body composition along with my workouts (but no automatic way to do this (BTW)), a way of automatically recording my weight and body composition (Fitbit), and a way to join them up (Selenium).</p>
<p><script src="https://gist.github.com/notionparallax/10013450.js"></script></p>
<p>I'm pretty sure that this is a bad way to do this, but it works and will give me something to build on as I learn how to do it better.</p>


[^1]: I was using <a href="http://Temboo.com">Temboo</a> which seems like a pretty cool thing

[^2]: as a one off thing, if you want to do it again you need to pay them $60 a year - arseholes.

