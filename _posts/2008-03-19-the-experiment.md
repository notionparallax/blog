---
layout: post
title: the experiment
date: 2008-03-19 06:45:31.000000000 +11:00
type: post
published: true
status: publish
categories: []
tags:
- architecture
- geek
- hardware

---
<p>In order to make any sort of meaningful map or information visualisation, I think you need a _lot_ of data, especially when it is related to the unpredictable nature of humans.</p>
<p>Manually capturing that much information is for people with more time and patience than me.</p>
<p>I'd like to start out by pointing out two things. I have no idea where this will lead to, and that there is an ulterior educational motive at work - I don't know how to do any of this so I thought I'd get down to it and learn.</p>
<p>I'd like to measure how long it takes for people in a fairly uninteresting area of street to pass from one side of the cameras frame to the other, and then make subtle changes to the environment to see if this affected their behavior.</p>
<p><img src="{{ site.baseurl }}/assets/lookDownTrackPrototype.gif" height="333" width="500" /></p>
<p>Changes like lines marking territory,  the addition of mirrors, blasts of hot air etc. might or might not affect the behavior of the people passing. </p>
<p><img src="{{ site.baseurl }}/assets/detect.gif" alt="http://www.cs.cmu.edu/~vsam/FREcached/vismod.www.media.mit.edu/darpa-vsam/darpa-images/detect.gif" /></p>
<p>In order to capture the data I'm going to have a go at making a piece of person tracking software using blob detection, and then hopefully I'll be able to mine that information and extract vector paths and times.</p>
<p><img src="{{ site.baseurl }}/assets/Shadow-Monsters-330.jpg" title="http://www.designmuseum.org/media/item/61417/71/Shadow-Monsters-330.jpg" alt="http://www.designmuseum.org/media/item/61417/71/Shadow-Monsters-330.jpg" width="240" /><img src="{{ site.baseurl }}/assets/data_item_1_img.jpg" border="0" width="240" /></p>
<p>the <a href="http://www.v3ga.net/processing/BlobDetection/" target="_blank">v3ga.net Blob Detection library</a> has been used for projects like <a href="http://www.worthersoriginal.com/viki/">shadow monsters</a> (above) and a <a href="http://www.v3ga.net/processing/BlobDetection/index-page-projects.html">few other</a> projects</p>
<p><img src="{{ site.baseurl }}/assets/vector_outline.jpg" height="288" width="335" /></p>
<p>the <a href="http://webcamxtra.sourceforge.net/reference.shtml">myron webcaXtra library</a> is a possible alternative, but i haven't researched the relative merits of the two options</p>
<p><img src="{{ site.baseurl }}/assets/blob-recognition.jpg" width="500" /><img src="{{ site.baseurl }}/assets/webcamxtra_cactus.jpg" width="500" /></p>
<p>Jason Bruge and  <a href="http://www.redremote.co.uk/whitewing/switchedon.html.">White Wing Logic</a> used bluetooth rather than image based methods to track people over London bridge and display the results on tower bridge. The possibilities of <a href="http://en.wikipedia.org/wiki/Bluetooth">bluetooth</a> are great, they allow tracking of specific people even if they go out of sight, but the technology is much more expensive and complicated.</p>
<p><img src="{{ site.baseurl }}/assets/switch4.jpg" title="wpeA4.jpg (195290 bytes)" alt="wpeA4.jpg (195290 bytes)" width="500" /></p>
