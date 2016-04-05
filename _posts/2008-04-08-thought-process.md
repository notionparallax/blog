---
layout: post
title: thought process
date: 2008-04-08 15:56:12.000000000 +10:00
type: post
published: true
status: publish
categories: []
tags:
- architecture
- GC
- geek
- rmit
description:
meta:
dsq_thread_id: '4503551690'

---
<p>I've been breaking all my own rules, I've just been jumping into trying to write this program without really thinking about how it'll all go together.This'll hopefully make it clear.</p>
<p>The first thing is that the frames that the camera produces are too noisy, there are too many static blobs. Things like a puddle, a bollard, etc. will all show up as blobs and be tracked. There is a fairly simple (conceptually) way to deal with it. if you compare each frame to it's previous one, then it'll only show up the difference between the two (in photoshop it is called the _difference_ blending mode). This is actually what I go so wrapped up in bit shifting for a couple of posts ago, but as it was late at night, I actually forgot to find out what it did, I was just interested in the bit I didn't understand. Typical me. </p>
<p><embed src="Images/Antipodes/frame-comparison.swf" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/shockwave/download/" height="800" width="500"></embed><br />
So now that I know what it actually _does_ I can start to use it.Tracking people movement is a fairly low res thing, people don't move very fast, so if my frame is 5 meters across, and people walk at roughly 6kph, that's about 1.7 meters per second, so they'll take 8.5 seconds to cross the frame. That means that they'll even at 10 frames per second (fps) they'll get tracked 85 times. That's more than enough, so when I get down to it I might actually try reducing the frame rate to save on data.<br />
<img src="{{ site.baseurl }}/assets/trackign-cycles.png" alt="tracking cycle" align="middle" width="500" /><br />
This test data was made using <a href="http://en.wikipedia.org/wiki/OpenOffice.org_Calc" target="_blank">calc</a> (the free version of excel) and it's done by finding a random number that fits on the frame (between 0 and 320 for x and 0 and 420 for y) and then using the previous frame and going ±5 to make some sort of noise. It's not the best test data, but it should do.  <embed src="Images/Antipodes/generateded-test-data.swf" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/shockwave/download/" height="448" width="500"></embed>I think that at the moment, as I'm going to be interested mainly in paths, I'm going to try and just reconstruct the paths from the xy 'point cloud' data as a post processing thing. that way I can get nice vectors. If I can do some sort of <a href="http://en.wikipedia.org/wiki/Comma-separated_values">csv</a> or excel out from processing then I'll just rebuild the data in GC as I'm so comfortable programming there.  <embed src="Images/Antipodes/salesman.swf" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/shockwave/download/" height="500" width="500"></embed>This is the output of a brute force traveling salesman type thing that I did yesterday after I got sidetracked trying to prototype the code for this.The actual  way of writing the file will have to be a 90° rotation of the way that I've shown it to be in the test data though, as the data will come out frame by frame along the line. So it'll look like</p>
<pre>blob1X,blob1Y,blob2X,blob2X,blob3X,blob3Y...        etc.
xval,  yval,  xval,  yval,  xval,  yval</pre>
<p>That'll bung out a massive list of data for me to process in GC.I'm going to stick with a maximum of 20 blobs in a frame at any time, I think this'll be plenty. as blobs appear and disappear they'll stay in the track associated with their index number, this means that as blob 1 disappears blob 5 becomes blob 4. as all the data will be post processed this isn't actually a problem (as I previously thought when trying to think it through in real time)</p>
<p>I think the solution the problem of working out where one path starts and another one ends can be solved in post processing by giving a maximum search radius. Then if there is nothing in the radius, then it'll start making a new path.</p>
