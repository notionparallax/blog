---
layout: post
title: Define and control the API - be powerful
date: 2015-08-24 07:00:25.000000000 +10:00
type: post
published: true
status: publish
categories: []
tags:
- BVN
- data
- manifesto
description:
meta:
  _publicize_facebook_user: http://www.facebook.com/541400612
  _publicize_twitter_user: "@notionparallax"

---
<style type="text/css">
.minibar {
      width: 40%;
      display: block;
      float: right;
      transform: translateX(2em);
      background-color: rgba(255,255,255,0.2);
      padding: 1em;
      font-size: 70%;
    }
    .api-links a {
      display: inline-block;
      width: 20%;
      height: 15em;
      float: left;
      padding: 0.5%;
    }
    .api-links a img {
      width: 100%;
    }
    .api-links:after {
      display: block;
      clear: both;
      content: " ";
    }</style>

API is a big buzzword. It's really confusing until you know what it means.

An Application Programmer Interface (API[16. <a href="https://www.google.com/url?q=https%3A%2F%2Fwww.codecademy.com%2Fen%2Ftracks%2Fyoutube&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNEc-H9T8Mj46IggXXnMD1dmj-e_rA">Here's a course that teaches you about APIs</a> and how to use them. In this case to control YouTube. There are also a whole load of others that you can learn about on there too. Then you'll be an API BOSS.]) is just like any other interface to software. You interact with your computer with a Graphical User Interface (GUI). If you talk to Siri then that's an audio user interface (AUI I suppose).

An API interfaces with software but with text not icons. Old school AutoCad nerds should be totally into that idea.

To put it in simple terms APIs let programmers plug one system into another system.
<div class="minibar">Actually, you can't because you are outside the firewall. Trust me, if you were inside it'd be amazing. <a href="https://github.com/bvn-architecture/OAF">Check it out on GitHub for all the details</a>!</div>

Here's an example of an API in use. This one is made by our very own Dave Wilcox. It's called Open Asset Fixer, or OAF for short.

You can try it out here.
<p style="padding-left: 30px;"><code>phonelist.bvn.com.au:4567/S0910004/main/0/web_view</code>

That would get you the highest rated image from the S0910004 project, with the webview size.

You can try it yourself by copying it into the address bar and noodling about with the values . The pattern is:
<p style="padding-left: 30px;"><code>phonelist.bvn.com.au:4567/:project_number/:tag/:index/:size</code>

<code>size</code> must be one of: <code>square</code>thumbnail, <code>small</code>, <code>web_view or <code>medium</code>.</code>

