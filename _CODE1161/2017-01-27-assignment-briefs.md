---
layout: post
title: The Assignments
date: 2017-01-27 00:00:00  PDT
type: post
published: true
status: publish
categories: []
tags: []

#this goes on the index page, and into facebook shares
description: Course admin and a tiny bit of syntax

# This is what twitter will pick up if someone tweets the link to this page
# 110 marker 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
twitter-body:
#Twitter and facebook will pick up this image. you can also use it in a post with:
# ![alt text]({{ site.baseurl }}/assets/{{page.featuredimg}})
featuredimg:
---

**Assignment 1**

* [a--Lab-Book](#part-alab-book)
* [b--Weekly Programming Exercises](#part-bweekly-programming-exercises)
* [c--Exam](#part-cexam)

**Assignment 2**

* [Holy Wars](#assignment-2holy-wars)

**Assignment 3**

* [a--Open Data Project](#part-aopen-data-project)
* [b--Git collaboration](#part-bgit-collaboration)


# Assignment 1

## Part a---Lab book

Each week you should publish your notes from that week. This is quite a big change to the way you've probably worked in the past, but you'll find it incredibly valuable.

This is what it says in the course outline:

> A lab book is a record of what you&rsquo;ve learned, what you are going to try next and a reference for next time you encounter the same problem. Students will assemble one document per week that they will post to the course&rsquo;s Medium publication ([medium.com/code17](https://medium.com/code17)).
> This will cement concepts by writing about, and illustrating, them. There is also value in reading and commenting on other students&rsquo; lab books as a way of distributing the effort of learning.
>
> **DELIVERABLES**: 14 Medium blog posts. These will be marked in two parts. Half the mark is for weekly presence; is there something posted by 7pm on Thursday? The other pass will be for quality which will happen in one go in week 15, which will give time for tidying up and refinement.

I find that the best way to do a lab book entry is to open a file, either in your editor or in Medium, and keep it open all week. (Save often!) Whenever you have an idea, or you get stuck on something, or you see something cool, write about it.

In practice, imagine that you are writing some beautiful code, but one part of it looks a bit inelegant. You could write that down. You could also make a note of what you found that helped you make it better. You can record links to the Stack Overflow posts that you referenced, or to some blog posts.

You can (and should) also use it for general musings. Perhaps you notice that the law would be better if it was [written](https://techblog.bozho.net/writing-laws-is-quite-like-programming/) as a [programming](http://jeremy.zawodny.com/blog/archives/009421.html) [language](https://www.quora.com/Would-the-legal-system-benefit-from-using-a-programming-language), or you read about some new thing in quantum computing, or that you renamed a whole folder of files with a python script. Maybe even just your thoughts on the world in general. It's always nice to go back in time and see what thoughts you were having together.

There are also specific things that we'll ask you to put into your lab book. There is going to be some discussion of data ethics, and there will probably be other things along those lines too.

The medium app ([iOS](https://itunes.apple.com/ca/app/medium/id828256236?mt=8), [Android](https://play.google.com/store/apps/details?id=com.medium.reader&hl=en)) makes it really easy to post from anywhere, so you could be on the bus or the beach and still posting. It's also easy to put in pictures. So _do_; lots of them! Draw diagrams in your sketch book and photograph them, take screen grabs, take photos of the world, then put them all into your lab book.

The way the marking for this works is that each week is worth 1% of your total mark. You get that mark _just_ for posting something. The other 14% is for the quality of your whole lab book. That part is assessed in week 15.

Writing down your thoughts is really valuable. We have a rule at work that we're not allowed to get stuck on a problem for more than an hour. If it gets to an hour then we write it up, usually as a Stack Overflow question. That said, we only post about <sup>1</sup>&frasl;<sub>5</sub><sup>th</sup> of the questions because the act of writing them makes the problem clear enough to solve it.

This is worth a whopping 28% of your marks! Doing a good job of this will be good for your mind and good for your marks.

## Part b--Weekly Programming Exercises

For the first part of the course there will be structured exercises for you to complete.

Again, this is what it says in the course outline:

> Each week until the mid semester break there will be tasks for you to complete. These will be briefed during the contact time. These are marked automatically, but the code used to mark them will be available to you so you can tell if your work will pass or not.
>
> DELIVERABLES: Each week at the cutoff time (7pm the following Wednesday) each student&rsquo;s GitHub repository will be parsed by a script and the code present will be marked. It will either pass or fail the tests. Feedback will be given in a communal way through the discussion forum. (No submission in week 7.)


_TODO: check this with real tests_

These exercises are very dependent on GitHub. Each week you'll update your fork with the latest version of the course repo using `git fetch upstream` ([as described here](https://help.github.com/articles/syncing-a-fork/)). That'll have the latest version of the exercises in it.

A typical exercise will have a function stubbed out, e.g.:

``` python
    def exercise1(dog, cat, pig):
        pass
```

and then below that there will be another function that tests that function. You should be able to run the code right away and it'll fail all the tests.

``` python
    def test_exercise1(dog, cat, pig):
        expect = "Spot, Felix and Babe all had tea"
        if exercise1("spot", "felix", "babe") == expect
            print "good job - " + expect
```

Your job will be to make the function pass all the tests. This will be an exercise in writing code, but also in reading it. The tests will tell you all about what is expected from that function.

These will be marked at 7pm on Thursday of the following week. It'll be automatic. You push your changes to _your_ repo, then I'll pull them down onto my machine. If the tests pass on my machine then you'll get the mark. If they don't then you won't.

## Part c--Exam

Just to check that you can do this stuff under pressure, there will be an exam!

> This will test recall on basic principles and your ability to apply them. The subject of the questions will be given ahead of time, but the specifics will only be revealed on the day.

The exam will work exactly like the weekly exercises, except we'll only release the actual tests at the start of the exam, and the cut off will be at the end of the exam.

# Assignment 2--Holy wars

<figure>
![Real programmers set the universal constants at the start such that the universe evolves to contain the disk with the data they want.](http://imgs.xkcd.com/comics/real_programmers.png)
<figcaption>
[Real Programmers](http://xkcd.com/378/), from xkcd
</figcaption>
</figure>

> A very deep dive into a specific aspect of programmer culture.
>
> There are deep divisions in programmer culture over seemingly trivial things. For example, the advocates of different text editors treat their allegiance with a religious fervour. Each student will pick one of these divisive topics and present it to their peers during the week 5 lab. the marks will be evenly split between defining the context, presenting both sides of the argument with balance, and stating their position on the matter and substantiating why they hold that belief.
>
> **Deliverables:** A 5 minute presentation in the week 5 Lab. A 20 slide presentation in Google slides format. Each slide should be set to have a 15 second automatic timer. The slides should be shared no later than 1pm on Thursday week 5. Details on sharing will be given closer to the date.

That says most of it already!

Here's a list of topics for you to pick from:

* Vi vs Emacs
* One True Brace vs K&R

    ```js
    if() {
        code
    }
    ```
  vs
    ```js
    if()
    {
      code
    }
    ```
* Tabs vs Spaces
* Why python's lambda is bad or good
* Semicolons, yes or no
* double space after a full stop
* Cherry brown vs Cherry blue
* Imperative vs functional
* IDE vs text editor
* Standing vs sitting
* Pair programming or not?
* Agile vs waterfall
* 40%, 60% or full sized keyboard?
* Long variable/object names versus short and/or abbreviated names
* Mountain Dew versus Coffee
* _j_if vs _g_if
*

You should record all your references and put them on the slide that they relate to. That'll mean that we can go through your slides and see where you've got your information from.

Google slides doesn't give you the option of timing the slides, but we _can_ time them once we have them all. There will be 90 seconds between the presentations for change over and questions, then the next one will start playing.

You'll actually submit 21 slides, the first one will have your name and student number on it. This will give you some time to grab the mic and steady your nerves; you'll need to be ready before though, 15 seconds isn't enough warning to get from your seat to the front. There will be a running order sheet available on the day.

Looking at the assessment criteria:

1. #### The submission fits the specification

    This is pretty self explanatory. Don't throw away marks here. Make sure you have a 21 slide Google slides presentation, where slide 1 is your name and student number. Make sure that it's shared well in advance of the cut off.

    **If you don't get this bit right, you can't get any marks for the remaining parts of the assessment.**

1. #### Defining the context

    What does this mean? Why is this even an issue? Why isn't there agreement? Present the context of the question. E.g. for Vi vs Emacs, say that they are both text editors, assume that your audience knows absolutely nothing about this topic.

1. #### Presenting both sides of the argument with balance

    We shouldn't be able to tell what your position is yet, that should come as a surprise in the next section. For now, present both sides of the argument as well as you can, as if you are arguing _for_ both sides.

1. #### Stating a position on the matter and substantiating why that belief is held

    Now you can break out your position. Tell us why you believe what you do. Back it up with references and examples too.

The key to this assignment is to enjoy yourself and to nerd out in a big way. It's only by understanding the depth of these sorts of arguments that you can appreciate the culture that you are entering.

# Assignment 3
## Part a--Open Data Project

> This is the capstone project for this course. You will take an open data set, probably from the NSW government collection and build a way to present it to others.
>
> You will use any available libraries or frameworks to do so, although py.processing and matplotlib are recommended. The marks will be awarded for:
>
> * Code quality: Is the code tidy, is it modular, is it self documenting, does it use efficient algorithms etc.
> * Data manipulation: has the raw data been transformed well, and repeatably.
> * Quality of output, is the ‘front end’ of your project successful, is it supported by data visualisation and HCI principles?
> * Depth of insight: Does your system lead to a greater understanding of the phenomenon described by the data? What did you find in the data that you wanted to share with others?
> * Final presentation: was the presentation clear and well rehearsed? Did it get the salient points across? Was it technically deep while avoiding jargon?
>
> **DELIVERABLES:** A presentation and demonstration of your data exploration tool in week 14’s contact time. Your GitHub Repository will be marked at its state at 7pm Tuesday of week 15.
20% w14

15% w15

W14 presentation
W 15 submission

## Part b--Git collaboration

5%

W 15
