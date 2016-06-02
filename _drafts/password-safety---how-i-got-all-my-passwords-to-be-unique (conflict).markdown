---
layout: post
title: Password safety – how I got all my passwords to be unique
date: 2016-06-02 13:00:00   PDT
type: post
published: true
status: publish
categories: []
tags: []

#this goes on the index page, and into facebook shares
description: 

# This is what twitter will pick up if someone tweets the link to this page 
# 110 marker 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
twitter-body:
#Twitter and facebook will pick up this image. you can also use it in a post with:
# ![alt text]({{ site.baseurl }}/assets/{{page.featuredimg}}) 
featuredimg: rate_your_driver.png
---

<figure class="half-width right">
![](http://imgs.xkcd.com/comics/password_reuse.png)
<figcaption>
[XKCD](https://xkcd.com/792/), probably mandatory
</figcaption>
</figure>
Password entropy and password reuse is a pretty boring topic&mdash;it's a bit like eating enough vegetables and flossing&mdash;it is something that we _should_ do something about.

I'm in the camp that thinks that passwords are a terrible idea in general[^1], but given that I need to live in some kind of real world I was looking for a way to solve the problem. Most people I talk to say that they use the same 2-3 passwords for everything, or that they use some kind of rule to decide what the password is. E.g. for Facebook it'd be `myBasePasswordFB` or something a bit crap like that. There are loads of Coding [H](https://blog.codinghorror.com/your-password-is-too-damn-short/)[o](https://blog.codinghorror.com/i-just-logged-in-as-you-how-it-happened/)[r](https://blog.codinghorror.com/the-dirty-truth-about-web-passwords/)[r](https://blog.codinghorror.com/youre-probably-storing-passwords-incorrectly/)[o](https://blog.codinghorror.com/passwords-vs-pass-phrases/)[r](https://blog.codinghorror.com/passphrase-evangelism/) (Yep, that's one article per letter in horror, that guy just loves to write about passwords!) that talk about how your default password is basically useless. The general advice is that you need at least 12 characters of password, and that length trumps weirdness. This means that `R3m0+3`[^2] is for total chumps, and everyone's favourite [`correcthorsebatterystaple`](http://correcthorsebatterystaple.net/) is pretty good. However, `Mjvbm5U2ezbPrRLIokeG` kicks both of them to death. My memory is like a sieve; I struggle to remember my own phone number so I'm not going to remember a long, high entropy string.

Recently I started using

[^1]: They are a bit of a path dependency thing, like QUERTY. Things like social login, and the idea of [security providers](https://diogomonica.com/posts/password-security-why-the-horse-battery-staple-is-not-correct/) is good. The WhatsApp login method is fantastic, particularly the way that they handle logging into your account on desktop. Some people have suggested that putting all your eggs in one basket is bad, but the basket that your eggs are in is usually your email provider (at least in Google's case) and if someone compromises your email account you are deeply screwed anyway because all password reset requests go via your inbox.

[^2]: I've seen this used as a real password, by people who really should have known better.