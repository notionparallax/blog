---
layout: post
title: Grind size analysis app
date: 2016-01-11 08:00:48.000000000 +11:00
type: post
published: true
status: publish
categories: []
tags: []
description: "Another app idea that I'm never going to make so someone else can have it. Grid size is really hard to get right for home coffee nerds."
meta:
  _publicize_facebook_user: http://www.facebook.com/541400612
  _publicize_twitter_user: "@notionparallax"
  _wpas_mess: An idea for a Grind size analysis app?

---
<style type="text/css">
  .monster{width:100%;}
  svg.example{
      width:  100%;
      height: 100%;
      stroke: red;
      fill: none;
      stroke-width: 0.1;
    }
</style>
<p>Another <a href="http://notionparallax.co.uk/?p=2040">app idea</a> that I'm never going to make so someone else can have it. Grid size is really hard to get right for home coffee nerds. If you've got a 250g bag of something expensive, you can't run half of it through the grinder to get the grind right. This is an especially big problem if you are running different brew techniques[^1].</p>
<p><a href="/wordpress/wp-content/uploads/2015/12/grains.png" rel="attachment wp-att-2698"><img class="alignnone size-full wp-image-2698" src="{{ site.baseurl }}/assets/grains.png" alt="grains" /></a></p>
<p>The factors everyone cares about are particle size and consistency. How big are the chunks, and how much do those sizes vary?</p>
<p>Modern smartphone cameras are amazingly high resolution. This photo is a crop out of the middle of a picture from my Nexus 6p on 5mm squared paper. At my screen resolution each square is about 25mm, so that's plenty of magnification.</p>
<p>The question is:</p>
<blockquote><p>Can modern smartphone cameras + computer vision + some graph paper[^2] measure particle size usefully well?</p>
</blockquote>
<p>Here's an enlarged square, bigger than 100%:</p>
<p><svg class="example" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewbox="0 0 19.488182 19.488188" height="5.5mm" width="5.5mm">    <image preserveaspectratio="none" xlink:href="http://notionparallax.co.uk/wordpress/wp-content/uploads/2016/01/coffee-square.png" y="-.593" x="-.402" height="21.145" width="20.936" />    <rect y="1.145" x="1.2" height="17.348" width="17.796" />    <ellipse rx=".162" ry=".151" cy="7.671" cx="13.716" />    <ellipse rx=".209" ry=".209" cy="12.803" cx="13.624" />    <ellipse rx=".266" ry=".174" cy="14.32" cx="8.26" />    <ellipse rx=".278" ry=".197" cy="6.025" cx="4.286" />    <ellipse rx=".475" ry=".44" cy="12.038" cx="11.643" />    <ellipse rx=".278" ry=".672" cy="15.514" cx="9.36" />    <ellipse rx=".371" ry=".197" cy="5.353" cx="17.308" />    <ellipse rx=".382" ry=".869" cy="10.662" cx="12.827" transform="rotate(-15.404)" />    <ellipse rx=".44" ry=".44" cy="6.616" cx="2.919" />    <ellipse rx=".463" ry=".255" cy="18.063" cx="6.325" />    <ellipse rx=".521" ry=".405" cy="2.967" cx="5.804" />    <ellipse rx=".545" ry=".568" cy="7.74" cx="9.187" />    <ellipse rx=".75" ry=".463" cy="6.083" cx="8.341" />    <ellipse rx=".637" ry=".846" cy="12.119" cx="7.843" />    <ellipse rx=".915" ry="1.193" cy="3.523" cx="12.894" />    <ellipse rx="1.365" ry="2.114" cy="3.968" cx="20.705" transform="rotate(27.845)" /></svg></p>
<p>I have no idea if there is enough contrast in the images for the <abbr title="computer vision">CV</abbr> algorithm to see grain boundaries. Maybe that's not even required, perhaps you can just do blob detection on the smallest particles?</p>

<iframe width="600" height="371" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/137age3FI3P_Sq6dBXcol-zP8nkLwo-OWGxPez4-pCgo/pubchart?oid=159538498&amp;format=interactive">
There really should be an iframe here :(
</iframe>

<p>Seems like a pretty straight middle section, and maybe you could just discard anything really big as likely to be a clump?</p>
<p>Anyway, let me know if you are a CV genius and you make this app, I'd use it. </p>

[^1]: We've got one of almost everything in our house except turkish and espresso.

[^2]: Graph paper for context, maybe you could use some other context thing, like a Nickel or a ruler.