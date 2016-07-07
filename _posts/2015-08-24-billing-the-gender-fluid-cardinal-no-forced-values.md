---
layout: post
title: Billing the gender fluid Cardinal – no forced values
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
<style type="text/css">
  .sidebar {
      width: 60%;
      display: block;
      float: right;
      transform: translateX(2em);
      background-color: hsla(0, 0%, 0%, 0.1);;
      padding: 1em;
    }
</style>

<img class="alignright wp-image-1851" src="{{ site.baseurl }}/assets/image01.png" alt="image01" width="146" height="200" />I touch on this in <a title="Fluid categories – define things by their attributes not their name" href="http://tropos.bvn.com.au/2015/02/27/taxonomy/">my Fluid categories post</a>. I think it's worth expanding on. Traditional databases are designed to serve one master–technological constraints.

Think the typical drop down list on a survey. If the correct answer isn't one of the two options you huff and puff for a minute, look for the field where you can type your answer, you can't find it, so you close the survey and vow never to do another survey again. Technology has moved past these sorts of constraints. Unfortunately the technology hasn't filtered down to _all_ the people who design human-computer interfaces [^1].

A good example of forced values is SQL style databases[^2]. They were designed specifically to deal with the extortionate price of storage [^3]. This constraint is no longer relevant, so we are able to abstract away how the database actually works; to make it invisible to the user[^4].

Sadly those same non-HCI (Human Computer Interaction) people who deal with interactions learned to think in terms of tables and rows. This leads to a “leaky abstraction”.

Why am I talking about abstractions and tables leaking? Where are they leaking from? Where are they leaking to?

This long introduction is to prepare you for why the next part of the story is so hard.

