---
layout: post
title: Voting for a group
date: 2015-07-30 08:35:23.000000000 +10:00
type: post
published: true
status: publish
categories: []
tags:
- analysis
- BVN
- geek
- graphs
- Shane Dalton
- Voting
description:
meta:
  _publicize_facebook_user: http://www.facebook.com/541400612
  _publicize_twitter_user: "@notionparallax"
  _thumbnail_id: '1831'
  _wpas_mess: Voting for a group - some thoughts and observations and stuff

has-math: true
---
<style type="text/css">
    iframe {
      width: 100%;
      height: 390px;
      border: none;
    }
    .payload {
      font-size: 60%;
      line-height: 1;
    }
</style>

<p class="lead">Voting for one person is complicated enough. Electing a group of people is a surprisingly difficult job! Here's some work we did recently at BVN to elect a group of 13 people.</p>
<p><span id="more-1811"></span></p>
<p>As with all the stuff I do, I'm sure this has been studied to death, by some field or other. If anyone knows what the field is called then I'd love to know.</p>
<p>Throughout this, when I'm talking about "we" I mean Shane Dalton, a 15 year old work experience student who was with me for two weeks, and me.</p>
<p>What we were trying to develop is called a "multiple winner voting system" which hasn't been studied very much[^1] as far as I can tell.</p>
<p>Let's start by stating our goals:</p>
<ol>
<li>We want to elect 13 people</li>
<li>Those people should have equal status</li>
<li>There should be no ambiguity about membership of the group</li>
<li>The results should be <a href="http://en.wikipedia.org/wiki/Condorcet_criterion">reflective of the electorate's aggregate opinion</a>.</li>
</ol>
<p>One and two can easily be handled by an unbiased returning officer. We had a great one, her job was to interpret the results and release 13 names. (In no particular order.)</p>
<p>The hard part is in making her job easy. We need to be able capture the electorate's preferences. This isn't as easy as it sounds!</p>
<p>Kenneth Arrow was the youngest person ever to get a Nobel prize for economics. His <a href="http://en.wikipedia.org/wiki/Kenneth_Arrow#Arrow.27s_impossibility_theorem">impossibility theorem</a> proves[^2] that no voting system is perfect, or in the words of wikipedia:</p>
<blockquote><p>In short, the theorem states that no rank-order voting system can be designed that always satisfies these three "fairness" criteria:</p>
<ul>
<li>If every voter prefers alternative X over alternative Y, then the group prefers X over Y.</li>
<li>If every voter's preference between X and Y remains unchanged, then the group's preference between X and Y will also remain unchanged (even if voters' preferences between other pairs like X and Z, Y and Z, or Z and W change).</li>
<li>There is no "dictator": no single voter possesses the power to always determine the group's preference.</li>
</ul>
</blockquote>
<p>This is actually pretty freeing for us! It means that we can just rank different methods of choosing people.</p>
<p>We've tested 4 methods of voting and ranked them on the same dimensions.</p>
<ol>
<li>one vote per voter</li>
<li>13 votes per voter</li>
<li>Preference voting (order the candidates)</li>
<li>Currency allocation voting</li>
</ol>
<p>These all result in an ordering of candidates, so it's possible to see who is the most popular and least, but for our use we just need to trim off the top 13. We couldn't come up with a model that elected whole groups[^3].</p>
<p>We didn't expect number one to work, but we included it to give some indication of how it fares against more complicated methods[^4].</p>
<p>From our exploration we've found that the factor that matters from a voting point of view is the distinction between 13<sup>th</sup> and 14<sup>th</sup> place. We need to make sure that the method we pick is unlikely to give a tie. Imagine how miffed Xavier be if he missed out on his place in the council to Aaron because of a secondary sorting choice; that wouldn't be acceptable.</p>
<p>The other criteria we need to think about is how hard it is to actually vote correctly. Remember the fuss about the hanging chad[^5] problem in the <a href="http://en.wikipedia.org/wiki/Bush_v._Gore">Bush Gore</a> election. That whole election may have gone differently if the voting method was more reliable.  </p>
<p>Most voting systems need to cope with people of wide ranging abilities (language, mental capacity, physical capacity). We're really lucky to only need to design this system for a fairly narrow group of capacities. We do have one major problem though–scarce attention makes us stupid. This system needs to work for geniuses who are only able to give it a small proportion of their full brain power.</p>
<h1>The systems</h1>
<h2>Method</h2>
<p>We've used 220 voters and 62 candidates. We ran each test 200 times and used the <a href="https://docs.python.org/2/library/random.html">Python random number generator</a> for all our randomness. If you'd like to read the code then it's <a href="https://github.com/bvn-architecture/voting">available here</a> (open source of course – never trust a closed source voting system, it's almost certainly corrupt!)</p>
<h2>One vote per voter</h2>
<p>In this system each person gets one vote. They then use it to say who they think is the best person for the job. We take the 13 people who have the most votes and they become the council.</p>
<p>This is a familiar voting method for most things, but in our context it has some huge problems! In most voting situations there are thousands of voters; that makes the ratio of candidates to voters tiny. In our case that ratio is more like 1:4. It would be sort-of-ok if we were only voting for one person, but for 13 it's a disaster.</p>

