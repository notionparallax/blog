---
layout: post
title: How to do lecture 1's homework
date: 2017-01-05 00:00:00 PDT
type: post
published: true
status: publish
categories: []
tags: []

#this goes on the index page, and into facebook shares
description: A worked example so that your head doesn't explode!

# This is what twitter will pick up if someone tweets the link to this page
# 110 marker 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
twitter-body: A worked example so that your head doesn't explode!
#Twitter and facebook will pick up this image. you can also use it in a post with:
# ![alt text]({{ site.baseurl }}/assets/{{page.featuredimg}})
featuredimg:
---

<style>
.blink_me {
  animation: blinker 3s linear infinite;
}

@keyframes blinker {  
  50% { opacity: 0; }
}

.caret {
    display: inline-block;
    width: 0.5em;
    height: 1em;
    background: black;
    transform: translateY(0.2em) scale(1.3);
}
</style>

Open the terminal and let's get going!

This is what my terminal looks like when I open it:

`ben@um:~$` <span class="blink_me caret"></span>

To break that down: `ben` is my computer name and `um` is my machine name. I'm in my home directory so I just have a `~` (that's called a tilde in case you wondered).

## Mea culpa

First off, a _mea culpa_. I managed to leave a couple of things out of the VM as you got it. First order of business is to fix that. This is going to take some typing into the terminal.

```shell
sudo -H pip install colorama
```

This will ask you for your password, and then install the [colorama](https://pypi.python.org/pypi/colorama) package. This makes it fairly easy to colour the results of a print to the terminal. This gets used a lot in the tests.

## How to homework

Let's get _your_ copy of the code onto _your_ computer

```shell
git clone [your clone path, from the green button on github]
```

Now we can change directory and go into the `code1161base` directory. From now on, let's just call this _base_.

```shell
cd code1161base
```

Let's see what's there, `ls` lists the contents of the folder:

```shell
ben@um:~/code1161base$ ls
aboutMe.yml      email_template.md  node_modules  week2  week6
admin            __init__.py        README.md     week3  week8
codeHelpers.py   marking_puller.py  vmStartup     week4
codeHelpers.pyc  mugshot.png        week1         week5
```

Running the command `python week1/pytest.py` does all the work you need. So, here's how it goes for me:

```
ben@um:~/code1161base$ python week1/pytest.py
Let's test Python and Requests:

****************************************
*                                      *
*   Python and requests are working!   *
*                                      *
*    All hail his noodly appendage!    *
*                                      *
****************************************
8232d00b53d4d3d04424a78156c79f9e

ben@um:~/code1161base$
```

Your long number will be different to mine.

If you don't get this, then you might not have a current internet connection.

## Don't stop yet, there's more to do!

You've done your homework, but you need to _submit it_. On this course, this is done using github.


If you've done the first part, there will be 2 new files created. We can see this by using `git status`:

```
ben@um:~/code1161base$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

    week1/_checkID
    week1/_requestsWorking

nothing added to commit but untracked files present (use "git add" to track)
ben@um:~/code1161base$
```

The two files are sitting there, sad, untracked, waiting to be pulled into the git fold. You can do this by typing `git add .` or `git add week1/_checkID week1/_requestsWorking`, so you can see why `git add .` is more popular. In this context, the `.` means _everything in this folder (and below)_. Usually we want to commit more carefully than this, but these two files are actually related so we want them committed together.

```
ben@um:~/code1161base$ git add .
ben@um:~/code1161base$
```

nothing happens, because it's all going according to plan.

But if we do another `git status` we get:

```
ben@um:~/code1161base$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    new file:   week1/_checkID
    new file:   week1/_requestsWorking

ben@um:~/code1161base$
```

These files are now _staged_, you still need to _commit_ them.
type `git commit`, then the flag `-m` which means that you'll write the commit message inline, then [a good commit message](https://chris.beams.io/posts/git-commit/):

```
ben@um:~/code1161base$ git commit -m "do week 1 homework"
[master bdc280c] do week 1 homework
 2 files changed, 3 insertions(+)
 create mode 100644 week1/_checkID
 create mode 100644 week1/_requestsWorking
ben@um:~/code1161base$
```

Now you just need to do a `git push` and follow the prompts.

## Checking that it all worked

The easiest way to check is to look on github for the new files.

If you want to _really_ make sure, then you can run the tests. We'll be covering this in more detail in this week's (week 2) lecture so don't stress too much.

The tests are the actual code that I run on my computer to see if your work is correct. Each week has a tests.py file in it.

To run the tests for week 1, change directory into week 1:

```
ben@um:~/code1161base$ cd week1
```

and then run the test:

```
ben@um:~/code1161base$ python tests.py

Welcome to week 1!
Let's check that everything is set up.

✔ Exercise 1: Test that your VM is working
✔ Exercise 1: Test your connection to the internet
ben@um:~/code1161base$

```

If you get 2 ticks then you are done. Each tick is worth <sup>1</sup>&frasl;<sub>number of tests</sub><sup>th</sup> of that week's marks. As there are 2 ticks, each one is worth 50%.