_Imagine a future where [@pontifex](https://twitter.com/Pontifex) gets rid of his silly, dudes-only rule for his club. One of the new cardinals hires us to redo their walk in wardrobe. (Better lighting to tell between different shades of red.)_

_The cardinal is now a client of ours. We get them to fill in their details for our billing database. The interface looks like this:_

![]({{ site.baseurl }}/assets/image00.jpg)

_Immediately we are stuck! Our mate the cardinal identifies as “fluid gender”[^5]. Ideally the entry would allow for male, female and fluid gender[^6], but just _fluid gender_ would do in a pinch[^7]._

_The interface is driving a fixed set of results: either ‘male' or ‘female'. The idea of tables, rows and fixed sets of options has leaked into the designer's thinking . This is a leaky abstraction._

_It's a sad situation, but the cardinal says a serenity prayer and moves on. “First name” is unproblematic, but then they get to “title”. They've put in a lifetime of dedicated work to get that title. They aren't about to let some snotty database person push them around. (╯°□°）╯︵ ┻━┻. Rage quit. Fire BVN!_

<div class="sidebar">
## Gardening and folding

Gardening, in the sense of pulling out the weeds and tending to the flowers, is applicable to databases too. If a user has put in things that we don’t want, but make sense, then we need to find ways to fix that. The first line of defence is to support them to make good inputs though typeaheads. If that fails then the Database gardener will look for ways to keep the semantics alive.

Gardening is for when something is wrong. The gardener will find _sydney_ and convert it to _Sydney_.

![](/assets/accent-folding.png)

Folding is more nuanced. It is for when words all point to the same concept, but for one reason or another are written differently. E.g. USYD, Sydney Uni, University of Sydney etc. They are all valid, so we might make a mapping between all the words and their shared concept.

This is a very grey area. It’s where style guides come in handy, but also a good dose of common sense. Good examples of style guides breaking things are when Fairfax Media write out _Royal Melbourne Institute of Technology_, when RMIT has explicitly stated that their name is not an acronym. BVN is in exactly the same boat!
</div>

This story is only slightly silly. We come across this sort of problem all the time. We'll find it more as we go international. Buildings in the USA, UK, NZ or Thailand don't have BCA classes so we can't force the field to be 1-9 and some letters.

Let's try and tie these two things together.

1. Doing things in a way that suits the database is outdated. The database is our servant! We should revel in this brief period between the start of tech-abundance and skynet.
1. Real life is always richer than a database designer can imagine.
1. I'm going to pull in a quote from <a href="http://www.amazon.com/Work-Rules-Insights-Inside-Transform/dp/1455554790">Lazlo Bock's book Work Rules</a>:

    > “If you believe people are good then you must be unafraid to share information with them”

    This point is going to be an extension of that. If you believe people are good then you must be unafraid to share information _creation_ with them.

Forcing options by using drop down menus avoids people doing crazy stuff like spelling their state wrongly or filling in their religion as Jedi[^8] on the census. You also pollute your data with information that's “_close enough_ ”, which is a euphemism for “_wrong_ ”!

Misspellings and other ways of referring to a common concept can be fixed with gardening and folding[^9]. Data that is flat-out wrong is invisible. If someone chooses “glass” instead of putting in a support request to a DBA[^10] to get “self cleaning glass” added to the options then that data is wrong and can only be fixed by someone with domain specific knowledge[^11],[^12].

In conclusion, enforcing particular data values creates bad data and bad will. It’s a practice that is almost never a good idea.



[^1]: As an aside, I have a huge amount of respect for HCI designers. Their work is so rigorous and evidence based. Unfortunately, as we love to complain about in our own profession, not all human-computer interfaces are designed by HCI people. Especially unfortunately, this is disproportionately prevalent in ‘enterprise' software like MS word or the old Lotus Notes . My assumption for why this occurs is that the person procuring and paying for the software is very rarely the person who ends up using it.

[^2]: Technical: I know that this is technically incorrect, but the use of normalised tables to prefill constrained dropdowns is painfully common. I know that this problem can be caused by _any_ database, but none of the others have a mental model that _encourages_ it.

[^3]: In 1992 a 1GB hard drive would set you back about $2000US. <a href="http://www.jcmit.com/diskprice.htm">Check out this dry, but still fascinating table of storage price since 1955</a>!

[^4]: Technical: This post doesn't seek to denigrate the technology of relational databases. They have a lot of benefits. The declarative nature of SQL as a language feels like magic. What I am saying is that it is absurd--in a world of technological abundance--that the nature of the storage layer should be allowed to affect the design of the interface. The job of the interface is to protect the users' brains from the underlying technology.

[^5]: This is a toy example. In reality our client's genders are none of our business (literally and figuratively). We therefore don't need that bit of information.

[^6]: Chris sent me these excellent links to this exact topic. <a href="http://itspronouncedmetrosexual.com/2012/06/how-can-i-make-the-gender-question-on-an-application-form-more-inclusive/">How you can make the gender question on an application form more inclusive</a> and <a href="https://illinois.edu/blog/view/25/110232">Facebook multiplies genders but offers users the same three tired pronouns</a>. These two are great too: <a href="http://blog.codinghorror.com/doing-terrible-things-to-your-code/">doing terrible things to your code </a> &amp; <a href="http://www.cscyphers.com/blog/2012/06/28/falsehoods-programmers-believe-about-gender/">falsehoods programmers believe about gender.</a>

[^7]: Technical: This is a really tricky problem for database design, but it's not technically tricky only cognitively tricky. The field needs to be able to contain multiple values, where those values are defined by the user. The job of the database is to support the user in storing _true_ information. If it isn't doing this then it is failing. We currently handle this is a couple of ways in P+P. Most obviously in tag style fields. E.g. BCA classification.

[^8]: Although there's nothing wrong with that!

[^9]: This is where you equate two characters to make them easy to find, but store them differently to make the data accurate! This image is from [this nice article](http://alistapart.com/article/accent-folding-for-auto-complete). ![](/assets/accent-folding.png)

[^10]: DBAs are usually portrayed as the classic IT troll who lives under a bridge and eats people.

[^11]: Usually the only person with domain knowledge that specific is the person who first put the data into the database!


[^12]: I talk about how categories are defined in the fluid categories post. The key point that I want to hammer home is: _“Categories are an emergent way of describing set creation operations based on attributes”_