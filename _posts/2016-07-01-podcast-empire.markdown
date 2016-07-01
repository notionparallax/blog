---
layout: post
title: Podcast empire
date: 2016-07-01 15:30:36 PDT
type: post
published: true
status: publish
categories: []
tags: []

#this goes on the index page, and into facebook shares
description: A startup idea that I'm too lazy to implement

# This is what twitter will pick up if someone tweets the link to this page 
# 110 marker 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
twitter-body: A startup idea that I'm too lazy to implement
#Twitter and facebook will pick up this image. you can also use it in a post with:
# ![alt text]({{ site.baseurl }}/assets/{{page.featuredimg}}) 
featuredimg: 16/radioempire.jpg
---

I had this idea a little while ago, but I doubt I'll ever get around to doing anything with it, so feel free to build it out into million dollar business. Maybe, if you do, you could buy me a beer.

[Podcasts that I listen to](https://notionparallax.co.uk/2015/podcasts-i-listen-to) seem to fit quite neatly into two camps. On one hand you have the high production levels of _This American life_, _99% Invisible_ and _Planet Money_[^1]. On the other you've got things like _Rationally Speaking_ or _EconTalk_, which are more like people chatting, often with one of those people on the phone.

[^1]: I don't actually listen to _This American life_, but a lot of people do, so I put it in as an illustrative example.

# Problem

The latter type need a bit of help! No matter how fancy you get with digital phones and recording setups, the audio quality will always be a bit crap for the person who's calling in. 

_But_ most podcasts aren't live. Why not record the audio at high quality at both ends. There's no need to have all the sound mixed immediately, so just don't.

# Solution

With [WebRTC](https://webrtc.org/) you can handle the broadcast part of the setup, and with the [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API) you can record high quality files at each endpoint. Then you just merge the two sound files and you've got something that feels like both people were in the studio together!

# Err, there's another problem

> This seems like a good idea, but what's to stop an engineer at Skype ripping it off in an hour?

That is the big question but I think I have a solution.

(Of course this is only a problem if you care about this as a commercially viable product and not just an open source toy.)

# Solution to the other problem

One of the other problems in podcast land is that they are monolithic chunks of audio data. The ads are the same for everyone, no matter where they live or what they're like. If you are mixing the audio on a server for the podcast host then it'd be pretty easy to insert flexible chunks of time that can be filled however you want. (Some people are already doing something a bit like this with [midroll ads](https://www.google.ca/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8&client=ubuntu#q=midroll%20ads).)

Once you've got a series of content segments then it's easy to concatenate them together with advert segments, potentially even to order. Then each person has their own download link to the podcast.

That's still not that hard, but it's not core business for Skype, or anyone else who's into being a phone/messaging company.

# Other things
Once you've got an interface for editing audio, you can make new kinds of product. The one that interests me most at the moment is something I'm calling 'yep' for the moment.

This is for instructional audio and videos. You press play, it tells you what step one is, then it pauses and waits for you to say something (_yep_).

Initially it'd be linear, but there's no reason that you wouldn't go into things like choose your own adventure stories where it could have side segments:

> does your sauce look delicious and creamy?

> NO!

> If it's split, put it in the blender for a bit.

> yep

> is it looking good now?

> yep
 
... and then back onto the regular story

and so on.

