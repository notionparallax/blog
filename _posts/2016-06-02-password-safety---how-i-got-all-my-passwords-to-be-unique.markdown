---
layout: post
title: Password safety – how I got all my passwords to be unique and managed
date: 2016-06-02 13:00:00   PDT
type: post
published: true
status: publish
categories: []
tags: []

#this goes on the index page, and into facebook shares
description: A boring post about getting all your passwords to be unique and complicated

# This is what twitter will pick up if someone tweets the link to this page 
# 110 marker 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
twitter-body: How I got all my passwords to be unique and managed
#Twitter and facebook will pick up this image. you can also use it in a post with:
# ![alt text]({{ site.baseurl }}/assets/{{page.featuredimg}}) 
featuredimg: 16/HolyGrail.jpg
---

<figure class="half-width right">
![](http://imgs.xkcd.com/comics/password_reuse.png)
<figcaption>
[XKCD](https://xkcd.com/792/), mandatory
</figcaption>
</figure>
Password entropy and password reuse is a pretty boring topic. It's a bit like eating enough vegetables and flossing. It's something that we _should_ do something about, but it's a bit unpleasant.

I'm in the camp that thinks that passwords are a terrible idea in general[^1]. Given that I need to live in some kind of real world I need a way to solve the problem. Most people I talk to say that they use the same 2-3 passwords for everything. Sometimes they use some kind of rule to decide what the password is. E.g. for Facebook it'd be `myBasePasswordFB` or something a bit crap like that. There are loads of Coding [H](https://blog.codinghorror.com/your-password-is-too-damn-short/)[o](https://blog.codinghorror.com/i-just-logged-in-as-you-how-it-happened/)[r](https://blog.codinghorror.com/the-dirty-truth-about-web-passwords/)[r](https://blog.codinghorror.com/youre-probably-storing-passwords-incorrectly/)[o](https://blog.codinghorror.com/passwords-vs-pass-phrases/)[r](https://blog.codinghorror.com/passphrase-evangelism/)[^3] posts that talk about how your default password is basically useless. The general advice is that you need at least 12 characters of password, and that length trumps weirdness. This means that `R3m0+3`[^2] is for total chumps, and everyone's favourite [`correcthorsebatterystaple`](http://correcthorsebatterystaple.net/) is pretty good. However, `Mjvbm5U2ezbPrRLIokeG` kicks both of them to death. My memory is like a sieve; I struggle to remember my own phone number so I'm not going to remember a long, high entropy string.

Recently I started using LastPass to manage all my passwords. It turns out that starting to do this can either be gratingly unpleasant, or not too bad. At the _gratingly unpleasant_ end of things, you get yourself locked out of all your accounts, you lose access to important things, you have to do endless and meaningless clicking; it's generally very shit. At the _not too bad_ end of the scale, you just need to get used to a clunky UI.

Here's how I did it:

## Summary
1. Get all your passwords into Lastpass
2. Get someone else to change them for you
3. [Profit](http://knowyourmeme.com/memes/profit)

## Ingredients
* Chrome
* LastPass account
* Fancy hands account (I have way too many tasks unused, so if you ask me nicely I'll give you some)
* a bit of spare time

## Method

1. Whenever Chrome offers to save a password for you, let it. Do this for a good few months. This is like the 'pre heat the oven' step. You are using the magic of the browser's own password manager to harvest all your existing passwords so that you don't have to do it manually. (There's a pretty good chance you already do this, so you can skip this step.)
2. You've spent a few months doing this. Chrome is logging you in quite happily everywhere you go. You are ready to get busy with a password manager. Sign up for LastPass, pay them the money (you can get it for free, but it's not worth the pain). Download the Chrome extension, the phone app and the desktop app and sign up for all of them. This is probably the most painful part. I've done this on Windows (not too bad), Linux (OK) and Mac (a huge pain in the balls), so you pays your money, you takes your chances.
3. When you are signing up for LastPass, use a password like `myTemporaryPassword69dude` or something else that you are OK with giving to someone you don't know. I'll explain why in a few steps time.
3. Get LastPass to import your passwords from chrome. It's an option as part of the import.
4. At this point you have all your accounts in LastPass, but they are pairs like <br>`Facebook.com =>myStandardCrapPassword1` and <br>`my-job.com =>myStandardCrapPassword1` and <br>`my-bank.com =>myStandardCrapPassword1`.<br>See the pattern here? They are all managed but the same. LastPass claims that it can auto change passwords, but it's slow and only works about 1/10 of the time. You are ready to get _serious_ now. 
5. **Optional step:** export all your passwords to a spreadsheet and go through them. There are some that you just don't care about any more. You can delete them from LastPass to save a bit of time on changing them later. I didn't bother doing this, but it'll save you some money. (If you like money more than time.)
6. Now you go to Fancyhands. Here's a task template based on the one that I used:
    <style type="text/css">
        .fancy-hands-template {
            margin: 0 8em 0 3em;
            font-size: 90%;
            background-color: beige;
            padding: 1em 2em;
        }
    </style>
    <div class="fancy-hands-template">
    Hi, 

    I use lastpass (https://lastpass.com/) to manage my passwords. It has sucked up all my passwords. Some are already unique and random, but others are still the same.
    
    I'd like you to change all the non-unique passwords to lastpass generated ones.    
    
    To log into lastpass use my email (**put your email in here**) and this password: myTemporaryPassword69dude    
    
    If you have a root around you'll find the security challenge. That will give you a list of the bad passwords.    
    
    I'd like you to log in to each account and change it to a strong password using the lastpass generator. In the end the security challenge should show as few duplicate passwords as possible.    
    
    Exclusions: (**Put in anything that they won't be able to access, or you don't want them to touch. In my case, this was my work accounts.**).    
    
    Feel free to use up to 5 tasks, then let me know how it's going and I'll unlock more if you need them.
    
    Thanks!
    </div>
7. Now begins the teething trouble. Over the next few days your apps will start to log you out as your passwords change. You'll need to get accustomed to the LastPass UI and its foibles. It makes a big difference if you have fingerprint unlock, and if not that then setting up a pin make sit much easier.
8. Eventually, FancyHands will get back to you and either ask for more tasks, or to say that they are done. Now change your LastPass master password to something really secure. I use a phrase that's about 60 characters long; that has lots of entropy but is easy enough to remember.

By this point you are all set! You are secure, you'll probably want to get 2 factor auth set up on your email because if someone gets in there you are still stuffed.

[^1]: They are a bit of a path dependency thing, like QUERTY. Things like social login, and the idea of [security providers](https://diogomonica.com/posts/password-security-why-the-horse-battery-staple-is-not-correct/) is good. The WhatsApp login method is fantastic, particularly the way that they handle logging into your account on desktop. Some people have suggested that putting all your eggs in one basket is bad, but the basket that your eggs are in is usually your email provider (at least in Google's case) and if someone compromises your email account you are deeply screwed anyway because all password reset requests go via your inbox.

[^2]: I've seen this used as a real password, by people who really should have known better. It's _remote_ in leet if you were wondering.

[^3]: Yep, that's one article per letter in horror, that guy just loves to write about passwords!