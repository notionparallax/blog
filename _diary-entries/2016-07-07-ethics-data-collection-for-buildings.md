---
layout: post
title: Ethics of data collection for buildings
date: 2016-07-07 12:00:00 PDT
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

This is a topic I've thought about a lot, but know very little of the formal issues surrounding it. I had a coffee with [Rhys Goldstein](https://www.autodeskresearch.com/people/rhys-goldstein)[^1] today and he had the idea that a framework for collecting data about building occupants and their behaviour would be really valuable. It would make it possible to combine data from different environments and build up patterns across different situations. Currently there isn't a standard which means that the data can't be readily combined. Rhys has some great papers from around 2010 where they simulate user behaviour, but further progress in that area is held up behind a dearth of real data.

## The ethical mandate

I don't have a grounding in medical ethics, but to me the way that buildings are designed today feels a bit like the way barber-surgeons practised medicine. There is a vague understanding of the way that the system operates, an accumulated set of heuristics of what's worked and what hasn't (but no general principles to back that up)[^3]. We need to fast forward a couple of centuries and take advantage of the technology that has been made available as a spill over from other industries (sensing, wireless communication...) and develop a deeper understanding of the environment that building design is practised in.

It feels irresponsible to create environments for people to live and work in without having a more rigorous way to assess our designs. Buildings have very long lifespans. It's not uncommon for a building to be expected to last 50 years. It is unlikely that we would tolerate experimentation over such a long time span in other domains when a less committed method is available. Our problem is that a less committed method is not yet available, but its availability is within our grasp. We have all the pieces in place, the mathematical foundation of simulation, the immersive environments of virtual reality, the building physics and meteorology to model the way that the physical environment influences the _building_. What we don't have is the data to back up a simulation of human behaviour in buildings.

My assertion here is that we, as a field concerned with the human aspects of building design, are being negligent in not addressing the lack of data that makes it impossible to do good occupancy simulations. Following from that, we ought to do something about it, but it's not obvious how to start. This is what I'll try and work out below.

## What I'd like to come up with

This is a multi-pronged problem. 

### How do we collect enough data to be able to say that we have a good understanding of a person?

People are complicated and need many dimensions to describe their lives fully[^2]. How many of those dimensions do we need to collect data on to make a _good enough_ representation of their behaviour. Is there some kind of Pareto ratio that 20% of the things we _could_ measure give us 80% of the world that we care about?

What data do we need to collect and what format should it be in? Acknowledging that future people will want to collect more and different types of data, how would they go about extending that standard? 

### How do we protect that person from undue privacy incursions
It _seems_ as if individuals have quite a complex attitude to data privacy. People are often hostile to efforts to collect more data about them, but are rarely motived to find out about what is harvested without their knowledge.

### How do we reimburse the measured person?
The person being tracked is transferring value to another party. 
Is it just that they get to live in a better world?

The first two of these are in tension, and the third brings an uncertain economic angle into the equation.

## Problems
* Not all collection runs will collect all types of data
one of the problems that this is trying to overcome is that each research team is recording their data differently. We need a way to standardise the collection methodology or the data format so that different groups can combine their results to provide a larger corpus.
* Providing anonymity to users (those being tracked) is at odds with collecting detailed data
* Collecting demographic data (e.g. ethnicity, gender, income etc.) is likely to be seen as overly intrusive, but without it there is no way to ensure diversity in the data.
* These data are of benefit to everyone, but how can it be sufficiently anonymised to protect the privacy and safety of the individuals?

## Precedents
Carbon Buzz is a project that collects private data about building energy usage. The platform will do queries like 



[^1]: I had a very nice Brazillian coffee from Square Mile roasters, he had a green tea. It sounds a bit strange to say "mixed hot drink meeting".

[^2]: I don't have a reference for that, but I don't think it's likely to be disputed too much.

[^3]: There's also a protectionist sense that anyone criticising the methodology must by definition be hostile and stopped.