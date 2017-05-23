---
layout: post
title: Altspace automatic test fits
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

<style>
iframe {
  width:100%;
  height:60vh;
}
</style>

# Initial thoughts <small>doodling in my notebook</small>

Approach falls into 2+[^dichotomy] broad categories (1) optimisation and (2) apprenticeship.

## (1) Optimisation
Optimisation is the 'classical' approach. We, somehow, define a system that assesses the quality/fitness of a proposed solution. The algorithm then searches the design space for high scoring results.

## (2) Apprenticeship
Apprenticeship uses the computer to propose, then a human to assess, and then the computer tries to uncover/elicit the structure of the assessment.

---

With (1) there is more of a risk of baking in biases, or potentially cutting off a good avenue to explore.  This may also be a problem with (2) but it'll be easier to identify and fix in (1) so it's a trade off I guess.

To get the results/examples we want we'd need to get a corpus of examples. Assuming we start with the alt space furniture, we have a nicely constrained search space. I.e. _x_ furniture items and _y_ amount of space. (Where _y_ is between _a-b_ m².)

It would be good to pull a load of potential plan shapes from real estate sites. Different combinations of views, cores, shapes, sizes etc. Then we can get people to test fit and assess the examples to give us an idea of what's going on.

We should do some interviews to actually understand what people are looking for in a test fit. Interview part and then an observed task part where they do a layout. How can we broaden the group size beyond BVN?

Option (2) would need a large set of examples to start with, or a basic generation representation (i.e. give it skills like move and rotate, but don't tell it too much beyond that.)  Then, without saying why, the layout would be assessed by a human expert. They would provide either a single quality value or a quality value and a map of quality that points out bad and good things (or potentially just bad?). Underlying it all would need to be some sort of representation. It would contain things like the list of intersection events and accessibility criteria (straight skeleton, union of circles?)

In summary:

* ☐ get possible outlines
* ☐ get furniture set
* ☐ look at assessment representations/features
* ☐ design interviews
* ☐ eventually pull it all together into a _things we know_ deck


[^dichotomy]: Always distrust dichotomies!

# Designing the interviews

What do we actually want to know?
* What is a test fit for?
* What metrics are you generating?
* What other things do you take into consideration?

Then do an observed activity, with them narrating and me asking why a lot. Probably just laying out an altspace space.

# review of papers and products

## Interactive Furniture Layout Using Interior Design Guidelines

* Merrell, P., Schkufza, E., Li, Z., Agrawala, M., Koltun, V. **2011**. *Interactive Furniture Layout Using Interior Design Guidelines.* ACM Trans. Graph. 30, 4, Article 87 (July 2011), 9 pages. [DOI=10.1145/1964921.1964982](http://doi.acm.org/10.1145/1964921.1964982)

## Make it Home: Automatic Optimization of Furniture Arrangement
* Yu, L., Yeung, S., Tang, C., Terzopoulos, D., Chan, T., Osher, S. **2011**. *Make it Home: Automatic Optimization of Furniture Arrangement.* ACM Trans. Graph. 30, 4, Article 86 (July 2011), 11 pages. [DOI=10.1145/1964921.1964981](http://doi.acm.org/10.1145/1964921.1964981).

System that automatically extracts relationships from example scenes that are provided as a training set. It applies those relationships to new scenes.

Looks for:
*   **Bounding surfaces** (convex hull), is also looking for which part faces the wall.
*   **Centre and orientation**. If the back faces the wall, in 2d this establishes direction.
*   **Accessible space**. how do you get to the important part of the furniture? They use a rectangle I think. It might be worth thinking of this as a gradient? That might be a perf consideration.
*   **Visibility** Things like TVs and pictures need to be seen. Represented as a cone of rectangles. Rectangles must be used for perf, polygon seems more sensible.

Uses simulated annealing with moving, rotating, swapping to move furniture, and also moves pathway around. Not sure if the path is considered a piece of negative space furniture.

Did a comparative study to see if people could tell the difference between human and auto generated results.

### Thoughts:

Looks good, not super clear _how_ the relationships are extracted, but they do say what they look at.

Results are targeted at games development, not sure if they are good enough for a test fit, mainly because I don't know how good a test fit actually needs to be!

Simulated annealing appears to be a good approach to this optimisation-style strategy. If we think of this as a multi stage approach, this might be a good way of doing the last bit (actual arrangement)

<iframe src="https://www.youtube.com/embed/vlDoSv6uDKQ" frameborder="0" allowfullscreen>
</iframe>

Also, on a similar theme:

<iframe src="https://www.youtube.com/embed/AHwr9MzCMKg" frameborder="0" allowfullscreen>
</iframe>

## Intelligent critic system for architectural design


## [floored.com](http://www.floored.com/plans/)
