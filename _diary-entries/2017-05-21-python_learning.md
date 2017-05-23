---
layout: post
title: Python Course
date: 2017-05-09 00:00:00 AEST
type: post
published: true
status: publish
categories: []
tags: []

## this goes on the index page, and into facebook shares
description:

## This is what twitter will pick up if someone tweets the link to this page
## 110 marker 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
twitter-body:
## Twitter and facebook will pick up this image. you can also use it in a post with:
## ![alt text]({{ site.baseurl }}/assets/{{page.featuredimg}})
featuredimg:
---

## Why do people need to be able to use Python

  * We use spreadsheets a lot. Often transforms that we'd like to do in a spreadsheet are much simpler to express as python code than as a spreadsheet formula. E.g. I find this a lot easier to read:
  ```python
    if thing == 10:
        return "something"
    elif thing == 20:
        return "something else"
    elif thing == "balcony":
        return "yet another thing"
    else:
        return "the last option"
   ```
  than this:
  ```
  =IF(A1=10, "something", IF(A1=20, "something else",  IF(A1="balcony","yet another thing","the last option")))
  ```
  And this is a pretty straightforward example!

  There are also things that just can't be expressed in a spreadsheet, no matter how hard you try!
  *   Being able to program is a good mental skill, it promotes clarity and logical thought, and makes people patient.

## How to get as many people as possible at BVN able to use python?
So, a few prior observations:
* people generally seem interested
* people don't want to give up their lives outside the office (no evening classes)
* people have unpredictable and unavoidable commitments (meetings that show up out of the blue)

In light of that, the course should make it as easy as possible to learn in a way that's untethered from being in a specific time and place.

# The CODE1161 base

There is already a baseline course to be modified, I've run through the whole course 3 times. Once at UNSW with the 1<sup>st</sup> year CODE students and twice with an open audience of (mostly) professionals. (A lot of Arup and TTW people.)

## Lectures
The content from 1161 can be broken up into fairly short video lectures.

## Exercise sets
There are also 5 week's of exercises that will be broken up into topics, and collected into smaller courses to give people smaller, more achievable goals.

People need motivation The course will be broken into:
1. Baby snek
2. Carpet python
3. Killer python
4. Data python
5. Grasshopper python
6. Project python
6. etc.

These will have something collectable like a sticker or a [sewable badge](https://www.thestudio.com/landing/australia-custom-patches-au).

## Clinics
No matter how good the videos are, there will always be something confusing for each person. There will be clinics where someone who knows python will be available to answer questions and clear up progress blockgages. These will be mostly me, but could be MarcM, DR, IJ, etc.

## Cohorts

It's hard to motivate yourself to go on a journey alone. We'll find a way to get people to self organise into cohorts to pull each other along.

# Obstacles

Getting an environment that people can program in is going to be tricky. Anaconda should do the job, but we'd need to test that it won't hurt Citrix too much (currently running fine on ARR and SS's envs). Also need to test if `pip` can run fine or if it needs special permissions.

Testing might be hard (At the very least I'd need to rewrite all the tests) [this](http://blog.thedataincubator.com/2016/06/testing-jupyter-notebooks/) might help.

Linting may be tricky too.
