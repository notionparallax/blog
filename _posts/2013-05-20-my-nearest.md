---
layout: post
title: My nearest...
date: 2013-05-20 00:10:37.000000000 +10:00
type: post
published: true
status: publish
categories: []
tags:
- amenity
- D3
- javascript
- leaflet
- maps
- voronoi

---
<p>I've been pretty interested in what you can do with maps recently. There are loads of really nice map tools coming out for<a href="http://www.openstreetmap.org/"> Open Street Maps</a> (<a href="http://leafletjs.com/">leaflet</a>, <a href="http://www.mapbox.com/">mapbox</a>, <a href="http://www.mapbox.com/tilemill/">tilemill</a>, and more), and there will probably be a load more for Google maps since their <a title="cnet reports" href="http://reviews.cnet.com/8301-3513_7-57584722/navigating-the-changes-to-google-maps-at-i-o-2013/">announcements at IO</a>.</p>
<p><a href="http://notionparallax.co.uk/voCell/#15/-33.8746/151.2296"><img class="alignnone  wp-image-1352" alt="cafesV" src="{{ site.baseurl }}/assets/cafesV.png" width="100%" height="321" /></a></p>
<p>As a start at trying to work out the level of amenity for a given spot, I thought I'd take a crack at recreating the work that  <a title="John Snow (physician)" href="http://en.wikipedia.org/wiki/John_Snow_(physician)">John Snow</a>, did on the <a title="wikipedia" href="http://en.wikipedia.org/wiki/1854_Broad_Street_cholera_outbreak">1854 Broad Street cholera outbreak</a>. (Sort of.)</p>
<p>It's a bit more of my adventures in web development - so it's an adaptation of <a href="https://twitter.com/CWMma">Calvin Metcalf</a>'s <a href="https://github.com/calvinmetcalf/psychic-octo-nemesis">psychic-octo-nemesis</a> template. It uses <a title="AMAZING interactive toys" href="http://d3js.org/">D3</a> to do the Voronoi and <a title="really easy maps" href="http://leafletjs.com/">Leaflet</a> to display the map. It gets its data from Open street maps' <a href="http://overpass-turbo.eu/">Overpass</a> system.</p>
<h1 style="text-align: center;"><a href="http://notionparallax.co.uk/voCell/#15/-33.8746/151.2296">The closest...</a></h1>
<p>There are lots of problems to take into account when thinking about this as a measure of amenity, not least that we don't travel like birds, but need to use paths and roads, so the cells aren't especially realistic. However, I like to think about models as a tool to help understanding - if the model disagrees with your internal model then one of you needs to adjust.</p>
