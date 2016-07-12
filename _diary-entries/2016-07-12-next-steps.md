---
layout: post
title: Next steps
date: 2016-07-12 12:00:00 PDT
type: post
published: true
status: publish
categories: []
tags: []

# this goes on the index page, and into facebook shares
description: 

# This is what twitter will pick up if someone tweets the link to this page 
# 110 marker 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
twitter-body:
# Twitter and facebook will pick up this image. you can also use it in a post with:
# ![alt text]({{ site.baseurl }}/assets/{{page.featuredimg}}) 
featuredimg: 
---
OK, here's another one of my big task list type posts.

The reason I'm writing it is that I think we're almost ready to install the Raspberry PIs, probably in BVN. Here's the things I think are in the way. They are more or less in the order that they need to be done so that one doesn't trip another one up (some of them can be done in parallel).

1. ### Working out the layout of the base stations
    The layout that Annisa did looks very feasible in that it covers the whole office and only needs 27 bases. The problem I see is that the bases aren't placed in any relationship to the furniture in the room. My guess is that we need to take the current layout as a starting point and tweak it a bit to have each base station sitting somewhere useful. I'd say that useful places would be something like the middle of a desk, but in places that aren't going to work that way we'll need to find somewhere near a plug. This is a lot less work than mapping out all the plug sockets in the office; just the ones that aren't near a desk.

    It will almost certainly increase the number of bases but that's fine.
    ![automagic BVN base station layout](http://where-in.space/assets/isovist/ISOVIST_BVN_FURN.PNG)

1. ### Get results from existing experiments closed out
    This is 2 things:
    1. Report on the data from the rotating experiment.
        ![]({{ site.baseurl }}/assets/16/tracking/scatterWsine.png)
        We should hopefully see this data looking like it's fitting the sine wave nicely. Then we can wrap it around into a polar graph and see how that looks.
    2. Show the simulated movement data on the nav mesh.
        ![](https://scontent-sea1-1.xx.fbcdn.net/v/t34.0-12/13510619_10153891117486339_2019205684_n.jpg?oh=652d407d998fda8aadca11fab2a22594&oe=5786F1CD) We've got the nav mesh in place, we've got the (naively) simulated data. We just need to get the sim-paths to walk around the furniture. This is quite important in trust building. If people see that you are able to show a path that looks believable then they are likely to believe you when you way that you're ready to order a whole bunch of hardware.

        It'll also put you in a good position once you have real data to quickly be able to visualise path data which is essential for al of your particular angles.

    I don't know how you are getting single values from the stream of data coming out of the base stations. Let's stop presenting single values and show ranges. If you use scatter plots then you can see how the values are clustered. It'll make me feel much more comfortable. You can do this in both spreadsheets and scientific computing, so lets start now!

1. ### Work out a deployment plan
    How do we go about installing the bases? How does everyone get a beacon? How do you register the beacon to the person?

1. ### Getting people on board with being tracked
    This is going to be an exercise in politics and persuasion. You'll have principal support at BVN, at least in theory. We need to come up with a series of Tropos posts about why tracking is important, what we get from it, what data is collected, that kind of thing.

    It sounds like extra work, but the discipline of writing for this audience will make the content better for your thesis, so it'll actually have a double use.

    Let's have an editorial brain storm soon and work out what we'll need to say.

1. ### Design of the base stations
    The RPIs will need to be housed some way so that they can't be prodded too much. I've been working on some ideas of how to do it, so unless you guys have some alternative idea that you are particularly keen on, lets start with my sketches, model them up, 3D print them and see how we go. Then we can see what we need to change.

    ![sketch of a base station](https://scontent-sea1-1.xx.fbcdn.net/v/t34.0-12/13672208_10157228788070613_484309052_n.jpg?oh=2345d04c30ea1e92c928febee3fc62bf&oe=5787D12E)

    The base stations are a a bit over designed because they have some space left in there to accommodate future sensor upgrades.

1. ### Design of the beacon
    This is going to be important in keeping everyone happy about being tracked. It's essentially jewellery and BVN is full of people who'd love to flex their skills as designers (Arup too I'd imagine).
    We need to put together a brief for the design competition, and a plan on how we're going to run it. I have a voting website that we could use to decide on a winner.

    Things to go in the brief are:

    * We need the design to encourage people to wear their beacon in a certain place on their body so that the signals are consistent.
    * It needs to be something people want to wear.
    * It needs to be sturdy enough to last for a decent length of time.
    * Etc. What else needs to go into this brief?


I'd like to see this all planned out with who is going to take responsibility for each part of each task, and an estimated time scale for it. Remember this isn't who's going to _do_ the work, just who I'm going to harass if it's not done.

My preference is that all of it gets done badly, then we can go over it and make it better. If we tick things off one by one when they are perfect we'll never progress.