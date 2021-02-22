---
layout: post
title: "Updated: A Game About Possible Futures"
date: 2021-1-1 9:00:00 AEST
type: post
published: true
status: publish
categories: []
tags: []
author-name: Ben Doherty

# this goes on the index page, and into facebook shares
description: "A game to help you think about the future."

# This is what twitter will pick up if someone tweets the link to this page
# 110 marker 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
twitter-body: "A game to help you think about the future."
# Twitter and facebook will pick up this image. you can also use it in a post with: -
#![alt text]({{ site.baseurl }}/assets/{{page.featuredimg}})
featuredimg: https://www.architecture.com/image-library/imagecache/galleryitems/82870.1.434.434.FFFFFF.jpeg
---

<style>
  a {
    overflow-wrap: break-word;
  }
  /* body {
    background-color: beige !important;
  }  */
  
  figcaption {
      float: right;
  }
  .toc {
    column-width: 12em;
    font-size: 70%;
  }
  @media screen {
    .to-print {
      display: none;
    }
    section.card{
      width: 9in;
      border: 1px solid black;
      border-radius: 1em;
      padding: 10mm;
      font-size: 10pt;
      height: 6in;
      column-count: 2;
      margin-bottom: 1em;
    }
    section h2,
    section h3 {
      margin-bottom: 0;
    }
    article.post section blockquote {
      font-size: 80%;
      width: 100%;
      padding-left: 0.5em;
    }
  }
  @media print {
    /* html, body {
      height: 210mm !important;
      width: 297mm !important;
    } */
    @page {
      /* size: 148mm 210mm !important; */
      size: A5 !important;
      margin-bottom: 0;
      margin-left: 0;
      margin-right: 0;
      margin-top: 0;
    }
    iframe,
    header {
      display: none;
    }
    .post-content {
      column-count: 1 !important;
    }
    article.post figure img {
      max-height: 40vh;
      max-width: 50%;
      width: unset;
    }
    section {
      /* margin: 1em; */
      background-color: white;
      break-inside: avoid;
      column-count: 2;
      display: inline-block;
      display: inline-block;
      outline: 1px solid;
      padding: 1cm;
      page-break-before: always;
      vertical-align: bottom;
      /* height: 210mm;
      width: 148mm; */
    }
    section h1,
    section h2,
    pre,
    figure {
      column-span: all;
    }
    section h1 {
      text-align: center;
    }
    article.post h2 {
        margin-top: 0;
        border: none;
    }
    figure p {
      text-align: center;
    }
    article.post figure img {
      max-height: 55mm;
      max-width: 50%;
      width: unset;
    }
    h3 {
      break-after: avoid;
      /* This isn't actually implemented yet,
      but one day it'll make the headers look nice */
    }
    article.post li {
      margin-bottom: 0.2em;
    }
    .footnotes {
      border-top: none;
      column-count: 2;
      padding: 1cm;
      page-break-before: always;
    }
    section td {
      text-align: center;
    }

  }
</style>

<section>

# Possible Futures

It's difficult to sit down and think about the future. It's tempting to think about the present, but blue and shiny[^construal]. Or to think about the issue that's important and in the news today, and have much more or much less of it. You need a _framework_!

This is a game that helps its players think about the future. It gives players specific things to think about, and by thinking about the interactions between those things, gives a different way of thinking. It's not any more "correct", but it breaks through the barrier of simplistic utopias or dystopias, and pushes the ideas into the messy, soupy middle.

Have fun with this, and let your imagination loose. If there's anything we've learned from the recent past, it's that _That could never happen_ means that it's almost guaranteed to happen.

## How to play

Get into teams; teams of 3 seem to work pretty well. If the team is too small it's hard to get enough ideas bouncing around, if it's too big, not everyone's option gets heard.

Print out the cards. In total you need about 10 per team, there are {{ site.data.cards | size }} cards now, so you can work that out.

If you've got a particular focus or reason for running this workshop, then it's probably ok to make a fixed card that is always in each team's hand. E.g. if you really care about smart cities, make a card (or cards) about that, and make sure that each team always has one of them.

Someone needs to be the MC/time keeper. It helps to have a few people going around to get the teams to think a bit differently if they get stuck in a rut.

</section>
<section>
## Contributing

There are two main ways to contribute:

### Improving cards

These cards are made by me, who is an expert in none of these topics. If you _are_ an expert then you probably have way more useful things to say! Better illustrations, better prompts, better footnotes, and so on.