You can use this to get pictures of any project into a blog post on Tropos[17. You could use it from anywhere in the world, but the way our firewall and DNS is set up means that it is invisible from the outside world. If that wasn't the case it would work because it is made of internet.].

This gets the highest rated image for that project from Open Asset for you to do something useful with.

You can think of that as a way of plugging into a system, where Open Asset is the system. You could be plugging anything into it. In our case we plug the People + Projects system into it.

There are lots of APIs out there. It's virtually essential these days to have one if you want to be taken seriously!

Interfaces are powerful, they give us control of systems. They allow people to do things. They also exert power, they control what things can be done and how these things can be done.

We're in one of those wild west situations with data and APIs. Whoever makes it across the prairie can open the data mine and control the data supply.

We are collecting data and marshalling it into useful shapes. We need to decide what to do with it. Data kept in a box is worthless. Data wants to be socialised!

If we are brave citizens of the 21<sup>st</sup> century then we can make an interface that gives access to our data and controls who it gives access to. We can also set a precedent to our peers in the rest of the architecture world who are just about getting to grips with being brave citizens of the 20<sup>th</sup> century!

Part of the fun–and the challenge–of designing an API is that you have no idea what it will be used for. It could be for us to build our website[18. using your own software/systems is charmingly called dogfooding]. It could be a PhD researcher doing statistical analysis of Architectural firms over 50 years old. It could be a teacher explaining to 9-year-olds how to use APIs. It could even be ISIS collecting up images of Australian government buildings.

I don't mention that last one to undermine my argument, but to bring up the issue of paranoia. Someone always brings up a “what if… [insert bad thing here]… happens?” With APIs this issue is answered by what they are usually used for: making websites. If the data is OK to put on a website then it is OK to access it via the API. There are always worst case scenarios but if we were paralysed by caution on all of them then nothing would ever get done!
<hr />
<div class="api-links"><a class="api-link" href="https://www.codecademy.com/en/tracks/apigee"><img class="api-card__logo--dark" src="{{ site.baseurl }}/assets/apigee-4a520ff47615b11efbbf1f1ac9b7e222.png" alt="Apigee" />Learn how to use Apigee's API to store your app data in the cloud!</a><a class="api-link" href="https://www.codecademy.com/en/tracks/apigee"><img class="api-card__logo--dark" src="{{ site.baseurl }}/assets/wepay_ruby-9d6921011ec820175616b1f4df2c0fb3.png" alt="Wepay_ruby" />Learn how to use the WePay API!</a><a class="api-link" href="https://www.codecademy.com/en/tracks/wepay_ruby"><img class="api-card__logo--dark" src="{{ site.baseurl }}/assets/youtube-5dfbbca603af73360f51e12871aff155.png" alt="Youtube" />Learn how to use the YouTube API!</a><a class="api-link" href="https://www.codecademy.com/en/tracks/youtube"><img class="api-card__logo--dark" src="{{ site.baseurl }}/assets/wepay_python-9d6921011ec820175616b1f4df2c0fb3.png" alt="Wepay_python" />Learn how to use the WePay API!</a><a class="api-link" href="https://www.codecademy.com/en/tracks/wepay_python"><img class="api-card__logo--dark" src="{{ site.baseurl }}/assets/box_api-8f4126255c5923d08a1828da5380da74.png" alt="Box_api" />Learn how to use the Box API!</a><a class="api-link" href="https://www.codecademy.com/en/tracks/box_api"><img class="api-card__logo--dark" src="{{ site.baseurl }}/assets/oauth-3d0dacbc67e989f4e151fa4cc29a6cf4.png" alt="Oauth" />Learn OAuth2 with the GitHub API</a><a class="api-link" href="https://www.codecademy.com/en/tracks/oauth"><img class="api-card__logo--dark" src="{{ site.baseurl }}/assets/soundcloud-ed814c92469e708ed5f86f73de02d149.png" alt="Soundcloud" />Learn how to use the SoundCloud API!</a><a class="api-link" href="https://www.codecademy.com/en/tracks/soundcloud"><img class="api-card__logo--dark" src="{{ site.baseurl }}/assets/mandrill-f6f35ee33e282022ef016a077c50d719.png" alt="Mandrill" />Learn how to use the Mandrill API!</a><a class="api-link" href="https://www.codecademy.com/en/tracks/mandrill"><img class="api-card__logo--dark" src="{{ site.baseurl }}/assets/npr-3a0cb92871a6b21a1c7163c5913f6673.png" alt="Npr" />Learn to use the NPR API</a><a class="api-link" href="https://www.codecademy.com/en/tracks/npr"><img class="api-card__logo--dark" src="{{ site.baseurl }}/assets/dwolla-136bce68b8949bd0772f868b9a9cd365.png" alt="Dwolla" />Learn how to use the Dwolla API!</a><a class="api-link" href="https://www.codecademy.com/en/tracks/dwolla"><img class="api-card__logo--dark" src="{{ site.baseurl }}/assets/evernote-b32ea1e156b3726193e4336ee2d19e18.png" alt="Evernote" />Learn how to use the Evernote API!</a><a class="api-link" href="https://www.codecademy.com/en/tracks/evernote"><img class="api-card__logo--dark" src="{{ site.baseurl }}/assets/nhtsa-a1945bc0e9cc40938d0c826ec07611d8.png" alt="Nhtsa" />Learn how to use Python and the National Highway Traffic Safety Administration's API!</a><a class="api-link" href="https://www.codecademy.com/en/tracks/nhtsa"><img class="api-card__logo--dark" src="{{ site.baseurl }}/assets/twitter-c76f0c72dca232a0a6a2c970f91c66cc.png" alt="Twitter" />Learn how to use the Twitter API!</a><a class="api-link" href="https://www.codecademy.com/en/tracks/twitter"><img class="api-card__logo--dark" src="{{ site.baseurl }}/assets/sendgrid-f1de2c2ba34221def46519f9a9ae7653.png" alt="Sendgrid" />Learn to use the SendGrid API</a></div>
<hr />
