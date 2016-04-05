---
layout: post
title: why Postednot.es ?
date: 2014-07-15 00:00:36.000000000 +10:00
type: post
published: true
status: publish
categories: []
tags: []
description:
meta:
  _edit_last: '2'
  _publicize_facebook_user: https://www.facebook.com/ben.doherty1
  _publicize_twitter_user: "@notionparallax"
  _wpas_mess: 'Why Postednot.es ? How lean can I be, and how can the lazy become internet
    millionaires: step 4) PROFIT!! http://wp.me/p3wwRK-qv'

---
<style type="text/css">
  .fake-form{
      width: inherit;
      background-color: cornsilk; 
      padding: 0.5em; 
      float: right; 
      margin-left: 1em;
      -webkit-transform: scale(0.9);/*lolz*/
    }
    .fake-form input{width:10em;}
    .fake-form label{}
    .fake-form br{display:none;}
</style>
<p><a href="http://postednot.es"><img class="alignright wp-image-1651" style="height: 10em;" src="{{ site.baseurl }}/assets/letter.png" alt="letter" /></a><a href="http://postednot.es">Postednot.es</a> started as an experiment in how much could be achieved on a fairly limited development skillset. It is almost entirely a learning experience, an experiment in how lean an idea can be, and the business aspect is there to keep it spicy. (Although probably the thing I have to learn the most about is the bizzo end of things!) </p>
<p>There are some incredible tutorials on how to make custom paypal buttons with curlz so that you can sell crochet cat knickers on your blogger page. I figured that if these strange ladies could use this as a way of paying the bills then it was certainly worth a look.</p>
<p><img class="alignright" style="height: 2em;" src="{{ site.baseurl }}/assets/fe9491d3b8e00dd576ae70f1bab09b.gif" alt="" width="252" height="66" />The <a href="https://www.paypal.com/au/cgi-bin/webscr?cmd=_singleitem-intro-outside">PayPal "Buy Now" button</a> is an amazing thing. You generate some code on their site and then paste it into yours and you are off on your journey to becoming an internet millionaire! If you can read that code then you realise that there's a lot of potential for modifying it.</p>
<div class="fake-form"><label for="input1">Input 1<input name="input1" type="text" placeholder="Max 200 chars" /></label><br />
<label for="input2">Input 2<input name="input2" type="text" placeholder="Max 200 chars" /></label><br />
<label for="input3">Input 3<input name="input3" type="text" placeholder="Max 200 chars" /></label><br />
<label for="input4">Input 4<input name="input4" type="text" placeholder="Max 200 chars" /></label><br />
<label for="input5">Input 5<input name="input5" type="text" placeholder="Max 200 chars" /></label><br />
<label for="input6">Input 6<input name="input6" type="text" placeholder="Max 200 chars" /></label><br />
<label for="input7">Input 7<input name="input7" type="text" placeholder="Max 200 chars" /></label><br />
<label for="input8">Input 8<input name="input8" type="text" placeholder="Max 200 chars" /></label></div>
<p>I'm pretty backward when it comes to back-end. It's one of those things that I've never really got around to, so I'm always on the lookout for ways to get around the need for a database. The _buy now_ button allows for eight input fields, each with 200 characters in their values. This is super cool if you have 8 fairly big text inputs, but that's a pretty unlikely situation. This is where the idea for postednot.es came from, what can you do with a bunch of text fields and a pay now button[1. I have since found a whole load of other people who do the same thing: M<a href="https://maillift.com/">ail Lift</a>, <a href="http://letterfriend.com/">Letter Friend</a>, <a href="http://handwrittenletterservice.com/">Handwritten letter service</a>, <a href="http://handiemail.com">Handiemail</a> and of course <span style="color: #4e5665;"><a href="http://BeautifulHandwrittenLetters.com">BeautifulHandwrittenLetters.com</a> I think it's worth sticking with it though. I don't think that first-mover advantage is particularly significant here.</span>].</p>
<p>What's much more likely to be useful is if you have a whole bunch of values that you want to be able to capture, but they don't need anything like 200 chars each or you have a couple of big inputs that take up _more_ than 200 chars (as <a href="http://postednot.es">postednot.es</a> does). What's needed here is a way of treating the 1600 chars as a single packet limit.</p>
<p>This is pretty easy with a bit of JS and some imagination. You just forget about these form elements being part of a form, make a real form (like the one on the right here) be invisible. and then scrape up the values of the form _you_ want and layer them carefully into the invisible form.</p>
<p>[**Diagram here I think!]**</p>
<p>Once your hidden form is loaded you can send it off to Paypal. Then it's step 4 all the way (Profit!!)</p>
<p>I'm thinking of doing a more enthusiastic and detailed breakdown of how I built Posted Notes soon if there is any kind of excitement about it. The structure would be:</p>
<ol>
<li>Getting a buy now button</li>
<li>Getting a page with Github pages</li>
<li>Building the form _you_ want</li>
<li>Packing it into _their_ form</li>
<li>Making it look well wicked</li>
<li>Adding google analytics up the wazoo so you can see what's going on.</li>
</ol>
<p>If you think that this is the kind of lazy, effort skirting route to being an internet millionaire that you can see yourself getting onto then let me know somehow and I'll make a tutorial happen.</p>


[^1]: I have since found a whole load of other people who do the same thing: M<a href="https://maillift.com/">ail Lift</a>, <a href="http://letterfriend.com/">Letter Friend</a>, <a href="http://handwrittenletterservice.com/">Handwritten letter service</a>, <a href="http://handiemail.com">Handiemail</a> and of course <span style="color: #4e5665;"><a href="http://BeautifulHandwrittenLetters.com">BeautifulHandwrittenLetters.com</a> I think it's worth sticking with it though. I don't think that first-mover advantage is particularly significant here.</span>

