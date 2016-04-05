---
layout: post
title: Connecting a slider to a property to in Blend
date: 2009-07-27 21:11:27.000000000 +10:00
type: post
published: true
status: publish
categories: []
tags:
- geek
- tutorials

---
<p><img class="alignleft size-full wp-image-191" title="thermo1" src="{{ site.baseurl }}/assets/thermo1.png" alt="thermo1" width="157" height="454" />I felt pretty stupid for a couple of days trying to wire a slider up to a property in Expression Blend. I finally figured it out, so I thought I'd share the love as I didn't see any tutorials on line.</p>
<p>So you have a new project in blend, it doesn't much matter if it's destined for wpf or silverlight, as far as I can tell the procedure is the same.</p>
<p>I've used a mega pointless thermometer to illustrate this, hopefully you'll pick something less crap. (if you do, put a link to it in the comments!) </p>
<p>So I've drawn the thermometer as a rectangle and a circle. The circle is red, and the rectangle is a gradient between red and blue. The slider is going to control where the gradient stop is so that it looks like we are controlling the temperature with the slider.</p>
<p>So first thing's first, you need some elements, so draw a thermometer, and throw in a slider. You'll need to edit the slider's properties a bit to make it be vertical.</p>
<p><img class="size-full wp-image-199 alignnone" title="thermo2" src="{{ site.baseurl }}/assets/thermo2.jpg" alt="thermo2" width="312" height="542" /></p>
<p>Select the rectangle, and edit it's fill. Set the gradient so that it looks right at the coldest end of the slider. Make sure you have the blue gradient stop selected, and then click it's “Advanced Properties Options” icon, that's the tiny little white dot to the right of the value.</p>
<p><img class="alignnone size-full wp-image-192" title="thermo3" src="{{ site.baseurl }}/assets/thermo3.png" alt="thermo3" width="210" height="312" /></p>
<p>Click 'Data Binding' and it'll take you to the create data binding dialogue.</p>
<p><img class="alignnone size-full wp-image-193" title="thermo4" src="{{ site.baseurl }}/assets/thermo4.png" alt="thermo4" width="653" height="132" /><br />
Select 'element property', and you'll get a list of elements in your scene on the left, and once you've selected one of them, a list of that element's properties on the right.</p>
<p><img class="alignnone size-full wp-image-194" title="thermo5" src="{{ site.baseurl }}/assets/thermo5.png" alt="thermo5" width="616" height="580" /></p>
<p>If you scroll all the way to the bottom, the important one for sliders is 'Value' just select it and away you go!</p>
<p>Build the project (F5) and see what happens.</p>
<p>For me, there were a few issues. The range was wrong on the slider, and the slider was sliding the wrong way.</p>
<p><img class="alignleft size-full wp-image-198" title="thermo9" src="{{ site.baseurl }}/assets/thermo9.png" alt="thermo9" width="263" height="357" />To fix the range, select the slider and edit it's 'common properties' the range on the gradient stop says it's 0-100% but really it's 0-1 as a double (programmer thinking alert), but we've set the red stop to about 80% so we need to set the range as maximum 0.8, minimum 0.</p>
<p>that fixes the range, but the slider is still working the opposite way to the way we expect. I'd imagine that there is an elegant way to fix this, but I just rotated the slider by 180° and all is forgiven!<img class="alignright size-full wp-image-197" title="thermo8" src="{{ site.baseurl }}/assets/thermo8.png" alt="thermo8" width="157" height="454" /></p>
<p><a href="http://www.notionparallax.co.uk/wordpress/wp-content/uploads/2009/07/pointless-thermometer.zip">Here's the source files</a></p>
<p>You'll have to forgive me if there is anything patently wrong in this tutorial, it has been written on a train, and I've been using blend for less than a week, but it is good to talk...<br />
I'm sure that there are better ways to do this, so if you know, make a comment!</p>
<p><span style="color: #ffffff;">If you are reading this on facebook and you feel moved to make a comment, spare a thought for my online karma and copy the comment from facebook to </span><a href="http://www.notionparallax.co.uk/wordpress" target="_blank"><span style="color: #ffffff;">www.notionparallax.co.uk/blog</span></a><span style="color: #ffffff;"> so that it shows up in both places. Ta.</span></p>
