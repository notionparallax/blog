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

# Review of papers and products

## Interactive Furniture Layout Using Interior Design Guidelines

* Merrell, P., Schkufza, E., Li, Z., Agrawala, M., Koltun, V. **2011**. *Interactive Furniture Layout Using Interior Design Guidelines.* ACM Trans. Graph. 30, 4, Article 87 (July 2011), 9 pages. [DOI=10.1145/1964921.1964982](http://doi.acm.org/10.1145/1964921.1964982)

This seems like a good idea, provide support for designers, rather than dictating ideas.

Paper is very mathematically expressed. (Which made it a bit tricky for me to understand everything quickly.)

<figure class="half-width right">
![](http://4.bp.blogspot.com/_7C47xzBkV5Q/Sp5yeB_b65I/AAAAAAAAG-s/cPNJioe3yPQ/s320/afid2.jpg)
<figcaption>
They have explicitly taken interior design guidelines from [Anatomy for interior designers](https://www.amazon.com/Anatomy-Interior-Designers-Julius-Panero/dp/0823070263)
</figcaption>
</figure>

They use the configuration space to decide where you can walk. We've done a bit of this before with SQ&AT, but with furniture it migh tbe different to walls, I'd be happy brushing a leg against a stool, but not a wall. (Worth thinking about.)

They have a concept of 'focal point' which positively weights being able to view something like a fireplace.

There is also a concept of conversation, chair-occupants that might be able to talk to each other should be within a radius.

They use simulated annealing to run the optimisation. They put a lot of effort into computational performance.

They ran a study to see if people preferred assisted layout to fully manual mode. in most cases there is a moderate to weak preference.

<figure class="half-width right">
![ratios of preference]({{ site.baseurl }}/assets/17/assistedPreference.png)
</figure>

Similarly to _Make it home_, this approach requires explicit definition of pairwise relationships between furniture. This seems to result in fairly predictable structures that just move about in the space. E.g. sofa next to coffee table. What I'm less sure about is if this is a problem. We are generally fine with cad-blocks of sofas and coffee tables, or beds and bedside tables; this is just more of the same, but a bit more adaptive.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Xu7CUP9OQY8" frameborder="0" allowfullscreen></iframe>

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


## Intelligent critic system for architectural design


## [floored.com](http://www.floored.com/plans/)

Floored were a technology company that did a couple of things, they sold to CBRE. The CBRE press release about the acquisition describes those things as:

>Floored’s two main existing SaaS products are:
> * Protofit, which allows users to visualize and edit floor plans in 2D and 3D (including accurate external window views from each floor) and to create customized space layouts in real-time.  Protofit, which is being rebranded as Floored Plans, has been utilized in over 65 million sq. ft. of properties.
> * Luma, which enables a high-quality, interactive, next-generation customized 3D “walk-through” experience for new, unbuilt and repositioned spaces. This technology has been used to visualize space from project concept and design all the way through leasing and marketing efforts and is now being re-branded as Floored Build.

It's a bit hard to see what the state of things is now as they've been pretty quiet since joining CBRE (as far as I can tell).

It seems like the two products they have now are:

> [Floored Build](http://www.floored.com/build/). A bespoke, videogame-like experience for real estate professionals.

> [Floored Plans](http://www.floored.com/plans/). A breakthrough marketing and leasing tool for office space.

#### Summary of their site:
---
##### Floored Plans. A breakthrough marketing and leasing tool for office space.
Smart, interactive floor plans in 2D and 3D.

Floored Plans puts you in control of your leasing process. Create unlimited layouts, customized for each prospect. Be an expert on every property with live metrics and measurements.
And wow prospects with one-click, immersive 3D walkthroughs complete with accurate panoramic views from every floor.

*   Share and track
    Share test fits with your prospects and they’ll be able to customize the space for themselves. Then, visit the Sent Spaces dashboard to track activity and gauge interest. See how tenants customize the space, how long they spend on the page, and more.

*   Edit test fits
    Turn around most changes in seconds with simple tools. Floored Plans complies with code and makes architect-approved layout decisions.

*   **Interactive measurements**
    Zoom in to see the measurements of any room in your plans right from your browser. It’s more convenient and more accurate than a step-count guesstimate.

*   **Floored Plans 3D**
    With one click, instantly turn any floor plan into a fully interactive 3D tour. Show tenants not just how they’ll fit, but how they’ll live in the space.

*   **Panoramic Views**
    Look out the window of any 3D space and you’ll find accurate views. Plans automatically pull the latest images from Google Earth.


1.  **Send Floored your architectural files**
    We convert your CAD into smart, simple, online plans, making your space available from any browser.

2.  **Customize a plan**
    Start with as-built conditions or a Floored-supplied template like “Legal Office” or “Open Plan.” Then, customize the layout to your tenants’ needs in seconds.

3.  **Be an Expert**
    Provide accurate headcount and measurements, and give tenants a feel for the space with an interactive 3D tour.

4.  **Share**
    Send a link to any layout or 3D tour, or print a PDF.

---

This has all now been rolled into [CBRE Vantage](http://www.cbre.com/about/tech-vantage) (worth a look!)
<figure class="half-width right">
> CBRE brokers now use Floored’s products to help clients who are looking for new office space virtually “walk” through a potential location they are vetting; ...The technology is meant to save the brokerage’s clients up to hundreds of thousands of dollars in architectural costs and countless hours they would normally spend physically touring spaces.

<figcaption>
From [Floored to Ceiling: Inside CBRE’s Tech Revolution, Led by David Eisenberg](https://commercialobserver.com/2017/04/a-look-inside-cbres-tech-revolution-led-by-david-eisenberg/)
</figcaption>
</figure>

They seem to have stopped talking about automatic testfits, before they had a product called protofit that was looking into this. There isn't any proof that it's AI though (it might just be concierged). They might have pivoted away from test fits because it's hard, or because the market size isn't big enough?

What they were doing before:

<figure class="half-width right">
<iframe src="https://player.vimeo.com/video/138914937" width="500" height="281" frameborder="0" title="Protofit" webkitallowfullscreen="" mozallowfullscreen="" allowfullscreen="">
</iframe>
</figure>

http://www.floored.com/protofit returns a 404

[introducing protofit tenant](http://www.floored.com/blog/introducing-protofit-tenants/)

[Introducing Protofit: Test Fits Finally Made Simple](http://www.floored.com/blog/introducing-protofit/)

There is also the possibility that protofit never really did automatic layouts, but it was just the demented rantings of either a journalist or myself.

<figure class="half-width right">
<iframe width="560" height="315" src="https://www.youtube.com/embed/f8G1Ukdz1-8" frameborder="0" allowfullscreen>
</iframe>
<figcaption>
This video seems to say that they _do_ have some automation, but it's not clear what it is, or if they ever actually finished building it. (From 17 Apr 2015)
</figcaption>
</figure>

[Space HQ Announces It’s Platform Is Now Powered By Floored’s PROTOFIT Technology](https://medium.com/cre-tech/space-hq-announces-it-s-platform-is-now-powered-by-floored-s-protofit-technology-4d21100d7dd9)

(Space HQ is On Product Hunt — Custom 48 Hour Test Fits for the Workplace)[https://medium.com/cre-tech/space-hq-is-on-product-hunt-custom-48-hour-test-fits-for-the-workplace-79ea3032eca8] points to http://spacehq.co/testfits.html, but that's expired, but http://spacehq.co/ still works. Most likely the test fit part is now subsumed into their main product. It looks quite similar to alt space, it'd be worth figuring out what the difference actually is.

> Space HQ is proud to announce that we are offering 48 hour test fits for the workplace

Even if that isn't automated, if people are offering it then there's a good chance that the protofit software streamlined the process enough to make it possible.

# Project Fractal

[1](http://insidethefactory.typepad.com/thebuildinglab/2016/01/project-fractal-part-1-out-of-akaba.html)
, [2](http://insidethefactory.typepad.com/thebuildinglab/2016/02/project-fractal-part-2-you-know-what-we-did-last-summer.html)
, [3](http://insidethefactory.typepad.com/thebuildinglab/2016/02/project-fractal-part-3-from-akaba-to-fractal.html)
, [4](http://insidethefactory.typepad.com/thebuildinglab/2016/03/project-fractal-practice-partners.html)


# What is a test fit?

[What is the difference between a Test Fit and a Space Plan?](http://watchdogpm.com/blog/what-is-the-difference-between-a-test-fit-a-space-plan/)



# nice, but unrelated quotes
<figure>

> What remains hard is modeling. The structure inherent in three-dimensional models is difficult for people to grasp and difficult too for user interfaces to reveal and manipulate. Only the determined model three dimensional objects, and they rarely invent a shape at a computer, but only record a shape so that analysis or manufacturing can proceed. The grand challenges in three-dimensional graphics are to make simple modeling easy and to make complex modeling accessible to far more people.

<figcaption>
Robert F. Sproull 1990. Parts of the frontier are hard to move.
_Computer Graphics_ 24, 2, 9
</figcaption>
</figure>

<iframe src="https://www.youtube.com/embed/AHwr9MzCMKg" frameborder="0" allowfullscreen>
</iframe>
