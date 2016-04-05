---
layout: post
title: the experiment continues
date: 2008-03-31 13:55:41.000000000 +11:00
type: post
published: true
status: publish
categories: []
tags:
- architecture
- geek
- hardware

---
<p>upon getting stuck into any seemingly simple problem, more complicated things always seem to arise.</p>
<p>I think I'll get something at least a little bit useful out of this soon though.</p>
<p>lots of tests and diagrams after this </p>
<table>
<tr>
<td><img src="{{ site.baseurl }}/assets/08-03-31_tracker_progress_0005_Layer%201.jpg" height="271" /></td>
<td>This is the stock code for finding blobs, but with an extra line that marks the centres of the boxes</td>
</tr>
<tr>
<td><img src="{{ site.baseurl }}/assets/08-03-31_tracker_progress_0004_Layer%202.jpg" height="271" /></td>
<td>They make a bit more sense with just the edges turned on.<br />
Ultimately the display of all this data will be switched off to maximise running speed.</td>
</tr>
<tr>
<td><img src="{{ site.baseurl }}/assets/08-03-31_tracker_progress_0003_Layer%203.jpg" height="271" /></td>
<td>The centre markers can be tagged...</td>
</tr>
<tr>
<td><img src="{{ site.baseurl }}/assets/08-03-31_tracker_progress_0002_Layer%204.jpg" height="271" /></td>
<td>..with a number to identify them.<br />
This highlights a problem that I had anticipated. The numbering (array index) of the blobs is dynamically assigned. They are detected on a frame by frame basis, and therefore the numbering is not consistent across frames. This means that the paths can't just be drawn, but I'll need to do some sort of proximity search to find the nearest one to the previous one, and just hope that the movement isn't sufficiently large to upset the progression.</td>
</tr>
<tr>
<td><img src="{{ site.baseurl }}/assets/08-03-31_tracker_progress_0001_Layer%205.jpg" height="271" /></td>
<td>First attempts at tracking points are proving tricky, even without any sort of continuity tracking.</td>
</tr>
<tr>
<td><img src="{{ site.baseurl }}/assets/08-03-31_tracker_progress_0000_Layer%206.jpg" height="271" /></td>
<td>If the vertices with 0,0 coords are removed, it just spatters points.<br />
This also highlights the vast quantity of data that I am gathering here.<br />
There will probably need to be some sort of data reduction at the end, as at 10 fps, with 5 blobs, that produces 100 values a second, so even recording for a minute will make a huge dataset.</td>
</tr>
</table>
<p>The mapping of a point from frame to frame is going to prove to be the most complicated part of this operation<br />
<embed src="Images/Antipodes/frame-to-frame-mapping.swf" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/shockwave/download/" height="400" width="500"></embed>The possible options for frame to frame changes in path coordinate arrays. <embed src="Images/Antipodes/frame-to-frame-conditions.swf" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/shockwave/download/" height="500" width="500"></embed>I'm going to have a go at implementing a solution that tests to see if there is a centroid in the previous frame within 10ish pixels of the current one, then if there is, starts measuring it's path and adds the list of coords to a list.<br />
It'll take a bit of fiddling to find out how to work with lists in processing, but it should work.I should probably also implement a filter that only bothers dealing with blobs if they are over a certain number of pixels in area, as <a href="http://www.codeproject.com/KB/audio-video/Motion_Detection.aspx" target="_blank">suggested here</a>.There are all kinds of issues that will probably pop up. I find this sort of data management/array stuff quite hard to get my head around. I wonder why?</p>
