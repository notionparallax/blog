---
layout: post
title: centroid of points on the surface of a sphere
date: 2009-05-16 08:21:04.000000000 +10:00
type: post
published: true
status: publish
categories: []
tags:
- GC
- geek
description:
meta:
dsq_thread_id: '4503552955'

---
<p>I was sat in the airport after SG, trying to figure out the logistics of the tutor group meeting up. Where would be the most logical place to go?</p>
<p>As I'd been thinking about geeky problems for the preceding week, my brain was fixed into that way of thinking, and started on trying to figure out the centroid of people's locations on the globe. This one seemed easy until I tried to think it through and realised that there was a big stick in the spokes.</p>
<p>The seam!</p>
<p>Put more generally, assume that you have some points distributed randomly on the surface of a sphere, how do you find find the centroid of them?</p>
<p>Put into a (vaguely) real world example, my friends live all over the world, assuming that we all have amphibious planes as our only means of transport, where is the most convenient place for us all to meet up? (assuming that we also have a thunderbirds style floating island, and air space rights to everywhere etc.)</p>
<p>The obvious answer is that we map it back onto a plane, and then solve it on the plane, but this only works if people are clustered in one place.</p>
<p>As I'm British, I've got a British map with UK in the centre. If I lived in Alaska (hi Sarah P), and my friend lives in Vladivostock, (simple case with only 2 points) I can draw a line between us and we should meet at the midpoint of this line. simple.</p>
<p><img alt="" src="{{ site.baseurl }}/assets/World-map-without-dots.gif" width="100%" /></p>
<p>No, that point is in Norway somewhere, which is clearly wrong as the centroid of our positions is somewhere in the Aleutian isles or in the Bearing straights. So what's the solution?</p>
<p><img alt="" src="{{ site.baseurl }}/assets/world-map.gif" width="100%" /></p>
<p>I found <a href="http://mapgallery.esri.com/2008/839/graphics_poster_acrobat.pdf" target="_blank">this PDF outining a solution</a>, but it doesn't make much sense, and it's both a bit mathematical, and a bit clunky. Is there an elegant solution out there?</p>
<p class="content">I've come up with a few possible solutions, I'd be interested to see what other people think.</p>
<h2>solution 1 - pair wise great circle solving</h2>
<p class="content"><img alt="" src="{{ site.baseurl }}/assets/original.aspx" width="319" height="320" align="right" /></p>
<p>With a given set of points on a sphere, pick 2, draw two complementary arcs through these points with the centre of the sphere as the centre of the circle.</p>
<p>Pick the shorter of the two arcs and draw a point at it's midpoint.</p>
<p>remove the two initial points from the working set, and replace it with the new one</p>
<p>repeat until the centroid is found.</p>
<p>As I have no other way of testing this method, i can't be sure if it's accuarate. Does anyone have any insight?</p>
<p>Here's some GC script that produces a centroid point.</p>
<p>The only condition is that the points must lie on the surface of the a sphere.</p>
<pre class="c#">transaction script "make a centroid"
{
   Point workingSet = point01; //make the random points be our set of points to test

   Point finalPt = new Point("CentroidPt");// get a point ready to give to the world
   while (workingSet.Count &gt;= 2) //once we are down to two at the top, one will come out of the bottom
   {
      int indexEnum = Series(0,workingSet.Count-1,1);     //
      int indexOne = indexEnum[Random(workingSet.Count)]; //this section makes sure we have picked
      indexEnum = RemoveAt(indexEnum,indexOne);           //two unique points from the set
      int indexTwo = indexEnum[Random(workingSet.Count)]; //

      //set a workign plane based on those points
      Plane tempPlane = new Plane().ByOriginXYPoints(baseCS, workingSet[indexOne], workingSet[indexTwo]);

      //draw two arcs through the points with the centre as the centre of the earth
      double theAng = Angle(baseCS,workingSet[indexOne], workingSet[indexTwo]);
      Arc tempArc1 = new Arc();
      tempArc1.ByCenterRadiusSweepAngle(baseCS, tempPlane, 10, 0, theAng);
      Arc tempArc2 = new Arc();
      tempArc2.ByCenterRadiusSweepAngle(baseCS, tempPlane, 10, theAng, 360-theAng);

      //test to see which arc is shortest
      Point childPt = new Point();
      if (tempArc1.Length</pre>
<p>I can't see any problems with this except that it's not going to be very fast, and it relies heavily on geometry libraries. There must be a faster way, although I think this is likely to be the most easily understood solution.</p>
<h2 class="forum-post-panel-main clear-block">solution 2 -  mean vector</h2>
<p class="forum-post-panel-main clear-block">I think this will work, but I'm not sure, there are some indications from a GC model that there is something fishy about it, and I can think of situations where it might fail.</p>
<p class="forum-post-panel-main clear-block">From the centre of the earth to each person is a vector (x,y,z) which will have a length of 1 if we assume that the earth has a radius of 1.</p>
<p class="forum-post-panel-main clear-block">if we round up all the vectors and average their x,y and z components then we'll get a vector that has the right direction.</p>
<p class="forum-post-panel-main clear-block">If we then unitise it so that it's length is 1 again, it's endpoint will be the meeting place.</p>
<h2 class="forum-post-panel-main clear-block">solution 3 - manipulation of lat and long</h2>
<p>I'm still working on this, but there must be a way to give back both values for the average latitude, but I'm not sure how at the moment. I can make it work fine for 2 points on a circle, but 3 goes wrong.</p>
<p>There will be updates to this post over the next week. hopefully a solution, and definitely lots more diagrams and gct sketches.</p>
<p>if you've got anything to pitch in, please comment, if i don't solve this soon, it may lead to divorce!</p>
