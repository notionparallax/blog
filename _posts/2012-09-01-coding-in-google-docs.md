---
layout: post
title: coding in Google docs
date: 2012-09-01 06:39:06.000000000 +10:00
type: post
published: true
status: publish
categories: []
tags:
- data
- google
- programming
description:
meta:
  _wp_old_slug: '948'

---
<p>I'm doing a bit of data exploration for work based on our people. I don't know any statistical software (or really any stats![^1]), so rather than learning R or SPSS I thought I'd have a go at doing it in Google docs. I will probably need a stats library once we get into trying to find unexpected numbers, but for simple queries it does just fine. This stage is just about making some interesting graphs to give people an idea of what they can do with the data they have at their disposal.</p>
<p>Javascript now does array comprehensions, so you can chain Boolean expressions to filter for just the rows that you want.</p>
<p><code>var maleGlassesWearers = [p for each (p in people) if ((p.gender == 'm') &amp;&amp; (p.glassesInRealLife == 'y'))];</code></p>
<p>They aren't the prettiest of statements, but they get the job done in very little code.</p>
<p>Dan's been on at me to get my head around more functional language concepts, so this is probably a good place to start.<br />
The spreadsheet is confidential, but there is noting special about the code, so it's included here. I've done the filters using a for loop and using a comprehension so that you can see the difference.<br />
 <br />
<script src="https://gist.github.com/3564342.js"> </script></p>

[^1]: But I am going to do the <a href="https://www.coursera.org/course/stats1">coursera statistics course</a> starting next week.