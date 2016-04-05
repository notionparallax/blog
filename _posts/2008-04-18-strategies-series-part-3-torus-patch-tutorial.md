---
layout: post
title: strategies series part 3 - torus patch tutorial
date: 2008-04-18 17:18:25.000000000 +10:00
type: post
published: true
status: publish
categories: []
tags:
- architecture
- GC

---
<p><img src="{{ site.baseurl }}/assets/1332745021_3424604d16_m.jpg" align="left" /> If you rotate a circle around a centre point outside the circle, then you get a torus, or ring doughnut.The circle to circle gaps can be tiled with planar panels This method is less versatile than the sheared cones method, but it has the advanage that all the panels are identical. so if we know that all the panels on a the surface of a torus are planar, then if we only want a certain area to be tiled, then we can take a section of those panels, and that is the ‘patch’ that is referred to.</p>
<p> </p>
<p><img src="{{ site.baseurl }}/assets/2422608747_f0ce2c1e16_o.jpg" align="left" /></p>
<p><img src="{{ site.baseurl }}/assets/2423423480_4c151712a9_o.jpg" /></p>
<p><img src="{{ site.baseurl }}/assets/2423423510_41bdfa5e7e_o.jpg" /></p>
<p><img src="{{ site.baseurl }}/assets/2422706549_c3866cf2d7.jpg" /></p>
<p>If we reduce the above image to a series of pairs of arcs, as long as they are the same radius, they can tiled with planar panels as the pairs will always have an arc between them, no matter how weird they mgiht look!</p>
<p>This means that as long as the radius stays constant, the path can do what it likes and the panels will remain planar.</p>
<p>There is, as aways, a pdf and a supporting GCT in the GCuser gallery</p>
