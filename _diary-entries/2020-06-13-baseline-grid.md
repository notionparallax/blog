---
layout: post
title: Baseline Grid Drift
date: 2020-06-13 11:11:11 AEST
type: post
published: true
status: publish
categories: []
tags: []

## this goes on the index page, and into facebook shares
description: Documenting a maddening bug with how chrome renders repeating backgrounds

## This is what twitter will pick up if someone tweets the link to this page
## 110 marker 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
twitter-body: Documenting a maddening bug with how chrome renders repeating backgrounds
## Twitter and facebook will pick up this image. you can also use it in a post with:
## ![alt text]({{ site.baseurl }}/assets/{{page.featuredimg}})
featuredimg: {{ site.baseurl }}/assets/20/baseline_grid_drift.png
---

I've been trying to use a baseline grid in [Walden Pond](https://waldenpond.press/) for a _lot_ of the last couple of weeks. and I couldn't work out why the content would drift off the grid as it went down the page.

It seems like it's a Chrome bug. 😡

<figure>
![three browsers next to each other showing their different rendering of the same content.]({{ site.baseurl }}/assets/20/baseline_grid_drift.png)

<figcaption>
This is the same content rendered in 3 different browsers. From left to right:
1. Firefox 76.0.1
1. Chrome Canary 85.0.4170.0
1. Chrome 83.0.4103.97 (in incognito so there's no extensions doing unexpected things)

</figcaption>

</figure>

I thought it had something to do with the way the baseline was being drawn, so I tried 3 different ways of drawing a grid: a repeating image, and 2 gradient bases ways. Turns out they all work in almost exactly the same way. The drift is caused by something in the way that the current production Chrome repeats backgrounds.

It's working properly in canary, so fingers crossed, the problem will go away if I just wait.

Below is a live version, if the problem exists on your system you should see text starting to drift off the baseline by the second or third paragraph.

<style>
:root {
--line-height: 1.4rem;
--baseline-color: hsla(194, 100%, 50%, 0.7);
--color-paper: hsla(0, 0%, 100%, 0);
}
#demo * {
margin: 0;
padding: 0;
}
#demo div {
display: inline-block;
width: 30%;
outline: 1px solid;
}
#demo h1 {
line-height: calc(var(--line-height) * 2);
margin-bottom: calc(var(--line-height) * 1);
transform: translateY(calc(var(--line-height) * 0.5));
text-transform: capitalize;
font-size: 2rem;
}
#demo p {
line-height: calc(var(--line-height) * 1);
margin-bottom: calc(var(--line-height) * 1);
transform: translateY(calc(var(--line-height) * 0.25));
font-size: 1rem;
}
.one {
background-image: url({{ site.baseurl }}/assets/20/line_marker.png);
background-size: 100% var(--line-height);
background-repeat: repeat-y;
}
.two {
background-image: linear-gradient(
    var(--baseline-color) 1px,
    transparent 1px
);
background-repeat: repeat-y;
background-size: 100% var(--line-height);
}
.three {
    /* This is taken from the paged.js css */
background: linear-gradient(
    var(--color-paper) 0%,
    var(--color-paper) calc(var(--line-height) - 1px),
    var(--baseline-color) calc(var(--line-height) - 1px),
    var(--baseline-color) var(--line-height)
    ),
    transparent;
background-repeat: repeat-y;
background-size: 100% var(--line-height);
}
</style>
<div id="demo">
<div class="one">
<h1>one</h1>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.
</p>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.
</p>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.
</p>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.
</p>
</div>
<div class="two">
<h1>two</h1>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.
</p>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.
</p>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.
</p>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.
</p>
</div>
<div class="three">
<h1>three</h1>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.
</p>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.
</p>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.
</p>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.
</p>
</div>
