---
layout: post
title: Perfect TODO
date: 2014-05-23 08:51:33.000000000 +10:00
type: post
published: true
status: publish
categories: []
tags:
- TODO
description:
meta:
  _publicize_facebook_user: https://www.facebook.com/ben.doherty1
  _publicize_twitter_user: "@notionparallax"
  

  dsq_thread_id: '4503553461'

---
<p>I've been faffing about with different todo lists for years now. I've used everything from a <a href="http://www.43folders.com/2004/09/03/introducing-the-hipster-pda">hipster pda</a> to some pretty hardcore project management tools. I even used MS Project to get me fired from Autodesk! The one thing that was common amongst them all is that they niggled me because they didn't do everything I wanted. Often a lot of things that I didn't want.</p>
<p>Most of the time when I ask productive people about what they use I get the unhelpful answer:</p>
<p>"I use x tool and y system, the features you want are unhelpful. You should just follow the system better."</p>
<p>This might work well for them, but my brain doesn't really work that way. I need support for my habits and no amount of system will keep me on track if I don't have a framework to hang it on. [1. most people seem to work the other way around - they have a system in their heads and their tool is just a minor way of offloading the hard work to it. I really need a system to tell me what I should be doing!]</p>
<p>&nbsp;</p>
<p>The job of the list falls into two broad camps, being an external brain so that you don't forget things, and helping you decide what to do next.</p>
<p>&nbsp;</p>
<p>Here's a few ideas on what I'd like to see in a tool to help me get things done.</p>
<h2>Modularity</h2>
<p>I ummed and ah’d about putting this at the start or the end. I settled on start so that you can hold this all in your head as you go along. Few of these things are core capabilities, not everyone will want them all, and there’s no way that I’ve thought of all the features that everyone would want. The key thing about this proposed perfect system is that it would be modular; that way no component of if would be required. In fact, I think that the only common thing would be the message passing protocol or the api. That way you could swap out any part of it you liked for one that better suits your needs.</p>
<h2>Stats on what gets done</h2>
<p>If you've spend a day crushing through tasks it'd be nice to have some way of reminding yourself just how productive you've been. This is handy for keeping motivated, but I think the real value in this kind of thing is that it allows you to see your task habits. If you put a task onto list x it tends to get done that day, and tasks put on list y tend to never get done. If you took the analysis a bit further, you could do text analysis on the task descriptions. Maybe elaborately described tasks take about a week to do, tasks with lots of subtasks about a month etc. That kind of analysis might make it easier to see how you should be thinking about your tasks.</p>
<h2>Publish tasks with friends (I need x from supermarket)</h2>
<p>Whenever I go to make a cup of tea at work I ask if anyone else on my bench wants one[1. This might be my English upbringing, it seems normal to me, but it freaks all the Australians out no end!]. I do the same sort of thing when I go to a shop that's a pain to get to (the supermarket, or the big hardware store). People often don't ask for anything, but it's nice to offer. The idea of this feature is that you can make a task semi public. Then if a friend of yours is going to buy a hammer drill, and you need a box of nails then they can get it for you without you needing to know.</p>
<h2>Shortcuts !1</h2>
<p>This is one of the things that makes <a href="https://www.rememberthemilk.com/help/?ctx=basics.smartadd.howdoiuse">Remember the Milk </a>great. They have a really terse DSL that allows you to completely specify a task without taking your hands off the keyboard. This is good because it makes it fast to put tasks in, but it also makes it easy to specify tasks via email or some other api.</p>
<h2>Free form tagging</h2>
<p>I want to be able to tag freely, mainly because I think that this is something that should be enabled on everything. Not for any specific reason but because freeform tags allow people to hack their own system together on top of your system. Then if it seems like a good enough idea then you can make it a full feature.</p>
<h2>Hierarchical subtasks</h2>
<p>This one seems to split the todo world. The GTD people are all about projects and then only one level of hierarchy, and others like to subdivide to the nth degree. I'm with the latter group. I find that I often have big ideas, and it's only as I start to break those ideas up that they turn into something that I can do something about. Partially because I don't understand them, and partially because if my tasks take more that 10 or 20 minutes they are too daunting for me to start.</p>
<h2>Locations</h2>
<p>This is another one that's taken from <a href="http://www.rememberthemilk.com/help/?ctx=basics.locations">RTM</a>. With the recent improvements in the geofence APIs (at least in <a href="https://www.youtube.com/watch?v=Bte_GHuxUGc">android</a>) this becomes a lot more useful. E.g. you are 200m from the supermarket, pop in and buy an avocado. <a href="https://twitter.com/albcorp">ALB</a> has some ideas about how this could be extended by adding in context and transport method, but I’ll let him expand on that one day.</p>
<h2>priority vs importance view</h2>
<p>Some people call this an <a href="http://goo.gl/iQA9on">Eisenhower grid</a>, or have different labels for the axes. THe general gist of it is that you are able to decide how urgent and important something is, and from that decide what to do next.</p>
<h2>Timeline</h2>
<p>Todo entries have temporal characteristics; this is different from the way that people think of gantt charts in that this is more descriptive than normative. Item x was put into the system on this date, modified on this date, and completed on this other date. I guess you can add deadlines for things, but I find that deadlines just make me sad as they go whooshing past.</p>
<h2>Time estimates</h2>
<p>Similarly to the timeline, this isn't a project planning idea, but one I got from ALB. He has his tasks tagged with time estimates so that if he has 5 minutes spare then he just goes to his &lt;5 minute bin and picks something to do. It also helps with day packing.</p>
<h2>Required equipment</h2>
<p>This is one that grows out of the tagging thing as a base for features. Most tasks need some sort of equipment - phonecalls need a phone, digging a hole needs a spade. If you want to decide what to do next then you could click the things that you have with you, and then filter by how long you have... which leads on to:</p>
<h2>Day packing</h2>
<p><a href="https://taskk.it/">Taskk</a> is a really cool (but fairly broken at the moment to do list manager). It gets you to put in tasks, give them time estimates and then, based on some priorities that you set, it packs tasks into the day. It's really good, except for not taking into account your appointments or the cost of switching context. If it could work these sorts of things out then it'd be really handy.</p>
<h2>Delegation options</h2>
<p>The best way to get a lot of things done is to get someone else to do it. I have a painfully under-utilised fancy hands account, if I could delegate from inside my todo list (as you can in <a href="https://trello.com/">Trello</a>) I might be more able to use it. Likewise if you run a team then delegating to them is a pretty handy thing to do too. I hear <a href="http://www.simpleology.com">simpleology</a> does this well</p>
<h2><i>Not going to do</i>/<i>irrelevant</i> as well <i>complete</i></h2>
<p>I think about half the things on my lists end up not getting done. Mainly because they stop needing to be done before I do them! I'd like to be able to be more nuanced in the way that I get rid of tasks. As I look back over things, "Done" says to me tha<p>This might work well for them, but my brain doesn't really work that way. I need support for my habits and no amount of system will keep me on track if I don't have a framework to hang it on. [^1]</p>
<p>&nbsp;</p>
<p>The job of the list falls into two broad camps, being an external brain so that you don't forget things, and helping you decide what to do next.</p>
<p>&nbsp;</p>
<p>Here's a few ideas on what I'd like to see in a tool to help me get things done.</p>
<h2>Modularity</h2>
<p>I ummed and ah’d about putting this at the start or the end. I settled on start so that you can hold this all in your head as you go along. Few of these things are core capabilities, not everyone will want them all, and there’s no way that I’ve thought of all the features that everyone would want. The key thing about this proposed perfect system is that it would be modular; that way no component of if would be required. In fact, I think that the only common thing would be the message passing protocol or the api. That way you could swap out any part of it you liked for one that better suits your needs.</p>
<h2>Stats on what gets done</h2>
<p>If you've spend a day crushing through tasks it'd be nice to have some way of reminding yourself just how productive you've been. This is handy for keeping motivated, but I think the real value in this kind of thing is that it allows you to see your task habits. If you put a task onto list x it tends to get done that day, and tasks put on list y tend to never get done. If you took the analysis a bit further, you could do text analysis on the task descriptions. Maybe elaborately described tasks take about a week to do, tasks with lots of subtasks about a month etc. That kind of analysis might make it easier to see how you should be thinking about your tasks.</p>
<h2>Publish tasks with friends (I need x from supermarket)</h2>
<p>Whenever I go to make a cup of tea at work I ask if anyone else on my bench wants one[^2]. I do the same sort of thing when I go to a shop that's a pain to get to (the supermarket, or the big hardware store). People often don't ask for anything, but it's nice to offer. The idea of this feature is that you can make a task semi public. Then if a friend of yours is going to buy a hammer drill, and you need a box of nails then they can get it for you without you needing to know.</p>
<h2>Shortcuts !1</h2>
<p>This is one of the things that makes <a href="https://www.rememberthemilk.com/help/?ctx=basics.smartadd.howdoiuse">Remember the Milk </a>great. They have a really terse DSL that allows you to completely specify a task without taking your hands off the keyboard. This is good because it makes it fast to put tasks in, but it also makes it easy to specify tasks via email or some other api.</p>
<h2>Free form tagging</h2>
<p>I want to be able to tag freely, mainly because I think that this is something that should be enabled on everything. Not for any specific reason but because freeform tags allow people to hack their own system together on top of your system. Then if it seems like a good enough idea then you can make it a full feature.</p>
<h2>Hierarchical subtasks</h2>
<p>This one seems to split the todo world. The GTD people are all about projects and then only one level of hierarchy, and others like to subdivide to the nth degree. I'm with the latter group. I find that I often have big ideas, and it's only as I start to break those ideas up that they turn into something that I can do something about. Partially because I don't understand them, and partially because if my tasks take more that 10 or 20 minutes they are too daunting for me to start.</p>
<h2>Locations</h2>
<p>This is another one that's taken from <a href="http://www.rememberthemilk.com/help/?ctx=basics.locations">RTM</a>. With the recent improvements in the geofence APIs (at least in <a href="https://www.youtube.com/watch?v=Bte_GHuxUGc">android</a>) this becomes a lot more useful. E.g. you are 200m from the supermarket, pop in and buy an avocado. <a href="https://twitter.com/albcorp">ALB</a> has some ideas abou<p>I think about half the things on my lists end up not getting done. Mainly because they stop needing to be done before I do them! I'd like to be able to be more nuanced in the way that I get rid of tasks. As I look back over things, "Done" says to me tha

[^1]: most people seem to work the other way around - they have a system in their heads and their tool is just a minor way of offloading the hard work to it. I really need a system to tell me what I should be doing!

[^2]: This might be my English upbringing, it seems normal to me, but it freaks all the Australians out no end!

