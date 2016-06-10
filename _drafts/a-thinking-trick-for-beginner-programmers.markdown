---
layout: post
title: A thinking trick for beginner programmers - Ghetto TDD
date: 2016-06-10 09:28:21   PDT
type: post
published: true
status: publish
categories: []
tags: []

#this goes on the index page, and into facebook shares
description: A thinking trick that'll make it easier to program

# This is what twitter will pick up if someone tweets the link to this page 
# 110 marker 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
twitter-body: Doing ghetto TDD as a way to think as a beginner programmer
#Twitter and facebook will pick up this image. you can also use it in a post with:
# ![alt text]({{ site.baseurl }}/assets/{{page.featuredimg}}) 
featuredimg: 16/gap.gif
---

I've taught programming to a lot of people who don't have a STEM background; mostly architecture students. The myth is that architects know a lot of maths, but that's mostly false[^1]. That said, they are totally sold on the idea of programming as a creative medium, and often have a good idea of their intended outcome. They know where they want to go, but get frustrated because they can't get there.

> Slow is smooth and smooth is fast

One of the traps I see beginner programmers falling into is trying to go too fast. I can't find a source for that quote, but it's generally attributed to military types. It's a bit like <q>more haste; less speed</q>. 

There is a lack of respect for the skill level that professional programmers need to do their job. That lack of respect is totally natural; as a beginner in any endeavour you [don't know enough to evaluate your own ability](https://en.wikipedia.org/wiki/Dunning%E2%80%93Kruger_effect). That's fine, don't worry about it, that will come in time. Here's one way that you can make things a bit less painful until you get a bit more mastery of the art.

# Ghetto TDD

TDD stands for Test Driven Development. It, and all it's variants have one principle in common, _write a test before you write any code_. If you look up TDD methods you'll immediately come to a wall of complicated test frameworks. These are all totally overkill for the kind of code you'll be working on if you are reading this. This is because pro programmers can usually think their way through the kinds of problems beginners get stuck on. You want a way to get your head around _your_ problems, not a way to make sure _their_ problems don't trip you up.

I'm going to use some simple code here that you can probably run in your head. This might make you think that there's no point doing this, but I want you to be able to see what's going on. If I made the code hard it'd be too hard to grasp the bigger picture.


Here's an [empty console you can play in to keep up with what's going on](http://jsbin.com/mavodunago/edit?js,console).

## The problem we'll try to solve

We're getting some data from a database, then we need to do something else with it. This is a real problem [based on this](http://where-in.space/2016/updating-some-changes-to-the-javascript), but I'm going to really cut down the complexity for the moment.

### Input

The first thing to do is to work out what we're actually dealing with. I'm going to use the Mongo restaurants data as an example.

``` json
{
  "address": {
     "building": "1007",
     "coord": [ -73.856077, 40.848447 ],
     "street": "Morris Park Ave",
     "zipcode": "10462"
  },
  "borough": "Bronx",
  "cuisine": "Bakery",
  "grades": [
     { "date": { "$date": 1393804800000 }, "grade": "A", "score": 2 },
     { "date": { "$date": 1378857600000 }, "grade": "A", "score": 6 },
     { "date": { "$date": 1358985600000 }, "grade": "A", "score": 10 },
     { "date": { "$date": 1322006400000 }, "grade": "A", "score": 9 },
     { "date": { "$date": 1299715200000 }, "grade": "B", "score": 14 }
  ],
  "name": "Morris Park Bake Shop",
  "restaurant_id": "30075445"
}
```

This is our input. 

### Output

The next thing we need to do is to decide what we want to end up with. How do we want this data to be once we're finished with it.

Let's say that we're making a reviews site and we want to turn the JSON into a sentence about the restaurant. We might want it to look like:

> The Morris Park Bake Shop is a Bakery in Bronx. It's got an average score of 8.2

Let's ignore how weird it sounds to say _in Bronx_ for now. We've got an input and an output and we're off to the races.


``` json
{
  "address": {
     "building": "1007",
     "coord": [ -73.856077, 40.848447 ],
     "street": "Morris Park Ave",
     "zipcode": "10462"
  },
  "borough": "Bronx",
  "cuisine": "Bakery",
  "grades": [
     { "date": { "$date": 1393804800000 }, "grade": "A", "score": 2 },
     { "date": { "$date": 1378857600000 }, "grade": "A", "score": 6 },
     { "date": { "$date": 1358985600000 }, "grade": "A", "score": 10 },
     { "date": { "$date": 1322006400000 }, "grade": "A", "score": 9 },
     { "date": { "$date": 1299715200000 }, "grade": "B", "score": 14 }
  ],
  "name": "Morris Park Bake Shop",
  "restaurant_id": "30075445"
}
```
{: style="font-size: 50%"}

⇣ Some magical function that does a transform ⇣
{: style="text-align: center"}

``` JS
"The Morris Park Bake Shop is a Bakery in Bronx. It's got an average score of 8.2"
```
{: style="font-size: 60%"}

### The magical transform function

Let's jump right in and start working on this...

Actually, **STOP** this is exactly the wrong thing to do! First we should write a test!

### My First Test

A test is just a function that checks to see if your transform function does what it's supposed to. Here's an example
<noscript>
``` JS
function add (a, b){
    return 4;
}

function testAdding (aNumber, anotherNumber, theResult){
    console.log(`if I add ${aNumber} and ${anotherNumber} I expect ${theResult}`)
    console.log( add(aNumber, anotherNumber) === theResult);
}

testAdding(2, 2, 4);
testAdding(1, 3, 4);
testAdding(4, 0, 4);
testAdding(4, 4, 8);
```
</noscript>

<a class="jsbin-embed" href="http://jsbin.com/hicalukovi/1/embed?js,console">JS Bin on jsbin.com</a><script src="http://static.jsbin.com/js/embed.min.js?3.35.13"></script>

This is all great! Our add function kicks arse until we get to the last case, and then it sucks. 

We are doing things exactly right though. The model is _red, green, refactor_[^2]. This means that we write a test that we think is good, then we write a function that _fails_.

Exercise for you: 

* How would you rewrite the add function so that it passes?
* Add some more test cases that might catch it out.

If we rewrite this for our restaurant data then it might look like this:
<noscript>
``` JS
let inputData = {
  "address": {
     "building": "1007",
     "coord": [ -73.856077, 40.848447 ],
     "street": "Morris Park Ave",
     "zipcode": "10462"
  },
  "borough": "Bronx",
  "cuisine": "Bakery",
  "grades": [
     { "date": { "$date": 1393804800000 }, "grade": "A", "score": 2 },
     { "date": { "$date": 1378857600000 }, "grade": "A", "score": 6 },
     { "date": { "$date": 1358985600000 }, "grade": "A", "score": 10 },
     { "date": { "$date": 1322006400000 }, "grade": "A", "score": 9 },
     { "date": { "$date": 1299715200000 }, "grade": "B", "score": 14 }
  ],
  "name": "Morris Park Bake Shop",
  "restaurant_id": "30075445"
};
let outputData = "The Morris Park Bake Shop is a Bakery in Bronx. It's got an average score of 8.2";


function makeSentence (input){
    return "The Morris Park Bake Shop is a Bakery in Bronx. It's got an average score of 8.2";
}

function testMakeSentence (input, theResult){
    console.log(`given ${JSON.stringify(input)} I expect ${theResult}`)
    console.log( makeSentence (input) === theResult);
}

testMakeSentence(inputData, outputData);
```
</noscript>
<a class="jsbin-embed" href="http://jsbin.com/jaletenida/1/embed?js,console">JS Bin on jsbin.com</a><script src="http://static.jsbin.com/js/embed.min.js?3.35.13"></script>

This looks a _lot_ more complicated, but actually it's exactly the same as before. Our job now is to write some more useful code that we think will turn any input data into the right output.

Our magical transform function is now:

``` JS
function makeSentence (input){
    return "The Morris Park Bake Shop is a Bakery in Bronx. It's got an average score of 8.2";
}
```

Which gives us the same answer whatever the input. A better try might be:

``` JS
function makeSentence (input){
    let grades = 8.2;
    return `The ${input.name} is a ${input.cuisine} in ${input.borough}. It's got an average score of ${grades}`;
}
```

This still isn't fully general because it will always give you a grade of 8.2, but we can work on that. The test still passes and we know that whatever we've done works.

# Conclusion

This is a good drill to help at the start of your career. It's up to you if take with you for the rest of your life as you get better.

It's extremely helpful to take the time to define your input and output data. Just doing that is often enough to make it clear how to solve the problem.

Learning to program is mostly about ways of mapping an input to an output. It's also about having a clear enough head to do this. Very little of programming is typing; it is almost all thinking.


[^1]: This is true for British, Australian and Americans, less so for mainland Europe, Russia as their architecture education requires a lot more maths. In my degree we had 2 lectures that included any calculations, and it was primary school level maths. I don't think there is _any_ maths in Australian architectural education.

[^2]: By _green_  you made it work, but not be good. The _refactor_ part means taking the bad but working code (messy, slow, etc.) and make it good. The test will stop you from introducing _regression_ errors.