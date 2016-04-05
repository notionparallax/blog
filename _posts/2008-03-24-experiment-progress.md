---
layout: post
title: experiment progress
date: 2008-03-24 15:33:00.000000000 +11:00
type: post
published: true
status: publish
categories: []
tags:
- geek

---
<p><img src="{{ site.baseurl }}/assets/69175.png" align="right" width="100" />After much faffing about, I've bought a webcam to do my mapping with.</p>
<p>There seem to be a couple of  little processing sketches that do almost what I want, so the first step (finding the blobs that are people) should just be a case of wiring them together.</p>
<p><img src="{{ site.baseurl }}/assets/first%20tries%20at%20blob%20detection__0000_Layer%202.jpg" height="333" width="500" /></p>
<p> </p>
<p>The first problem is that the blob detection software finds all the blobs, even if they don't move. There is an example where it takes an source image and then compares the current frame with it. If the pixels match, then they get painted in in black. that solves the problem of static blobs.</p>
<p><img src="{{ site.baseurl }}/assets/first%20tries%20at%20blob%20detection1__0003_Layer%201.jpg" width="500" /></p>
<p>The resulting image is still a bit dark, but you can push the contrast pretty hard because you know that there are going no problems with things n the background popping up.</p>
<p>This version is pretty cool, it's packaged with processing, but it's an ascii video!</p>
<p><img src="{{ site.baseurl }}/assets/first%20tries%20at%20blob%20detection1__0001_Layer%203.jpg" width="500" /></p>
<p>So once there  are white blobs moving over a black screen then we are in a position to do some serious stuff with the blob detection.</p>
<p>This is were I'm a bit out on a limb now because I need to really look into how the blobs are stored, because from frame to frame they are totally recalculated, so how do I tell which is which? Once I can track them across frames, then I can start doing things like timing them from one side to the next and drawing lines.</p>
<p>The  actual mechanics of the programs are a bit of a mystery to me. They are doing a lot of bitwise operations on the image's pixels, and I have only a vague idea what a bitwise  operation is, let alone how it applies to graphics programming!</p>
<p><img src="{{ site.baseurl }}/assets/150px-Rotate_right_arithmetically.svg.png" align="left" height="120" width="150" />Argh,  I'm too damn inquisitive, I think my brain might explode if I have to do too much binary stuff.</p>
<p>but in traditional procrastination style, here is my best guess at what's going on</p>
<p><embed src="Images/Antipodes/bitwise-explanation.swf" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/shockwave/download/" height="800" width="500"></embed></p>
