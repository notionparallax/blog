---
layout: post
title: "My Dive Planner"
date: 2026-08-25 09:00:00 +10:00
type: post
published: true
status: publish
categories: []
tags: []
author-name: Ben Doherty

description: "Making a multi scenario dive planning tool"
twitter-body: "Making a multi scenario dive planning tool"
featuredimg: 
---

Every idiot with a Claude subscription seems to be making their own dive planning tool these days, so so as not to be left out, I've made one too.

The motivation for me was that every dive plan is really a bunch of dives that you don't do. There's the one you intend to do, and then there's what happens if you're slower than expected, if you go deeper than planned, if you lose a deco cylinder, etc. Working through all the variations of the plan by hand, is annoying and error prone.

I plan using [Subsurface](https://subsurface-divelog.org/) on my desktop, and the [Divesoft app](https://www.divesoft.com/en/app) on my phone, and I trust them to produce a deco plan. But all the apps I've seen do a single plan at a time, which means a lot of paperwork and iteration. I wanted a single table that runs the main plan and every contingency side by side, tuned to my team's conventions, and something I could send them as a link.

This started as a CLI tool, but I got a bit sick of that and put a UI on it. So far, it doesn't have a name, so if you have a brilliant plan for one, let me know.

## A load of scenarios

The app runs several scenarios at once from the same starting parameters — main plan, longer, deeper, deeper-and-longer, lost lean deco gas, lost rich deco gas, a bounce dive, and a fast-ascent emergency — and finds the longest bottom time where all of them still finishes with the diver alive.

The _auto bottom time_ feature is a binary search across bottom time, but it isn't searching for the point where the main dive runs low on gas — it's searching for the point where the worst-case scenario does. Every candidate bottom time gets checked against all the contingencies simultaneously, and the answer only counts if all of them clear the minimum gas reserve. Whichever scenario comes closest to failing gets a 🖐️ marker on its column header, so you can see which specific risk is limiting the dive.

![Reading timeline]({{ site.baseurl }}/assets/26/08/dive planner screenshots\whole_app.png)

You can add, remove, or edit the scenarios to change which gas goes missing, adjust the depth or time offset, toggle whether a scenario counts towards the auto-timer search, change the gradient factors. Everything else that feeds that table. Gas mixes, cylinder sizes, gradient factors, ascent and descent rates, SAC rates, gas switch depths are configurable too, and the whole configuration lives in the URL. In theory the dive plan is a shareable link, but that's a bit flaky at the moment

![Reading timeline]({{ site.baseurl }}/assets/26/08/dive planner screenshots\scenarios.png)

## life support mathematics

As noted above, I'm an idiot, and idiots shouldn't be left unsupervised with algos that support life. None of the decompression maths is mine. Under the hood it's using the python library [DecoDaiTengu](https://github.com/notionparallax/decodaitengu)[^tengu].

[^tengu]: [DecoTengu](https://github.com/notionparallax/decodaitengu) is a python library that uses the Bühlmann ZHL-16C model with Erik Baker's gradient factors, but it was last touched in 2018 so I forked it and modernised it a bit (Python 3.12, full type hints, dataclasses, `mypy --strict`) The fork is called DecoDaiTengu. That's separate story of its own. (Not a very interesting one)

I built this fast, with a lot of help from Claude Code — [Streamlit](https://streamlit.io/) made the UI side really quick to iterate on. But before I trusted the deco algos, I checked the underlying half-time and M-value tables against the published ZHL-16C values, and cross-checked full dive plans against Subsurface's independent planner at matched depth, time, gradient factors, and SAC rate, and the plans come out pretty much the same as Subsurface's.

## Caveats

This is a hobby project, not certified dive planning software. It has been battle tested a bit though: I used it to generate the team's dive plans on my trimix course, and it held up. That said, I would definitely recommend cross-checking any plan it gives you against something else before you trust it underwater, and don't take "the app said so" as a substitute for training.

## Have a go

The app is live at [diveplanner-demo-page.streamlit.app](https://diveplanner-demo-page.streamlit.app), and the code is [on GitHub](https://github.com/notionparallax/dive_planner). I'd like to hear from actual tech divers on whether the contingency scenarios match how you already plan, and whether the auto bottom time result matches your gut.

## What's next?

- I'd like to get it off streamlit now that it's pretty well prototyped, as there are some UI lags caused by round-trips to the server.
- I print out plans on a [Niimbot printer](https://niimbots.com/collections/business-label-maker/products/b1-2-inch-inkless-thermal-label-printer-create-professional-labels-with-ease), it would be good to be able to automate that a bit more. (People have been getting quite excite about this kind of thing since people have been connecting the [Halcyon analyser to a zebra printer](https://niimbots.com/collections/business-label-maker/products/b1-2-inch-inkless-thermal-label-printer-create-professional-labels-with-ease).)
- This is only really useful for square-profile, open ocean dives. It is going to take quite a lot of thinking about if it's going to be useful for overhead situations with weird profile shapes.
- I'm the only one who's used this so far. I'd really like to hear from other people about if it's useful for them.
