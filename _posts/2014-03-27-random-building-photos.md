---
layout: post
title: random building photos
date: 2014-03-27 00:00:07.000000000 +11:00
type: post
published: true
status: publish
categories: []
tags: []
description:

---
<p>I'm not sure if I've mentioned it, but I've been working on a project at work to organise as much of our information as we can, a bit like Goggle organising all the world's information, but _WAY_ smaller in scope. It's called <a href="https://github.com/notionparallax/ShadowWolf">Shadow wolf</a>.</p>
<p>We're using the excellent ruby library <a href="http://faker.rubyforge.org/">Faker</a> to fill the database up with pretend people and projects so that the tests don't freak out and so that we know what sort of shape the layout needs to be.</p>
<p>We've been using the randomuser.me service (and probably breaching their terms) to get mugshots of people by calling:</p>
<p><code>{ 'http://api.randomuser.me/0.2/portraits/' + ['women','men'].sample + '/' + (1..60).to_a.sample.to_s + '.jpg' }</code></p>
<p>To produce a random face.</p>
<p>We needed a similar source of building photos, so I pulled a bunch off flickr and probably breached their terms too (but they were all cc licenced), so we can now call:</p>
<p><code>{ 'http://notionparallax.co.uk/bldg/bld-' + ['women','men'].sample + '/' + (0..248).to_a.sample.to_s + '.jpg' }</code></p>
<p>To get any of 248 photos of buildings. In the spirit of these things, if you want to use them too, then just go ahead.</p>
<p>The pattern is http://notionparallax.co.uk/bldg/bld-**NUMBER**.jpg so it's pretty easy to use. Let me know if you find yourself using it, if there's enough interest I'll look into serving specific sized pictures, just like my favourite web service, <a href="http://placekitten.com/">placekitten</a>.</p>
<p><img class="aligncenter" alt="" src="{{ site.baseurl }}/assets/300" width="500" height="300" /></p>
