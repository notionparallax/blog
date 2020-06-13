---
layout: post
title: "Printing hyperlinks nicely as footnotes"
date: 2020-6-13 15:45:00 AEST
type: post
published: true
status: publish
categories: []
tags: []
author-name: Ben Doherty

# this goes on the index page, and into facebook shares
description:

# This is what twitter will pick up if someone tweets the link to this page
# 110 marker
#123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789
twitter-body:
# Twitter and facebook will pick up this image. you can also use it in a post with: -
#![alt text]({{ site.baseurl }}/assets/{{page.featuredimg}})
featuredimg:
---

[Walden Pond](https://waldenpond.press/) is full of content that was intended to go on the web. So there's all sorts of problems with how to make it usable in print. One of the most obvious is [hyperlinks](rickroll).

There are some really nice tricks that make what the link links to visible in print.

<figure>
```css
a:after {
    content: " [" attr(href) "] ";
}
```
<figcaption>
From <cite>[CSS tricks](https://css-tricks.com/css-tricks-finally-gets-a-print-stylesheet/#4-display-the-urls-in-the-body-content)</cite>
</figcaption>

</figure>

Which is cool if your links are nice looking, but sometimes the text has a tonne of links in it and you can end up with more link than content.

In Walden Pond I've put the links in as footnotes. So a superscript number in the text, and a numbered list of links at the end of the article. I'm using a slightly edited version of [Aaron Gustafson's](http://www.easy-designs.net/) [footnote code](https://gist.github.com/Sinetheta/6612205) (from 2005!).

This is great, but sometimes you'll get an article that uses a lot of long links. A prime offender is when the article recommends a lot of things with amazon referrer links, but it could be almost anything. For example, in the Wait But Why post [From Muhammad to ISIS: Iraq’s Full Story](https://waitbutwhy.com/2014/09/muhammad-isis-iraqs-full-story.html) there are 54 links, and a lot of them look like this:

> https://www.ft.com/<wbr>content/<wbr>69e70954-f639-11e3-a038-00144feabdc0?%E2%80%94ftcamp=crm/email/<wbr>2014617/<wbr>nbe/<wbr>AsiaMorningHeadlines/<wbr>product#axzz3A20GKJTZ

In this case, the bit after the `?` is just tracking (_?%E2%80%94ftcamp=crm/email/<wbr>2014617/<wbr>nbe/<wbr>AsiaMorningHeadlines/<wbr>product#axzz3A20GKJTZ_) to tell the FT where the reader found the link. But in some cases, the URL params actually have useful information in them, so I can't just cut them off.

What I've ended up doing is using [Firebase Dynamic links](https://firebase.google.com/docs/reference/dynamic-links/link-shortener) to shorten these links, so the FT link above becomes: `Hi1e`

That's sort of cheating because it's actually `https://pond.page.link/Hi1e` but the first part is the same for all the shortened links.

This means that people can either remember the `https://pond.page.link/` part and build their own links, or they can go to the [Walden Pond website](https://waldenpond.press/) and type it into the link-expander.

<figure class="two-side-by-side">
![]({{ site.baseurl }}/assets/20/Link-expander-in.png)![]({{ site.baseurl }}/assets/20/Link-expander-out.png)

</figure>

<figure class="half-width right">
![some links in a list, some shortened, some not]({{ site.baseurl }}/assets/20/shortened-links.png)

<figcaption>
This figure is half-width and floated right

</figcaption>

</figure>

One problem with shortened links is that they're an extra layer of abstraction away. So you have no idea if `Hi1e` is taking you to the FT or to PornHub, or to _Best Number One Phishing Bank_. I've tried to get around that by only shortening links over 90 chars long, and then for the links I do shorten leaving the first part of the domain intact. Giving: `ft.com | Hi1e`.

Sometimes the link has an ID attached to it, so I've added that in too. Hopefully it's not too confusing, because without it, you can't see what the link points to because Firebase seems to strip off the #part of the url.
