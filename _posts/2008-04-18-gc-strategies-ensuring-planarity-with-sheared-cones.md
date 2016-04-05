---
layout: post
title: gc strategies - ensuring planarity with sheared cones
date: 2008-04-18 03:28:13.000000000 +10:00
type: post
published: true
status: publish
categories: []
tags:
- architecture
- GC

---
<p><span id="spBody" class="Forum_Normal">here's another strategies tutorial, there is a pdf and gct that's more beautifully formatted over at <a href="http://www.gcuser.com">GCuser.com</a> in the gallery.</span></p>
<p>This is about making flat quad panels using sheared cones.</p>
<p>For those of us in Melbourne, there is a particularly horrific example of this in Melbourne central. if you look carefully, you can see the module size split halfway up when the panels get too small.</p>
<p><img src="{{ site.baseurl }}/assets/glass_08.jpg" height="200" /><img src="{{ site.baseurl }}/assets/Melb-Central-shot-tower.jpg" height="200" /></p>
<p> </p>
<p>The default solution to panelling anything is to do it in triangles. Any surface can be tiled in triangles. Any three points in space define a triangle, and also a plane.<br />
Quadrilateral panels are a bit trickier as there are only a certain number of ways of making a surface be predictably tillable using four sided shapes.<br />
The way outlined here is the sheared cones method.</p>
<table border="1" cellpadding="1" cellspacing="1" width="500">
<tr>
<td><img src="{{ site.baseurl }}/assets/2420404797_3e96673fa6_o.jpg" /></td>
<td>Given that all triangles are planar, and<br />
subdivision of that triangle is guaranteed to be<br />
planar too.<br />
If the base of a cone is chopped so that it has flat<br />
sides then the sides of the cone become<br />
triangles.</td>
</tr>
<tr>
<td><img src="{{ site.baseurl }}/assets/2421217822_a5dbba7b72_o.jpg" /></td>
<td>If we then slice the top off the cone, parallel to<br />
the base, then the remaining sections of panel<br />
are still going to be flat.</td>
</tr>
<tr>
<td><img src="{{ site.baseurl }}/assets/2420404873_2dec83c4c8_o.jpg" /></td>
<td>As counter intuitive as it initially feels, if we move<br />
the top point of the cone around then the panels<br />
remain flat as the triangles are still intact. So<br />
basically, shearing the cone has no effect on the<br />
planarity, hence the name “sheared cone”<br />
method.</td>
</tr>
<tr>
<td><img src="{{ site.baseurl }}/assets/2420404905_b39a1c4ed2_o.jpg" /></td>
<td>So if we bump up the number of sides on the<br />
cone, we begin to see that we are beginning to<br />
get a more realistic panellisation of the circle.</td>
</tr>
<tr>
<td><img src="{{ site.baseurl }}/assets/2421217904_675bf76aa1_o.jpg" /></td>
<td>The top set of points can then become the<br />
bottom set of points for a new set of panels, and<br />
so on.</td>
</tr>
<tr>
<td><img src="{{ site.baseurl }}/assets/2421217918_6a1c737046_o.jpg" /></td>
<td>So in summary, if two circles are parallel, and<br />
they have the same number of points, equally<br />
spaced on their circumference, then the panels<br />
between them will be planar, regardless of the<br />
shear or scale of the circles with respect to each<br />
other.</td>
</tr>
</table>
<p><a href="http://creativecommons.org/licenses/by-sa/2.0/uk/" rel="license"><img src="{{ site.baseurl }}/assets/88x31.png" style="border-width: 0pt" alt="Creative Commons License" /></a><br />
<span rel="dc:type" property="dc:title" xmlns:dc="http://purl.org/dc/elements/1.1/">Sheared cones tutorial</span> by <a href="http://gcuser.com/Forum/tabid/151/forumid/-1/threadid/2312/scope/posts/language/en-US/www.notionparallax.co.uk" rel="cc:attributionURL" property="cc:attributionName" xmlns:cc="http://creativecommons.org/ns#">Ben Doherty</a> is licensed under a <a href="http://creativecommons.org/licenses/by-sa/2.0/uk/" rel="license">Creative Commons Attribution-Share Alike 2.0 UK: England &amp; Wales License</a>.</p>
