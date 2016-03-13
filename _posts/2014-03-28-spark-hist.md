---
layout: post
title: Spark hist
date: 2014-03-28 04:47:55 +11:00
type: post
published: true
status: publish
categories: []
tags: []
description: "Ever need a histogram in a spreadsheet?▁░░░▃░▁▅▁█ █▄▁▁▂▃▇▆▂░ ▁▄▁▃▃▂▂█▂░ █░▃▂█▁▅▁░▁ ▂░░░░▄▆█▅░ ▄░▁▁▃░█▅▁▁ ▆▂▁░▃▁▄▇█▁ ▇▆█▅▅▃▄▅▂░ ▂█▃▂▂▂▄█▂"
meta:
  _wpas_mess: |-
    Spark hist http://wp.me/p3wwRK-pz
    ▁░░░▃░▁▅▁█
    █▄▁▁▂▃▇▆▂░
    ▁▄▁▃▃▂▂█▂░
    █░▃▂█▁▅▁░▁
    ▂░░░░▄▆█▅░
    ▄░▁▁▃░█▅▁▁
    ▆▂▁░▃▁▄▇█▁
    ▇▆█▅▅▃▄▅▂░
    ▂█▃▂▂▂▄█▂

---
<p>We did a survey at work recently. It had 72 ten-point-scale responses and I needed a quick way of seeing the distribution of people's scores.</p>
<p>Inspired by <a href="http://zachseward.com/sparktweets/">spark tweets</a> I made a little Google spreadsheet function (embedded Gist below) that makes cells that contain this kind of thing:</p>
<p style="text-align: center;">▁░░░▃░▁▅▁█<br />
█▄▁▁▂▃▇▆▂░<br />
▁▄▁▃▃▂▂█▂░<br />
█░░░░░░░░░<br />
█░▃▂█▁▅▁░▁<br />
█▁▂░▁░░░░░<br />
▂░░░░▄▆█▅░<br />
█░▁░░▁▁░░░<br />
█▁▂▁▁░▁▁░░<br />
█░░░░░░░░░<br />
█░░░░░░░░░<br />
█▂▂▁▁░▁░░░<br />
█░░░░░░░░░<br />
▄░▁▁▃░█▅▁▁<br />
▆▂▁░▃▁▄▇█▁<br />
█▁░░▁░▂▁░░<br />
█▅▄▆▁▂▅░▁▁<br />
▇▆█▅▅▃▄▅▂░<br />
█░░░░░░░░░<br />
▂█▃▂▂▂▄█▂</p>
<p>It's pretty limited in that it only handles numbers between 1 and 10, and has fixed bin widths of 1, but it get the job done for my needs. If you are interested in using it and don't know how to put it into your spreadsheet or want it to do something else then just let me know in the comments.</p>
<p><script src="https://gist.github.com/notionparallax/9044181.js"></script></p>
