---
layout: post
title: 'Centroid of points on the surface of a sphere: redux'
date: 2016-01-07 08:15:35.000000000 +11:00
type: post
published: true
status: publish
categories: []
tags: []
meta:
  _wpas_done_all: '1'
  _edit_last: '1'
  _publicize_facebook_user: http://www.facebook.com/541400612
  _publicize_twitter_user: "@notionparallax"
  _SnS: "a:1:{s:6:\"styles\";a:1:{s:6:\"styles\";s:210:\"iframe.world{\n\twidth:100%;
    \n\theight:50vh;}\n#tinymce{width:640px;}\n#tinymce p {\n    font-size: 14px;\n\tline-height:20px;\n}\nh1,
    h2,h3{clear:both;}\n.scruffy{width:65%;}\n.alignright {\n    float: right;\n}\";}}"
  _oembed_043cf2d6f7aa22d3aee36b5f02e551f4: "{{unknown}}"
  _syntaxhighlighter_encoded: '1'
  _oembed_2ec26a54ab7efd8eeab76ba812be423f: "{{unknown}}"
  _oembed_a984aa303398d961623afafcbc96acc4: "{{unknown}}"
  _wpas_mess: 'How to find the centroid of points on the surface of a sphere: redux'
  _wpas_skip_3597554: '1'
  _wpas_skip_3295701: '1'
  _wpas_skip_3597579: '1'
  _wpas_skip_6785826: '1'
author:
  login: Ben
  email: ben@notionparallax.co.uk
  display_name: Ben
  first_name: Ben
  last_name: Doherty