<iframe src="https://docs.google.com/spreadsheets/d/1YFYyntVfz4Z-jARA5lHeFqp_yK4PY0RcjJp6lgc2T0M/pubchart?oid=1897012938&amp;format=interactive" >
:(
</iframe>

<p>This is a really pretty graph, but that's about all it's got going for it. Out of 200 sample runs of this election it gave a tie between 13<sup>th</sup> and 14<sup>th</sup> place 189 times. So 94.5% of the time this method failed to give us what we were looking for.</p>
<h2>Thirteen votes per voter</h2>
<p>This is the closest we've got to electing the group as a whole, un-preferentially. Fans of direct mappings between metaphor and implementation will probably be drawn to this. It's a bit better than the previous method at avoiding clashes, but it's still not really _good enough_ (131 out of 200 or 65.5% of the time it will give a clash).</p>

<iframe src="https://docs.google.com/spreadsheets/d/1YFYyntVfz4Z-jARA5lHeFqp_yK4PY0RcjJp6lgc2T0M/pubchart?oid=787908325&amp;format=interactive" >
:(
</iframe>

<h2>Preference ordering</h2>
<p>We're in serious consideration territory now. This method is very similar to the way voting works in Australia[^6] It works by reordering a list of candidates, so that the person at the top gets a point, second place gets 2 points etc. Then the 13 people with the lowest number of points form the council.</p>

<iframe src="https://docs.google.com/spreadsheets/d/1YFYyntVfz4Z-jARA5lHeFqp_yK4PY0RcjJp6lgc2T0M/pubchart?oid=357940176&amp;format=interactive" >
:(
</iframe>

<p>The downfall of this model is that if you vote below the line you need to number all the boxes. We've got around this by introducing a line that you can move about yourself. All candidates below the line get the average value of the points left over. We've simulated this by randomly placing the line somewhere between 5 and 30 candidates down. This gives an excellent clash avoidance of 6 out of 200 or 3%</p>
<h2>Currency allocation</h2>
<p>This is the method that Shane and I both liked the best from an intuitive point of view. You are given lots of voting tokens, 100 in this case. You then ‘spend' them on candidates. You might want to give 25 to 4 candidates, or 10 to 10 candidates, or 50 to one, and five to another ten people. The idea is that you are given a lot of expressiveness.</p>

<iframe src="https://docs.google.com/spreadsheets/d/1YFYyntVfz4Z-jARA5lHeFqp_yK4PY0RcjJp6lgc2T0M/pubchart?oid=229529167&amp;format=interactive" >
:(
</iframe>

<p>This is pretty good, but not as good as preference ordering, giving 35 out of 200 or 17.5% clashes.</p>
<h1><img class="alignright size-full wp-image-1816" src="{{ site.baseurl }}/assets/high-five-gif-4.gif" alt="high-five-gif-4">Summary of results</h1>
<table>
<tbody>
<tr>
<td>One vote per voter</td>
<td>94.5%</td>
</tr>
<tr>
<td>Thirteen votes per voter</td>
<td>65.5%</td>
</tr>
<tr>
<td>Preference ordering</td>
<td>3.0%</td>
</tr>
<tr>
<td>Currency allocation</td>
<td>17.5%</td>
</tr>
</tbody>
</table>
<p>This is a pretty clear win for preference ordering. Preference ordering also has the benefit of being well understood by Australian voters and an easily implemented UI for when we actually need to implement it!</p>
<h1>Known problems</h1>
<p>All this analysis is done with unbiased picking. What that means is that there's no reason to pick one candidate over another. Imagine that we were electing a group of the tallest people, that's an objective ordering, so our voting simulation should reflect that objective reality as closely as possible. If there really wasn't anything to chose between the candidates we might as well have a lottery. These simulations are assuming that situation. I'd like to spend more time running these with biased picking, but undifferentiated candidates are a worst case so it should only get better from there.</p>
<hr>
<p>Now we know what sort of voting procedure will suit us the best, we need to be able to actually do the voting. As I said above we are dealing with the scarce resource of attention. We need a system that:</p>
<ol>
<li>Is simple enough for children to use (let's the spare attention is about equivalent to a 7 year old)</li>
<li>Can be used anywhere (not locked behind a firewall) so that people can vote at home or on the train etc.</li>
<li>Doesn't require much maintenance or developer skill (I had to make it, and to call myself a hobbyist is probably rude to hobbyists)</li>
</ol>
<p><a href="https://bvn-architecture.github.io/voting">Here's what we ended up with</a>, It's only tested in Chrome because that's the only browser we have at work[^7]. I also made it have a print stylesheet so that it could be filled in by people who are _totally_ technophobic. Turns out that after staying exceptionally late to make this happen a grand total of ZERO votes were submitted on paper. Oh well.</p>
<p>We've since used this to vote for a photo competition too, so it's pretty reusable. Here's the instructions I gave everyone. I thought I'd leave them more or less unchanged, mainly because I'm lazy.</p>
<p> </p>
<h1>How to vote – simple</h1>
<ol>
<li>First thing to do is to go to the voting page, but keep reading and _then_ go.</li>
<li>When you get there you'll see a list of people with some buttons next to them.<br>
<a href="{{ site.baseurl }}/assets/voting.png"><img class="alignnone size-full wp-image-1818" style="background-color: black; border-radius: 1em;" src="{{ site.baseurl }}/assets/voting.png" alt="voting"></a></li>
<li>You can reorder them by clicking–or tapping–the buttons</li>
<li>Make sure you've put in your email address</li>
<li>Press **Submit vote**</li>
<li>Go about your business</li>
</ol>
<p>You can do this on your phone, tablet or on your regular computer. If you are afraid of technology you can also do a paper vote. To print a paper voting form–or to see all the candidates at once–go to the voting form and press [ctrl]+[p] to print one.</p>
<h1>How to vote – less simple[^8]</h1>
<p>I'm told that if you vote below the line you need to rank _all_ the parties, that's a bit of a faff, so we've got a movable line.</p>
<a href="{{ site.baseurl }}/assets/movable-line.png"><img class="alignnone size-full wp-image-1820" src="{{ site.baseurl }}/assets/movable-line.png" alt="movable-line"></a>
<p>The all candidates above the red line line will be scored by their position in the list. All candidates below the line get the average of whatever is left over. **Remember that every person who votes affects the ordering of all candidates. That means that your votes beyond the 13 are still important!**</p>
<p>I found that the easiest way to organise candidates is to scroll down the list, sending each person who I think I might like to vote for to the top. Once I get to the bottom I scroll back up to the top and do the detailed work of ordering people precisely. Only when that is done and I've decided who I'm voting for do I move the red line to level off the rest of the candidates.</p>
<h1>How to vote – detailed</h1>
<p>The red line stuff can be a bit confusing. I find this diagram useful:</p>
<a href="{{ site.baseurl }}/assets/voting-ave-points.gif"><img class="alignnone size-full wp-image-1819" src="{{ site.baseurl }}/assets/voting-ave-points.gif" alt="voting-ave-points"></a>
<p> </p>
<p>Until the red line everyone gets an increasing score according to their ordering. Once the red line is placed we pivot the score through the middle of the leftover part of the line and give everyone who is left the same score. If you are mathematically inclined:</p>

$$uniformScore = \frac{numberOfCandidates - cutoffPoint}{2} + cutoffPoint$$

<p>The data from the votes gets sent to a spreadsheet through a google form. A sample payload looks like this:</p>
<p><code class="payload">{"aaa_email":"ben_doherty@bvn.com.au","aaa_timestamp":"2015-06-10T08:59:53.568Z","Chi Tang":0,"Sam Sweeny":1,"Paolo Frigenti":2,"Heather McCabe":3,"Ali Bounds":4,"Rana Abboud":5,"Katherine Withnell":6,"Tony Ogden":7,"Stella DeVulder":8,"Rebeca Buffington":9,"Simon Longstaff":10,"Brian Clohessy":11,"Michael Holt":12,"Damian Eckersley":13,"Bianca Smith":14,"Rob Vider":15,"Simon Swain":16,"Kellie Newman":17,"Mark Gazy":18,"Joanna Newton":19,"Jared Bird":43,"Caren Mok":43,"Glenn Millar":43,"Irina Belova":43,"Tim Gibson":43,"Barry Cantor":43,"Kristin Neise":43,"Tim Crawshaw":43,"Max Rampertshammer":43,"Palina Zhalniarovich":43,"Nikita Notowidigdo":43,"Chris Bickerton":43,"James Scott":43,"Graham Bligh":43,"Bella Pescia":43,"David McGirr":43,"Paul Wintour":43,"Catherine Skinner":43,"Naomi Stead":43,"Danielle McParland":43,"Domino Risch":43,"Glenn Irwin":43,"Luke Chalmers":43,"Izzie White":43,"Mitchell Medway":43,"Morten Weaver":43,"Nicholas Crawford":43,"Domenic Mesiti":43,"Craig Burns":43,"Nick Flutter":43,"Neil Haybittel":43,"Hayley Sainsbury":43,"Joseph O'Meara":43,"Ben Doherty":43,"Rose Steadman":43,"Gary Cai":43,"Kim Small":43,"Glenn Bliesner":43,"Jonathan Capparelli":43,"Abbie Lewis":43,"Sarah Barnes":43,"Kat Martindale":43,"Katherine Wiedersehn":43,"Marco Montevecchi":43,"Kirby Rees":43,"Kerwin Datu":43}</code></p>
<p>It's then processed by the spreadsheet into columns. The totals of those columns are taken and the lowest 13 scores are elected.</p>
<p>If you'd like do some scrutineering of your own, all the code for the voting and simulations is <a href="https://github.com/bvn-architecture/voting/tree/gh-pages">all here on Github</a>. Feel free to fork it if you need to elect some people. Let me know and I'll even give you a sanitised copy of the spreadsheet, it's got some sweet graphs in it[^9].</p>
<h1>Results</h1>

<iframe src="https://docs.google.com/spreadsheets/d/1wrb3CTOrbR5B3tvxDNKUV1YjtMECXu_7-T9DqvoaQUY/pubchart?oid=27970589&amp;format=interactive" >
:(
</iframe>

<p>This is how our ordering turned out, it was similar to the simulation, but more biased. In retrospect that makes sense, with more votes going where aggregate opinion went. There wasn't a draw, and everyone is happy!</p>

[^1]: compared to single winner voting systems. See <a href="http://ijcai.org/papers07/Papers/IJCAI07-238.pdf">Multi-Winner Elections: Complexity of Manipulation, Control, and Winner-Determination</a> and <a href="http://www.cs.cmu.edu/~yairzick/papers/tiesmulti_aamas.pdf">On Manipulation in Multi-Winner Elections Based on Scoring Rules</a> for an idea of how freaky it all is. 

[^2]: if you know me, you'll know how particular I am about using the word "prove"! 

[^3]: we could have had people form parties, but there aren't really enough people to make enough parties so they'd need to overlap, which would be really hard 

[^4]: Or in more salty language, to show that it's crap and that we're not idiots for not including it. 

[^5]: Justices Breyer and Souter stated: <q>It is true that the Equal Protection Clause does not forbid the use of a variety of voting mechanisms within a jurisdiction, even though different mechanisms will have different levels of effectiveness in recording voters' intentions; local variety can be justified by concerns about cost, the potential value of innovation, and so on. But evidence in the record here suggests that a different order of disparity obtains under rules for determining a voter's intent that have been applied (and could continue to be applied) to identical types of ballots used in identical brands of machines and exhibiting identical physical characteristics (such as "hanging" or "dimpled" chads).<q>

[^6]: or so I'm told, I'm not allowed to vote. 

[^7]: we also have IE, apparently, but that's no a browser is it? 

[^8]: but still pretty damned simple! 

[^9]: watching those graphs writhe about as more people voted was fascinating! 