You can improve them by going to [GitHub](https://github.com/notionparallax/blog/tree/gh-pages/_data/cards) and just editing the card you're interested in. Don't worry about breaking it, your edit will be sent to me for approval first.

### Making new cards

Cards are defined using a YAML format that looks like this:

```yml
title: The name of the card
image:
    source: usefulPicture.jpg
    caption: This is an image of an xxx
    citation: a graph by by YYY
    link: https://www.google.com/
body:
    paragraphs:
        - The first paragraph.
        - Another one.
        - one more just for luck[^luck].
footnotes:
    luck: "I'm not sure luck really exists: [luck](en.wikipedia.org/wiki/luck)"
consider:
    - add a prompt for the players
    - And maybe another one too
card_type: future_tech
```

Save the file as `The name of the card.yaml` and either [💌email](mailto:ben@notionparallax.co.uk) it to me, or make PR against the repo. (I'd go with email for the moment, until this game gets it's own repo; my blog is a huge download.)

The current cards are:

<div class="toc">

{% for org_hash in site.data.cards %}
{% assign card = org_hash[1] %}

-   {{ card.title }}

{% endfor %}

</div>

</section>

<section>

## Early rounds

This is all about getting warmed up. You can play through this stage for as long as you like until you feel like everyone's "got it".

I'd recommend playing 3 rounds, the first with 1 card, the second with 2, and the third with 3 cards.

For these first rounds, keep them quick, 10 minutes or so. You should keep these following prompts in mind, but not be too diligent about doing them all. Save the diligence for the last round.

1.  Each team picks N card[s], at random. The job then is to bat ideas around between the team members. Most of the cards don't explicitly give an outcome, more like an idea or a trend, so it's the team's job to think about the bounds of that trend. E.g. will _all_ the bees die, or will we do something magical and get bee populations to their highest ever level?

1.  If you've got more than one card, think about each one individually, and then think about their interactions. Do they amplify each other (IoT trackers glued to bees?) or cancel out (a fashion for owning bee eating lizards?).

1.  If you've heard of the _five whys_, this is the five _and then whats_. Think of an effect:

    {:start="0"}

    1. get started

        - not many bees

    1. and then what?

        - so not as many people get stung as kids

    1. and then what?

        - so more people get stung for the first time as an adult

    1. and then what?

        - so more people die from anaphylaxis without any warning

    1. and then what?

        - so people are more afraid of bees

    1. and then what?

        - so people go out of their way to kill bees when they see them.

    This might not be scientifically supportable, but you can get to some pretty interesting and unintuitive results from it.

1.  Once you've got a pretty good grasp on how the ideas interact, take some time to think about them from different perspectives.

    -   How does it affect the economy? What about under different forms of government? How would they deal with it in the USA, in France, in China, in North Korea?
    -   How will it change what we eat?
    -   How will it change what we buy?
    -   How will it change family structures?
    -   How will it change our free time?
    -   How will it change what we think about as we live our lives?
    -   How will it change what society values?

1.  Invent a protagonist.

    -   What do they do?
    -   How is their life different to yours?
    -   How is it the same?

1.  Capture it! Write notes, do sketches, take photos of your team acting out scenarios. The idea is to have a record of your thoughts so that _if you wanted_, you could go back and write a speculative fiction short story about your world.

1.  Put all your cards to one side, and take N+1 new cards. Start again, but with more insight and enthusiasm now that you're getting more warmed up.
</section>

<section>

## Final round

Each team keeps one card from their last round (so throw away 2 of the three for example).

Play through the same as before, but take the luxury of more time. Make your notes a bit more detailed and your sketches more detailed/atmospheric. Once you're about 10&ndash;15 minutes in we can start to stress test the ideas.

Pair up teams, and present the future to the other team. Their job is to stress test the future. To be clear, it's not to find a knock down argument that destroys the delicate fiction that you're assembling! It's to ask questions that they think that you haven't thought of, and to ask for clarification. If you're a dick in your questioning, nobody wins, so help build your partner team's world.

Once the teams have reciprocated, swap again. Have a little break between swaps to consolidate your team's thoughts, and then go refreshed into the stress test.

Take a bit more time to weave all these ideas into a story, and then tell everyone about that world.

### Tips

-   It's very tempting to think of blissful utopias or of hellish dystopian worlds, but there is good, even joy, in all worlds, and bad in them too.

    Try to avoid extremes in your worlds, it'll feel much more real if it's nuanced. Balance is a much better place to make a jump from.

-   Make way more notes than you think you need. At the time everything seems impossibly vibrant, but as the blinding light of the next idea comes along, it'll bulldoze the preceding ideas out of its path.

-   Grab quotes from others in your team, they're really usable in future bits of work you'll do.

## The canvas

Fill in the canvas. Its job is to make all the ideas visible, so that you can start to probe them for inconsistencies. Start using post it notes, so that you can change things, _a lot_.

### Canvas

If you've got a big printer, print this as A3 or even better A2

![]({{ site.baseurl }}/assets/20/game/Artboard 1@1x.png)

[High res download]({{ site.baseurl }}/assets/20/game/Artboard 1@4x.png)

Or just work through these prompts on whatever paper you've got:

-   Imagine an object used in this world
-   What would a convenience store be like (or the nearest thing to one)?
-   What's child rearing like?
-   What are the last 10 years of a person's life like in this world
-   draw up a timeline of your protagonist's day, who do they interact with, what technology do they interact with?
-   How will this scenario
    -   affect the economy?
    -   change what we eat?
    -   change what we buy?
    -   change family structures?
    -   change our free time?
    -   change what we think about as we live our lives?
    -   change what society values?
-   How would it play out under different forms of government? How would they deal with it in the USA, in France, in China, in North Korea?
</section>

---

{%- comment -%}
From here down is the automatically generated content from the `cards`
sub-folder in the `_data` folder.
{%- endcomment -%}

{% for org_hash in site.data.cards %}
{% assign card = org_hash[1] %}

<section class="card {{ card.card_type }}">
## {{ card.title }}

<figure>
![]({{ site.baseurl }}/assets/20/game/images/{{ card.image.source }})
<figcaption>{{ card.image.caption }} <a href="{{ card.image.link }}"><cite>{{ card.image.citation }}</cite></a>
</figcaption>
</figure>

{% for p in card.body.paragraphs %}
{{ p }}
{% endfor %}

### Consider

{% for p in card.consider %}

-   {{ p }}
{% endfor %}
</section>

{% for fn in card.footnotes %}
[^{{ fn[0] }}]: {{ fn[1]}}

{% endfor %}

{% endfor %}
