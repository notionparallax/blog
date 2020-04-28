---
layout: post
title: "WIP: Recipe vis"
date: 2020-4-28 21:45:00 AEST
type: post
published: true
status: publish
categories: []
tags: []
author-name: Ben Doherty

# this goes on the index page, and into facebook shares
description: "Working post: How to represent cooking multiple recipes at once"

# This is what twitter will pick up if someone tweets the link to this page
# 110 marker
#123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789
twitter-body: "Working post: How to represent cooking multiple recipes at once"
# Twitter and facebook will pick up this image. you can also use it in a post with: -
#![alt text]({{ site.baseurl }}/assets/{{page.featuredimg}})
featuredimg: https://developers.google.com/optimization/images/scheduling/schedule1.png
---

# Visualising cooking a meal

I've always struggled to read recipes all the way through and visualise the order of operations. Mainly because my attention span is terrible, but also because there is going to be interactions with other things in my life; usually the other parts of the meal I'm cooking.

I'd imagine that chefs are pretty good at imagining how the sequencing of a day's work is going to go. What prep needs to be done, in what order, and how it's going to interact with the other components. There's also the advantage of getting another go at it; Home cooks don't do so well because usually it's the only time you'll ever cook a dish. [Chris Young][cy][^cyfn] said in an interview that the best thing for a home cook to do to level up their cooking was to not cook things for the first time on the day of the dinner party.

Anyway, most recipes say "Here's how to cook really good roast potatoes" which is great if you want to only serve your guests roasties, but if you want to roast a chicken too, your oven becomes a bottleneck in your production. This sort of thing makes cooking at home tricky because home cooks aren't skilled in planning this sort of stuff. Short of having a cup of tea and writing lists, how else could we support home cooks who are planning a dinner party (or just dinner) to get things to the table at the right time?

Eventually, I really should go and talk to some people who are actually good at this sort of stuff, but while I'm trapped in my house, let's take an abstract approach to the problem.

## Questions:

- Information structure (is this the right term?)
    - How do you plan the interaction between your recipes?
    - How do you plan the interaction between the cook[s] and the things they're making?
    - Can the recipes be broken into components?
    - Can components be interrupted? I can stop chopping a carrot to take something out of the oven if a beeper goes off. What's the task switching cost?
    - What tolerances are there? E.g.:
        - Can I make this component ahead of time? How far ahead? 
        - Can this cook for 40 minutes instead of 35?
    - Can components share equipment? E.g. there's a [ChefSteps eggs benedict recipe][eb] where everything gets cooked at 64°C. That means that you can do everything in the same pot with one circulator. The "[Perfect Hollandaise][ph]" recipe asks for 75°C, but that would need an extra circulator for the eggs.

        <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/HDmP0zZMw1Y" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        vs
        <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/9DLRL2shlPI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        - Does those shared pieces of equipment have limits? I can only put so many trays in the fridge (space), so many cookies in the oven (power).
- User
    - Does the representation actually make it easier to understand and plan a cook?
    - Is there a lot of user specific information? Can cook _A_ mince a shallot faster than cook _B_? (Do we end up with a bunch of comparative advantage issues here?)


## First thoughts

I think that Gantt charts, _a la_ Microsoft Project, are more about organisation theatre than an actually useful tool. [Tufte][ta] agrees. But, if you flip the chart so that instead of each task going in it's own row, like an endless waterfall of misery, each resource gets a row, then you can see some useful interactions.

![](https://developers.google.com/optimization/images/scheduling/schedule1.png)

The diagram above is pinched from the docs for Google's OR-tools [Job shop algorithm][jsa]. [Job shop scheduling][jss] is the most promising algo/concept that I've seen that applies to this problem. The only problem being that the _jobs_ have a lot more metadata than the basic examples that I've seen. There are some papers that discuss the addition of operators to the problem, so they're probably helpful ([e.g.][jswo]). I'll consult the CS brains.

## Prototype vis

TODO: draw out a couple of simple recipes to see how it looks.
Put an operator rail along the top for person one, and along the bottom for person 2, maybe through the middle for a third person?

The people can be linked to the tasks on equipment rails.




[jswo]: https://www.google.com/search?q=job+shop+algorithm+with+operators&rlz=1C1CHBF_en-GBAU804AU804&oq=job+shop&aqs=chrome.0.69i59l2j69i57j0l2j69i60j69i61l2.2023j0j7&sourceid=chrome&ie=UTF-8
[jss]: https://en.wikipedia.org/wiki/Job_shop_scheduling
[jsa]: https://developers.google.com/optimization/scheduling/job_shop
[ta]: https://www.edwardtufte.com/bboard/q-and-a-fetch-msg?msg_id=000076
[ph]: https://www.chefsteps.com/activities/perfect-hollandaise
[eb]: https://www.chefsteps.com/activities/can-t-f-it-up-eggs-benedict
[^cyfn]: I think it was when he called in to Cooking Issues, but I wouldn't trust anything I say!
[cy]: https://twitter.com/chefchrisyoung