---
<p>Imagine you are an international sort of person. All your friends are international sorts too. Where should you all fly your private helicopters to for a party?<!--more--></p>
<p><iframe class="world" src="http://notionparallax.github.io/whereToMeet/sphere.html" width="300" height="150"></iframe></p>
<p>This problem comes up whenever someone is planning a conference or a wedding or anything that needs global travel.</p>
<p>It's a bit of a toy problem because it doesn't take into account transport methods. It's a lot easier for me to meet a South African and an Argentinian in Dubai than it is to meet in Antarctica, even though that <a href="http://www.geomidpoint.com/?ml=-80.95903&amp;mn=25.19528&amp;l=-33.867487|-33.924868|-54.93521&amp;n=151.20699|18.424055|-67.605854&amp;a=Sydney+NSW,+Australia|Cape+Town,+South+Africa|Puerto+Williams,+Cabo+de+Hornos,+Regi%C3%B3n+de+Magallanes+y+de+la+Ant%C3%A1rtica+Chilena,+Chile&amp;cl=-66.79489&amp;cn=41.80057&amp;z=1&amp;x=0&amp;c=0&amp;p=1&amp;r=0&amp;w=0">minimises travel distance</a>. Ignoring the realities of planes, how <em>do</em> you work it out?</p>
<p>Back in 2009 I published a post called <a href="http://notionparallax.co.uk/wordpress/?p=130">centroid of points on the surface of a sphere</a>. Then in 2012 I did another one where I looked at <a href="http://post popularity">which posts get visited the most</a>. Turns out that something like 6 times as many people want to look at that post than the next most popular one. This problem consumed me for ages in 2009! I dismissed the most obvious solution (vectors) because I spotted a degenerate solution. What if the points were evenly spaced? <a href="http://users.cs.cf.ac.uk/O.F.Rana/Antonia.J.Jones/">Antonia J. Jones</a>[1. Sadly, <a href="http://www.legacy.com/obituaries/staugustine/obituary.aspx?n=antonia-j-jones&amp;pid=150288587">here's her obituary</a>.] pointed out that this was a problem in all situations, not a solution specific one.</p>
<h1>General solution</h1>
<p>It's the vectors stupid. If you assume that the world is spherical[1. It's <a href="https://en.wikipedia.org/wiki/Figure_of_the_Earth">not spherical</a>, it's an <a class="mw-redirect" title="Oblate spheroid" href="https://en.wikipedia.org/wiki/Oblate_spheroid">oblate spheroid</a>, but let's not let that get in the way. I'm sure if you were even moderately good at maths that you could correct for that. (I'm not.)] then 2 points on the  surface make a pie segment shape, <a href="https://en.wikipedia.org/wiki/Circular_sector">a sector ⌔</a>. The midpoint of the curved bit of the sector is the midpoint between those two points. You can either do that by measuring the arc, or by bisecting the angle.</p>
<p>The angle bisection is really just the average of the two vectors. The neat thing is that you don't need to do anything magic when you get 3 points, or 100 points. Vector averages will still give you the right answer.</p>
<p>Some js that I wrote to do the job (which I thought about for almost exactly no seconds) looks like this:</p>
<p>[code language="javascript"]<br />
function meanVector(people) {<br />
    let xTotal = 0;<br />
    let yTotal = 0;<br />
    let zTotal = 0;<br />
    let n = people.length<br />
    for (let p of people) {<br />
        xTotal += p.vector.x;<br />
        yTotal += p.vector.y;<br />
        zTotal += p.vector.z;<br />
    }<br />
    return new THREE.Vector3(xTotal / n,<br />
        yTotal / n,<br />
        zTotal / n);<br />
}<br />
[/code]</p>
<h2>Degenerate cases</h2>
<h3>Opposites</h3>
<p><a href="https://en.wikipedia.org/wiki/Antipodal_point"><img class="alignright" src="{{ site.baseurl }}/assets/Digon_on_circle.png" alt="" width="240" /></a>If you have two points that are exactly opposite each other then there is no answer. The two vectors resolve to <a href="https://en.wikipedia.org/wiki/Journey_to_the_Center_of_the_Earth">the centre of the earth</a>!</p>
<h3>Equal spacing</h3>
<p><a href="http://stackoverflow.com/questions/9600801/evenly-distributing-n-points-on-a-sphere"><img class="alignright" src="{{ site.baseurl }}/assets/NsCif.png" alt="" width="240" /></a>The points don't need to be opposite. If the points are evenly spaced on the sphere then it'll fail too. This could be even spacing along a great circle, eg at exactly a quarter apart. In fact, direct opposites is a subset of this when they are exactly 1/2 apart.</p>
<p>It could also be some kind of magnetic repulsions spacing over the whole surface. They are an equal distance from each other, but in 3 dimensions. (See <a href="http://stackoverflow.com/questions/9600801/evenly-distributing-n-points-on-a-sphere">here</a> and <a href="http://web.archive.org/web/20120421191837/http://www.cgafaq.info/wiki/Evenly_distributed_points_on_sphere">here</a>)</p>
<h1>Three.js implementation</h1>
<p>Go on, click the world and drag it about!</p>
<p><iframe class="world" src="http://notionparallax.github.io/whereToMeet/sphere.html" width="300" height="150"></iframe></p>
<p>While I'm a free agent[1. where free agent == willingly unemployed.] I don't have access to any of the tools that I'm accustomed to having (Grasshopper etc.) so I thought I'd have a crack at doing it in something more universally accessible. <a href="http://threejs.org/">Three.js</a> lets you do 3d geometry stuff in your browser[1. There is some slightly strange stuff to get it going, but I found it surprisingly easy to pick up. The model above took me about 3 hours with no prior experience.<a href="http://twitter.com/andraconnect">Alexandra Etienne</a> and <a href="http://twitter.com/jerome_etienne">Jerome Etienne</a> have a super cool tutorial on <a href="http://learningthreejs.com/blog/2013/09/16/how-to-make-the-earth-in-webgl/">how to make a planet</a> which helped a lot.].</p>
<p>It shows 12 people, randomly spaced all over the globe. The orange spike (which you might need to hunt for a bit) shows the centroid of those points. If the iframe is annoying, you can <a href="http://notionparallax.github.io/whereToMeet/sphere.html">see it full screen here</a>.</p>
<p>I might add a bit more UI to it soon to pick cities etc. so that you can use it to pick the positions of your own friends. In the meantime, <a href="http://www.geomidpoint.com/">this does almost exactly that</a>!</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
