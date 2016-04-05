---
layout: post
title: Moar power?
date: 2013-06-05 13:14:40.000000000 +10:00
type: post
published: true
status: publish
categories: []
tags:
- crossfit
- D3
- graph
- gym
- javascript
- JSfiddle
- power
- programming
- regression
description:
meta:
dsq_thread_id: '4503553294'

---
<p>If I really smash it I can hit 0.18 <a href="http://en.wikipedia.org/wiki/Horsepower">horsepower</a>!</p>
<p><a href="http://jsfiddle.net/mnUWA/35/"><img class="alignnone  wp-image-1403" title="click the image to go to the real thing" alt="A scatter plot of workout power outputs" src="{{ site.baseurl }}/assets/powerGraph.png" width="100%" /></a></p>
<p>I've been meaning to try using d3 a bit more proper like after I skimmed it for <a title="My nearest…" href="http://notionparallax.co.uk/?p=1348">_my nearest_</a> a few weeks ago. I've got the <a href="http://shop.oreilly.com/product/0636920026938.do">Interactive Data Visualization</a> for the Web book by Scott Murray, and I read it as prose, then jumped straight into the middle of it and tried the code examples and I really should have worked through it methodically. (Maybe feeling stupid will give me some motivation now!)</p>
<p> </p>
<p><a title="This will take you to a fiddle" href="http://jsfiddle.net/mnUWA/35/">This graph</a> displays my workouts since I started tracking them using Beyond the whiteboard 6 months ago</p>
<ul>
<li>The x axis is length of workout, i.e. how long it took me to complete it.</li>
<li>The y Axis is the wattage as calculated by BTW</li>
<li>The blue line shows the line of best fit between the filtered workouts</li>
</ul>
<p>To use it, just set the slider to the time window that you are interested in.</p>
<p>There is still a lot to do in terms of interactivity.</p>
<ul>
<li>Names shown on roll over - not all the time</li>
<li>a slider to control the date window</li>
<li>maybe a way of showing a number of best fit lines for different time windows to see if there is improvement.</li>
<li>I'd like to also try changing it to a curve of best fit eventually.</li>
</ul>
<p>The data is scraped from their website, so isn't live (snapshot taken on 2013-06-05).</p>
<h2>The why story</h2>
<p>Recently I've been having a bit of a cry at the gym, I feel a bit like I'm slipping backwards in terms of work capacity.</p>
<p>Being a big <a href="http://quantifiedself.com/">QS</a> nerd I've been tracking my performance since I started[^1] with <a href="http://beyondthewhiteboard.com">beyond the whiteboard</a> so I have the historical data on how I've been performing.</p>
<p>Looking at the results I can see that what's really happening is that I'm progressing, but not as fast as the people around me. A bit like being on a train that's being overtaken by another one; you feel like you are going backwards, but really you are going forwards! It's a pretty simple three step process for improving more though:</p>
<ol>
<li><span style="line-height: 13px;">fix my diet</span></li>
<li>harden up and rest less between bits of doing</li>
<li>profit</li>
</ol>
<hr style="background: #EEEEEE; border: 0; height: 7px;" />

[^1]: apart for a bit of a lapse a couple of weeks ago :(