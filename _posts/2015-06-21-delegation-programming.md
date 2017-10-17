---
layout: post
title: Delegation == Programming
date: 2015-06-21 05:27:31.000000000 +10:00
type: post
published: true
status: publish
categories: []
description:

dsq_thread_id: '4503553673'

---

I think that delegation to another person is analogous to programming a computer. I want to explain why I think this, and how thinking like this can be useful.

Programming as a discipline has developed loads of ways of making code better. That might mean more efficient, easier to understand, easier to maintain etc. The general term for this tidy up process is _refactoring_. If you think of delegation as a function call to a human then you can refactor the way you do things to make them better.  

<img class=" size-full wp-image-1773 alignright" src="{{ site.baseurl }}/assets/shared-understanding.png" alt="shared understanding" /><img class=" size-medium wp-image-1774 alignleft" src="{{ site.baseurl }}/assets/shared-understanding-human-comp.png" alt="shared understanding human comp" />Lots of tasks are too big for one person to do. Most orgs use some kind of hierarchical model to get these kinds of big jobs done. This means concentrating power and responsibility in the hands of one person who then breaks the job up into tasks. They then assign those tasks to someone else to do.

Saying _someone else_ is a lazy way of saying _entity with the capacity to get the task done_. That might be a future version of themselves, or another person, or a donkey or a computer. All that matters is that there are two entities that are capable of developing a shared understanding. Once that understanding is in place the other entity can go off and do the task.

If we explore that in a few ways:

* Alice and Bob discuss how to achieve the goal of drinking a cup of tea. Alice delegates tea making to Bob. Bob makes the cup of tea and brings it back to Alice.
* Charlie wants to do some arithmetic. He punches some numbers into a spreadsheet and gets an answer back.
* Daisy works at a nuclear plant. The control computer spots an irregularity and sends Daisy off to look at it. Daisy brings a report back to the computer.
* The _edit_ function in a word processor calls the _format_ function. It then returns some formatted results.<img class=" size-medium wp-image-1775 aligncenter" src="{{ site.baseurl }}/assets/comp-masters.png" alt="comp masters" />

<img class=" size-medium wp-image-1776 alignright" src="{{ site.baseurl }}/assets/org-tree.png" alt="org tree" />None of these are perfect examples, but they give you the idea of one agent getting another agent to do something for them. Usually this is more like a chain, where one person delegates down the chain to get things done[1. realistically it's _much_ more complicated once you need to interact with customers etc. Triggers come from all over the place, but they can probably be abstracted away with subsystems. The more important question is if that's a good idea. This is just one way of thinking, a <a href="https://en.wikipedia.org/wiki/George_E._P._Box#Quotes">wrong model</a> if you like.].

Programming a computer is just delegating to it using a tightly controlled set of commands. In human-human interaction we use empathy to substitute for precision. Computers are short on empathy, but good at precision and attention to detail.

Computers will do whatever you ask them to do, but only what you ask them to do. They are very fault prone. If you ask them to do something and you haven't given them an explicit instruction for what to do if it goes wrong, they'll stop. If you have managed to program them to do your bidding they'll continue to do that flawlessly for as long as you like!

People are incredibly fault tolerant. They can find all kinds of ingenious ways to complete their tasks in the face of adversity. The problem is that they lack precision, so getting to a shared understanding is difficult.[1. <a href="https://github.com/Dawil">Dave</a> thinks that the precision problem is too great. This might as well be a problem of kind not degree as compilers can't handle the ambiguity. I'm more optimistic and think that we'll develop a way that we'll be able to do natural language programming soon.]

All kinds of delegation need some kind of shared understanding. A computer does this by having libraries of functions and people do it by having common life experiences. If two humans have a common language they can communicate commands incredibly tersely. A great example of this is ER staff communicating a patient's state and what they need to do next. This common language takes a long time to develop and it is like learning the commands in a programming language. If people don’t share an explicit set of commands then the ambiguity is a problem but not an insurmountable one. It just needs the two people to negotiate more[1. a lot of the problems I see in life come from people not developing enough shared understanding. I've just started reading about this a bit in <a href="http://shop.oreilly.com/product/0636920033851.do">User Story Mapping</a> by Jeff Patton.].

If we can agree on most of that then maybe we can agree that **delegation is analogous to programming**.

A more difficult task might be convincing you that thinking this way is a useful mental tool. My reasoning goes like this:

1. Most tasks can be decomposed and then delegated, often recursively.</li>
1. Eventually some part of that task will be automatable.</li>


This isn't very complicated. The useful part comes when you think about a _frontier of automation_. As technology gets more sophisticated that frontier keeps moving closer to the initial delegator.

Once you have the idea of a frontier of automation you can blur it a bit. There are things that you:

* can do and a future version of yourself will do them
* can do, but it'd be better if someone else did them
* can't do so someone else needs to do them


The second two are prime for delegation. Using the mental tools developed by programmers you can think about how to best get things done.


[^1]: realistically it's _much_ more complicated once you need to interact with customers etc. Triggers come from all over the place, but they can probably be abstracted away with subsystems. The more important question is if that's a good idea. This is just one way of thinking, a <a href="https://en.wikipedia.org/wiki/George_E._P._Box#Quotes">wrong model</a> if you like.

[^2]: <a href="https://github.com/Dawil">Dave</a> thinks that the precision problem is too great. This might as well be a problem of kind not degree as compilers can't handle the ambiguity. I'm more optimistic and think that we'll develop a way that we'll be able to do natural language programming soon.

[^3]: a lot of the problems I see in life come from people not developing enough shared understanding. I've just started reading about this a bit in <a href="http://shop.oreilly.com/product/0636920033851.do">User Story Mapping</a> by Jeff Patton.

