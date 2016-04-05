---
layout: post
title: Asset pipelines - being part of the process
date: 2015-08-24 07:00:25.000000000 +10:00
type: post
published: true
status: publish
categories: []
tags:
- BVN
- data
- manifesto
description:
meta:
  _publicize_facebook_user: http://www.facebook.com/541400612
  _publicize_twitter_user: "@notionparallax"

---

<a title="Google Research Blog | The latest news from Research at Google | Speed Matters" href="http://googleresearch.blogspot.com.au/2009/06/speed-matters.html">Studies keep showing that making your website just a tiny bit faster </a><a title="HOW ONE SECOND COULD COST AMAZON $1.6 BILLION IN SALES" href="http://www.fastcompany.com/1825005/how-one-second-could-cost-amazon-16-billion-sales">makes your customers spend more</a>. There are lots of things that can make a website a tiny bit faster, and they are all pretty easy to do. However, no one thing is really going to give you a big speed bump. There might be 20 things that each give a 1% improvement.

Asset pipelines are a big thing in web programming now because they let you automate those 20 things.

The general idea is what I'd like to talk about here. I think that as a general idea it adds a lot of value to the way we work. I'll need to talk specifically a little, but I'll try and minimise that.

We use a tool called Grunt to organise our pipeline. It's all text based, but underlying it is some very grasshopper-like logic. Take _this_ from _here_ and put it _there_ . Then do something to it and move it somewhere else. That kind of thing is really time consuming for humans to do, and we're also just not very good at it.

<img class="size-full wp-image-1849 alignnone" src="{{ site.baseurl }}/assets/image03.png" alt="image03" />

A simple use for a pipeline is to glue bits of documents together. Lots of web pages have a common top and bottom and special content in the middle. It's very similar to referencing in Microstation or Xrefs in AutoCad.

<a href="/wordpress/wp-content/uploads/2015/08/image04.png" rel="attachment wp-att-1848"><img class="alignright size-full wp-image-1848" src="{{ site.baseurl }}/assets/image04.png" alt="image04" /></a>

The image above is a bit more complicated. Several <a href="http://sass-lang.com/">SCSS</a> files are joined together, much like referenced drawings. The next steps do extra things, there aren't really good metaphors in the way we make drawings. The SCSS is converted to CSS[19. scss is a format that is more concise and easier to read, but the internet needs css, so scss can be converted into css for the computer to read. A bit like a drawing being converted to postscript for the printer to read.] then that CSS is minified [20. minification takes out all the concessions to human readability and makes things as small as is feasibly possible. e.g. from

<code>.box-style{<br />
color: red;<br />
}<br />
to:<br />
<code>.box-style{color:red;}</code></code>

The computer sees each space as a character. This is a toy example, but over a 1000 line file you can make big file-size savings by removing all the things that aid human readability, which translates into faster websites.].

Let me try and explain why I think that this is important to to the work that we do as architects. I'm talking generally about pipelines, everything from making drawings, to getting new people started, to getting things onto the website or even filling the dishwasher!

With the asset pipeline that I mentioned above (Grunt) each step is delegated to a task. That task fulfils a contract. It expects to be provided with source material in a certain format, it will then provide and output in a certain format. By breaking down the tasks like this it's easy to see where it is going wrong. The task that is breaking its contract will cause an error in the next task in the chain.

The ‘contract' that each part of the pipeline[21. or link in the value chain or whatever you want to call it.] agrees to means that you can think of that part as a box. As long as it fulfills its agreement then you don't need to worry about how.

<a href="/wordpress/wp-content/uploads/2015/08/image02.jpg" rel="attachment wp-att-1850"><img class="size-full wp-image-1850 alignnone" src="{{ site.baseurl }}/assets/image02.jpg" alt="image02" /></a>

&nbsp;
<p class="c2 c4 c25"><a href="http://www.google.com/url?q=http%3A%2F%2Fwww.chem4kids.com%2Ffiles%2Fbio_enzymes.html&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNGD-692o6iIs83aLNDP3BGhTvXbgg">Enzymes are a nice metaphor </a>- they take something and return something else.

To think of our work as tasks with contracts isn't all that natural. We tend to think of our work to be governed by a contract between us and an external party. The work we do internally is more fluid. I'm not advocating that we should start writing contracts between each other! If you stop to think, that contract is already there. It's just in the form of a tacit agreement.

If you ask me to do something and I agree then we've made a contract that you'll provide me with some input and I'll provide you some output. If I break it you can't sue me, but you can be annoyed and change your opinion of me. As a side note, when I see really good delegators working their wording fits this pattern[1. really _really_ good delegators make people think it was their idea all along!].
<blockquote>
"I'll give you this, and then you'll do that and give it to so-and-so by this time."
</blockquote>

There are two main reasons I think that this is important to us.

Firstly it clarifies communication and understanding in a team. If I am clear about what I'm expected to do then I stand a much better chance of doing it well.

The second thing is about automation. If you see each of your tasks as discrete steps then<a href="http://notionparallax.co.uk/wordpress/?p=1768"> they are easier to delegate to another human</a> or <a href="http://www.bruno-latour.fr/sites/default/files/35-MIXING-H-ET-NH-GBpdf_0.pdf">non-human agent</a>.

It can make your life easier even if you aren't delegating. Imagine that your present self and future self are different people. Present me is often annoyed with past me for doing something stupid. That's unavoidable, but if you do something lazy and future you has to clean up then that's extra annoying. If you make a deal with future-you that you'll do it right then you'll stay happy.
<hr />


[^1]: really _really_ good delegators make people think it was their idea all along!

