---
layout: post
title: Let's get coffee and a doughnut on the way
date: 2016-03-21 15:34:23 PDT
type: post
published: true
status: publish
categories: []
tags: []
description: Can we ask mapping systems simple things like this? It's going to be important for conversational interfaces.
---

I'm writing a piece of speculative fiction to see if I can tie all my ideas about the future together. It's probably not very good but, as with this blog, I'm writing it as therapy for me, not to sell books. If I ever finish it I'll post it here[^1]. 

One of the bits of it has the protagonist picking up dinner on his way home from the airport in an Uber. Today we found ourself in a similar situation, except this time we wanted to get coffee and a doughnut on the way somewhere.

This kind of query is quite natural for a human brain to do. It is a bit taxing sometimes to come up with an answer, but it's not possible with the way the mapping systems I know of are implemented.

#### Why do I care about this?
This week's obsession is conversational interfaces. A lot of the things we do with computers rely on graphical interfaces to communicate. This means that they can offload a lot of the processing to the visual cortex by displaying a map.

Conversational interfaces are like talking on the phone so there's no way to cheat, they need to offer actionable options. In this case, where to refil my snack-tank!

# What things does the map AI need to think about?

#### Where I am (Point A)
This one is simple, GPS has you totally covered here.

#### Where I'm going (Point B)
Things like Google Maps have a pretty solid grasp of all the places you could want to go. They know their coordinates and they know their opening hours. What they don't warn you about yet is if you are going to get there after they close; it'll just merrily send you on a route to get there at five past six as they are walking out of the door.

#### Places that can service the desire
Let's stick to the plan here and get coffee and a doughnut! I need to filter for all the businesses that sell coffee _and_ doughnuts. This also isn't that hard, but it will take a fair but of work on the part of business owners to keep their offerings updated. Foursquare, Yelp and Google will ask a bunch of questions about a place that you've been to or reviewed.

<figure>
![Two screen shots of Google asking questions about a place](https://s3.amazonaws.com/images.seroundtable.com/Local-Guides-Riddler-2-1434109843.png)
<figcaption>
Google [asks people about places they've been](https://www.seroundtable.com/google-maps-places-poll-20433.html), presumably to build up a more accurate idea of what the world is really like than they can get from business owners alone.
</figcaption>
</figure>

#### Places that I'd like
Up to this point has been pretty straight forward, OG database stuff. All we're doing is putting points on a map. The next thing it to work out if I'll like any of those places. I have preferences, and communicating them to an AI would be really hard if I had to do it manually. My revealed preferences are probably more useful to an AI; Google Now already asks me if I am in a certain place or not. 

I've been thinking for a while that a social pressure to review will emerge eventually. This is enforced by Uber because you can't book your next one without reviewing the last one, but it doesn't account for taste, Uber just wants to make sure that you got acceptable service. In [Building Web Reputation Systems](http://shop.oreilly.com/product/9780596159801.do) they talk about how almost all reviews on a five star system come out as 1s or 5s so you don't get much nuance[^2]. This is something that we need to get over because if we all rate 5* then there's no way to say _this place is fine, but it's not for me_. If we can do that then the AI can start to build us into tribes[^3] and recommend places that other people in our tribe liked.

#### Is it on the way?
This is much less nuanced and is just a straight up computing problem. My guess is that you'd want to do it in a few steps. 

<figure class="half-width right">
![An ellipse from the two focal points drawn with a string](http://i1.wp.com/blog.zacharyabel.com/wp-content/uploads/2012/09/string-anim.gif)
<figcaption>
This has always amazed me. [This page](http://blog.zacharyabel.com/2012/10/what-makes-ellipses-ellipses/) has some nice diagrams on how it works.
</figcaption>
</figure>

To cut down the field you could do a geometric cull. A basic one would be a circle, but that doesn't fit in with deviation from a path very well. I think an ellipse does a pretty good job of this. If A and B are the focal points of the ellipse, then anywhere inside that ellipse is within a given amount of deviation from the path. The path is unlikely to be a straight line, so it'd need to be a squished ellipse that follows the path of the route. You can then throw out all the places that are outside that shape.

Now we've cut down the field to all the places that I'd like to go and that are within a rough cut of where I'm going we can start to do detailed checks.

Let's say that [Cartems](http://cartems.com/), [Luckys](http://www.luckysdoughnuts.com/) and [Cin City](http://www.cincitydonuts.com/) are inside the shape. If we do a proper route analysis we see that there's a big chunk of water between me and Cin City, so that's that out of the way.

#### Reel me in

Now it's up to my preference, the system can present me with two options. Maybe the two places could battle it out to try and attract me now that I've stated an [intent](https://en.wikipedia.org/wiki/Intention_economy) to drink coffee and eat doughnuts by offering me deals!



[^1]: Maybe I'll try out the Amazon self publishing thing too. It feels like it's just bible belt erotica and stories about cats, but I'm probably hugely biased.

[^2]: I've got a idea to deal with this in the future, but I'll get to that another day. The short version is that 5* is the same as a good baseline. To unlock stars 6 to 11 you need to pay money as a tip to the Uber driver on some kind of exponential scale.

[^3]: The AI could also do this by just looking at our patterns, we're unlikely to go _back_ to a place that we didn't feel like we fitted in.
