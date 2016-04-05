---
layout: post
title: Lean at the gym (the other lean)
date: 2013-05-23 08:30:13.000000000 +10:00
type: post
published: true
status: publish
categories: []
tags:
- android
- crossfit
- FOSS
- geek
- graph
- hardware
- nexus
- Olympic weightlifting
- phone
- sensors
description:
meta:
  _thumbnail_id: '1380'

---
<p><script type="text/javascript" src="//ajax.googleapis.com/ajax/static/modules/gviz/1.0/chart.js"><br />
{"dataSourceUrl":"//docs.google.com/a/notionparallax.co.uk/spreadsheet/tq?key=0AgIWT_wqd-VmdGxnamtuUG8yZEo3UzViel8xV1o0b2c&transpose=0&headers=0&range=A191%3AD358&gid=0&pub=1",<br />
"options":{"vAxes":[{"useFormatFromData":true,"title":null,"minValue":null,"viewWindow":{"min":null,"max":null},"maxValue":null},{"useFormatFromData":true,"minValue":null,"viewWindow":{"min":null,"max":null},"maxValue":null}],"titleTextStyle":{"bold":true,"color":"#000","fontSize":16},"booleanRole":"certainty","curveType":"","title":"","animation":{"duration":0},"legend":"none","lineWidth":2,"useFirstColumnAsDomain":true,<br />
"hAxis":{"useFormatFromData":false,"minorGridlines":{"count":"2","color":"#cccccc"},<br />
"formatOptions":{"source":"inline"},"minValue":null,"format":"0.##","gridlines":{"count":"5","color":"#b7b7b7"},"logScale":false,"viewWindow":{"min":null,"max":null},"maxValue":null},"width":620,"height":400},"state":{},"view":{},"isDefaultVisualization":true,"chartType":"LineChart","chartName":"Chart1"}<br />
</script></p>
<p>One of my major faults is my inability to finish off ideas, they usually get as far as spending the money to get them going, and then I just leave the kit lying around gathering dust and making my bank account empty. I've been <a href="http://shop.oreilly.com/category/series/lean.do" title="THE LEAN SERIES">reading a bit</a> about doing things in a lean way and it seems to be rubbing off on me.</p>
<p>One of my recent ideas is that there must be a quantifiable way of recording how my Olympic lifting is progressing other than just the amount of weight I'm able to move. Often my lifts are pretty messy and it'd be good to try and break it down in a way that I can tell _how_ I'm doing it.<br />
As usual I'd solved the problem and patted myself on the back for being a genius, a paragon of originality, but of course someone had already solved the problem years ago (<a href="http://www.setantacollege.com/wp-content/uploads/Journal_db/VALIDATION%20OF%20AN%20ACCELEROMETER%20FOR%20MEASURING%20SPORT%20PERFORMANCE.pdf" title="VALIDATION OF AN ACCELEROMETER FOR MEASURING SPORT PERFORMANCE - KIMITAKE SATO, SARAH L. SMITH, WILLIAM A. SANDS ">pdf</a>).</p>
<p>I'd had a little look around at <a href="http://littlebirdelectronics.com/collections/sensors-accelerometers">various accelerometers</a> but I didn't really know what I was doing there (being a bit of a hardware-phobic). Then I remembered that I could do it all with my phone! </p>
<p>Over at <a href="http://www.brokenairplane.com/2012/08/physics-gizmo-is-open-source.html">broken airplane</a> <a href="https://plus.google.com/110891307255905847602/posts" title="Phil Wagner's Google+ page">Phil Wagner</a> has an app called <a href="https://play.google.com/store/apps/details?id=com.brokenairplane.physicsGizmo" title="Android play store - free!">Physics Gizmo</a> that. amongst other things, has a really nice accelerometer recorder.</p>
<p>So, in the spirit of leanness and learning fast, I turned it on, wrapped my phone in a towel and taped it to a bar!</p>
<p>The raw results at the top, there is a bit more analysis below.<br />
 <br />
<a href="http://notionparallax.co.uk/wordpress/wp-content/uploads/2013/05/accelerometerTest.png"><img src="{{ site.baseurl }}/assets/accelerometerTest-1024x486.png" alt="Here&#039;s my take on what&#039;s going on in this. Click to make it bigger." class="alignnone size-large wp-image-1380" /></a></p>
<p>If I'd been thinking I would have got a film to go with this (like they did in <a href="http://www.setantacollege.com/wp-content/uploads/Journal_db/VALIDATION%20OF%20AN%20ACCELEROMETER%20FOR%20MEASURING%20SPORT%20PERFORMANCE.pdf">the paper</a>) so that I didn't need to guess what the graph means. </p>
<p>In the rest of the 'things I've learned' list: </p>
<ul>
<li>The accelerometer hits 19.5N a few times, so it makes me think that it tops out at about 2g, so it might need a beefier one. </li>
<li>There was a lot of enthusiasm about it, so maybe it'd be good to do some more investigation (Physics gizmo is FOSS so it'd be easy to modify it to track a whole workout)</li>
</ul>
