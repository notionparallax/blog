---
layout: post
title: A couple of things I know about my first years
date: 2017-03-02 14:00:00  AEST
type: post
published: true
status: publish
categories: []
tags: []

# this goes on the index page, and into facebook shares
description: Here's a few graphs about the first year computational design students.

# This is what twitter will pick up if someone tweets the link to this page
# 110 marker 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
twitter-body: Graphs and things!
# Twitter and facebook will pick up this image. you can also use it in a post with:
#![alt text]({{ site.baseurl }}/assets/{{page.featuredimg}})
featuredimg:  17/party_distance.png
---

The first thing everyone did in [the class](https://notionparallax.co.uk/CODE1161/2017-01-01-lecture1) was to fill in a few questionnaires. I split them up so that it'd be harder for me to reverse engineer the responses into identifiable data. Hopefully everyone got this and filled them in honestly, the responses don't _look_ like there's been a lot of trolling.

I did a couple of toy trend lines, don't take these too seriously, but they match my intuitions. It'd be good to try this type of thing on a course with 600 students!

<figure>
![distance vs party](https://docs.google.com/spreadsheets/d/1lpgfIo4A7mMpvo66w0tOsRMzr-UJHX5Ja-QEZKiR7_Q/pubchart?oid=1896688223&format=image)
<figcaption>
This backs up the intuition that being closer to uni indicates more partying
(This is a bit hard to read because Google doesn't let you pick which series to put on the y axis.)
</figcaption>
</figure>

<figure>
![marks vs party](https://docs.google.com/spreadsheets/d/1lpgfIo4A7mMpvo66w0tOsRMzr-UJHX5Ja-QEZKiR7_Q/pubchart?oid=2097846239&format=image)
<figcaption>
This one has a good chance of being totally off because most people don't have an intuitive grasp of percentiles. I've flipped the scale so the percentiles map more closely onto marks---i.e. 100 means the top mark, and 0 means the lowest[^map]. They are basically backwards; being in the top 99% sounds good, but is actually really bad. That said, if people _do_ getti, it looks like  people who party the most expect to do the best. I'd say that this is a _very_ spurious result!
</figcaption>
</figure>

[^map]: or even more technically, I've mapped the hypothetical domain of the marks onto the domain 0...100.

<figure>
![marks vs experience](https://docs.google.com/spreadsheets/d/1lpgfIo4A7mMpvo66w0tOsRMzr-UJHX5Ja-QEZKiR7_Q/pubchart?oid=1761879851&format=image)
<figcaption>
This one has a pretty clear causal mechanism, people who already know the stuff that we plan to teach in the class expect to do better. I'm a bit surprised that the effect isn't more evident.

The three dots clustered in the top right are the three of us on the teaching team, so that reduces the effect size further, maybe even to the point where there is _no_ relationship between prior experience and expected mark. It'll be interesting to see how this plays out at the end.
</figcaption>
</figure>

<figure>
![os](https://docs.google.com/spreadsheets/d/1lpgfIo4A7mMpvo66w0tOsRMzr-UJHX5Ja-QEZKiR7_Q/pubchart?oid=1332238088&format=image)
<figcaption>
I expected Macs to be in the lead, but windows totally takes first place. (I'm the 1 linux user.) I wonder if this is indicative of a bigger trend away from macOS, or do I just not hang out with enough 18 year olds to know what computers they have. (There are at least 2 surface books in the class, so it's not necessary a cost issue, people have consciously decided that win is what they want.)
</figcaption>
</figure>

<figure>
![experience](https://docs.google.com/spreadsheets/d/1lpgfIo4A7mMpvo66w0tOsRMzr-UJHX5Ja-QEZKiR7_Q/pubchart?oid=1643742134&format=image)
<figcaption>
Unsurprisingly, most people in an intro to programming course haven't done much programming! 3 of the "loads" are the teaching team.
</figcaption>
</figure>

<figure>
![living situation](https://docs.google.com/spreadsheets/d/1lpgfIo4A7mMpvo66w0tOsRMzr-UJHX5Ja-QEZKiR7_Q/pubchart?oid=43371140&format=image)
<figcaption>
As a Brit, this is a strange situation, but I'm getting used to it. Living at home is cheaper, but you don't learn the meta-skills of being an adult. How important that is I don't know.
</figcaption>
</figure>

I thought this was interesting, so I did some pivot table magic[^pt]

[^pt]: I call it magic because pivot tables are still a mystery to me.

| Accom. state | average time |
|---|---:|
|In a share house | 22.81339764|
|In student housing | 1.497822372|
|On your own | 21.68523621|
|With parents/family | 50.87675689|
|Total | 38.23998121|

People who live at home are willing to cop a significant travel burden in exchange for saving their rent money. I'd be interested to hear if this was a choice they made, or if it was just a default thing.

<figure>
![distance from uni](https://docs.google.com/spreadsheets/d/1lpgfIo4A7mMpvo66w0tOsRMzr-UJHX5Ja-QEZKiR7_Q/pubchart?oid=897075153&format=image)
<figcaption>
Although the mean travel time is 38 minutes, the mode is about 90! That might be because UNSW is a pain to get to, or it might be because people really do live a long way away.
</figcaption>
</figure>

<figure>
![colour blindness](https://docs.google.com/spreadsheets/d/1lpgfIo4A7mMpvo66w0tOsRMzr-UJHX5Ja-QEZKiR7_Q/pubchart?oid=1923603520&format=image)
<figcaption>
I'm surprised by how few colour blind people there are, and that it's one girl and one guy. Programming is a lot of looking at coloured text, so I'll have to be careful that everyone can read it.
</figcaption>
</figure>

There were a couple of open text questions too:

### Why did you do this course? <small>Tell us, be honest, I can't tell who you are.</small>

* I'd like to think that learning to "speak" programming will help immensely in the future.
* I was told about this course by a mate who really enjoyed it. Thought I'd give it a go
* Choose as a strand elective to complete my degree
* To get a degree
* It was on the sugggested course
* I like designing objects people would use.
* I am interested in IT and design
* Complete my units.
* Because I love coding
* It genuinely seemed like a course id be interested in, also since im unsure about what kind of design id like to do this seemed like a good course for figuring that out while obtaining a good skillset
* I was really interested in the design aspect of architecture
* my strand elective
* I did this course because it was a part of the computational design course and I wanted to gain a wide variety of skills that I could apply to architectural computing.
* It was a part of my bachelor degree.  I am terrible at using computers and would like to learn
* Complete my units
* only course that was interesting to me and it is the future of our world
* It's in between two highly dynamic and fascinating feilds of knowledge and is a new course tailored for the modern workforce
* I chose the course because of the flexibility for a future career and also because I dint want to do something to mainstream such as Engineering or Law or Medical.
* I chose this course because computational design covers a wide variety of design branches
* I like to design on the computer
* it was required
* Career change
* I am interested in designing as well as innovating.
* A friend of mine took it a while back. Another of my friend's tutored it a while back. They said it was good.
* I love the ability to create/design things through the means of a computer
* I liked computing and also design
* because i am very interested in design with the use of computers
* it looked like the most interesting course I was offered a place in
* I'm trying out a few CODE courses because I might switch to the program
* because i am extremely interested in the creativity and buildings that can be built with the use of technology and architecture.
* because i am interested in what product will be formed through the use of technology and the creativity through the minds of architectures.

### What does 'programming' mean to you?

* Explicitly defining a process
* To compile rules for the computer to process any of my inputs to generate some level of desired outputs.
* To define instructions specifically for a machine to execute.
* Giving instructions to the computer
* Why isnt my laptop connecting to uniwide
* The way to tell computers and machines what to do.
* To create or manipulate something digitally
* The backbone of a program.
* It means coding and using computer to do what u want
* Writing for computers.
* Telling a computer what to do
* programming is the ability to design software using a variety of computer languages
* Writing and debugging codes.
* use computer language to achieve the communication between computer and people
* The background information of software - writing code to make things function in the computer
* process of coding, designing or controlling software
* making code work
* By giving the commands to the computer for it to do something in a certain procedure
* writing and arranging code in order to create or make something
* Creating a code to tell a computer how and when to do something, almost like teaching it a lesson.
* coding in the background
* Process of teaching or presenting
* telling computers what to do
* idk lol
* Giving computer's instructions to complete a  certain task.
* Computer work; writing code that enables a function/task to be performed
* Automating
* making stuff automated
* Proscribing rules
* Coding, inventing, automating things.
* I think being able to program is like learning how to form the clay of the 21st century. Computers are ubiquitous and understanding how to best use their power I believe to be a fundamental skill.
* designing code
* using computers to solve problems
* Fun.
* solving problems with the use of digital technology
* SOLVING PROBLEMS WITH THE USE OF TECHNOLOGY
* solving problems with the use of tehcnology

I think my favourite is _idk lol_, which is probably the most honest! I think that deep down, that's what my response would be too!

I'm going to do something similar at the end of the course. It'll be interesting to see how things change!
