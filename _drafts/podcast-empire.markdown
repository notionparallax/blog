---
layout: post
title: Podcast empire
date: 2016-03-21 09:26:12 PDT
type: post
published: true
status: publish
categories: []
tags: []
description: 
---

Podcasts that I listen to seem to fit quite neatly into two camps. On one hand you have the high production levels of _This American life_, _99% Invisible_ and _Planet Money_. On the other you've got things like _Rationally Speaking_ or _EconTalk_, which are more like people chatting, often with one of those people on the phone.

#Problem

The latter type need a bit of help! No matter how fancy you get with digital phones and recording setups, the audio quality will always be a bit crap for the person who's calling in. 

_But_ most podcasts aren't live. Why not record the audio at high quality at both ends. There's no need to have all the sound mixed immediatly, so just don't.

#Solution
With [WebRTC](https://webrtc.org/) you can handle the broadcast part of the setup, and with the [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API) you can record high quality files at each endpoint.

#Err, there's another problem

> This seems like a good idea, but what's to stop an engineer at skype ripping it off in an hour?

That is the big question but I think I have a solution.

(Of course this is only a problem if you care about this as a commercially viable product and not just an open source toy.)

#Solution to the other problem

One of the other problems in podcast land is that they are monolithic chinks of audio data. The ads are the same for everyone, no matter where they live or what they're like. If you are mixing the audio on a server for the podcast host then it'd be pretty easy to put in flexible chunks of time that can be filled however you want.

Once you've got a series of content segments then it's easy to concatenate them together with advert segments, potentially even to order. Then each person has their own download link to the podcast.

That's still not that hard, but it's not core business for Skype, or anyone else who's into being a phone/messaging company.

#Other things
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

