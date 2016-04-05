---
layout: post
title: granularity
date: 2009-04-21 04:26:03.000000000 +10:00
type: post
published: true
status: publish
categories: []
tags:
- ecotect
- geek

---
<p>I've been telling people that turning up the analysis resolution on their Ecotect models is a bad idea, but I'd never stopped to figure out just how bad.</p>
<p>This table shows the rate at which the numbers grow as you go up through the resolution steps.</p>
<table class="ta1" border="0" cellpadding="3" cellspacing="3">
<tr class="ro1">
<td class="ce1"></td>
<td bgcolor="#ccffff">Sky<br />
subdivision</td>
<td bgcolor="#ccffff">
<p align="right">Lowest<br />
15° x 15°</p>
</td>
<td bgcolor="#ccffff">
<p align="right">Low<br />
10° x 10°</p>
</td>
<td bgcolor="#ccffff">
<p align="right">Medium<br />
5° x 5°</p>
</td>
<td bgcolor="#ccffff">
<p align="right">High<br />
4° x 3°</p>
</td>
<td bgcolor="#ccffff">
<p align="right">Highest<br />
2° x 2°</p>
</td>
</tr>
<tr>
<td bgcolor="#ffffcc">Grid subdivisions</td>
<td>Number<br />
of divisions</td>
<td style="text-align: right">144</td>
<td style="text-align: right">324</td>
<td style="text-align: right">1296</td>
<td style="text-align: right">2700</td>
<td style="text-align: right">8100</td>
</tr>
<tr>
<td bgcolor="#ffffcc">Low - 1</td>
<td>1</td>
<td style="text-align: right" bgcolor="#99ffcc">144</td>
<td style="text-align: right" bgcolor="#99ffcc">324</td>
<td style="text-align: right" bgcolor="#99ffcc">1296</td>
<td style="text-align: right" bgcolor="#99ffcc">2700</td>
<td style="text-align: right" bgcolor="#99ffcc">8100</td>
</tr>
<tr>
<td bgcolor="#ffffcc">Medium 5 x5</td>
<td>25</td>
<td style="text-align: right" bgcolor="#99ffcc">3600</td>
<td style="text-align: right" bgcolor="#99ffcc">8100</td>
<td style="text-align: right" bgcolor="#99ffcc">32400</td>
<td style="text-align: right" bgcolor="#99ffcc">67500</td>
<td style="text-align: right" bgcolor="#99ffcc">202500</td>
</tr>
<tr>
<td bgcolor="#ffffcc">High - 10 x 10</td>
<td>100</td>
<td style="text-align: right" bgcolor="#99ffcc">360000</td>
<td style="text-align: right" bgcolor="#99ffcc">810000</td>
<td style="text-align: right" bgcolor="#99ffcc">3240000</td>
<td style="text-align: right" bgcolor="#99ffcc">6750000</td>
<td style="text-align: right" bgcolor="#99ffcc">20250000</td>
</tr>
<tr>
<td bgcolor="#ffffcc">Full - 25 x 25</td>
<td>625</td>
<td style="text-align: right" bgcolor="#99ffcc">225000000</td>
<td style="text-align: right" bgcolor="#99ffcc">506250000</td>
<td style="text-align: right" bgcolor="#99ffcc">2025000000</td>
<td style="text-align: right" bgcolor="#99ffcc">4218750000</td>
<td style="text-align: right" bgcolor="#99ffcc">12656250000</td>
</tr>
</table>
<p>For those of you who are a bit rusty on your powers of ten (like me), that bottom right number _is_ **12.5 billion!** That's for each panel, so if you have a 5x5 subdivision on a grid, that'd be into the _trillions_ of calcs for your analysis. No wonder it takes a long time.</p>
<p>I thought I'd check to see if I was supposed to be using British billions, or American billions, and it turns out (<a href="http://en.wikipedia.org/wiki/Long_and_short_scalesB">Long_and_short_scales</a>) that all billions have been the same in the English speaking world since 1974!</p>
