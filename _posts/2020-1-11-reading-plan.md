---
layout: post
title: "A more diverse 2020 reading list"
date: 2020-1-12 9:00:00 AEST
type: post
published: true
status: publish
categories: []
tags: []
author-name: Ben Doherty

# this goes on the index page, and into facebook shares
description: "I'm trying to plan 2020's reading to balance the diversity; can you help?"

# This is what twitter will pick up if someone tweets the link to this page
# 110 marker 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
twitter-body: "I'm trying to plan 2020's reading to balance the diversity; can you help?"
# Twitter and facebook will pick up this image. you can also use it in a post with: -
#![alt text]({{ site.baseurl }}/assets/{{page.featuredimg}})
featuredimg: https://notionparallax.co.uk/assets/19/goodreads/clumsyDiversity.png
---

<style>
.planned:before {
    background-color: silver;
    content: "planned";
}
.finished:before {
    background-color: hsl(174, 100%, 29%);
    content: "finished";
}
.in-progress:before {
    background-color: hsl(199, 100%, 48%);
    content: "in-progress";
}
.Looking-for-suggestions:before {
    background-color: hsl(30, 100%, 48%);
    content: "still looking";
}
.planned:before,
.finished:before, 
.in-progress:before,
.Looking-for-suggestions:before {
    display: block;
    font-size: 50%;
    height: 100%;
    left: 0;
    margin-right: 1em;
    position: absolute;
    text-align: center;
    top: 0;
    transform: translateX(-3.6em);
    width: 3.6em;
    writing-mode: vertical-rl;
}
.planned, 
.finished,
.in-progress,
.Looking-for-suggestions {
    position: relative;
}
#plotly_div {
    height: 85vh;
}
article.post dt {
    width: 50%;
    text-align: right;
    padding-right: .5em;
    min-height: 2em;
}
article.post dd {
    width: 49%;
}
</style>

<script></script>

Based on [how poorly I did](https://notionparallax.co.uk/2019/goodreads2019) with reading a diverse set of authors last year, even with an explicit plan to try harder to _read books by people who are not like me_, I thought I'd try a quota approach.

<figure class="half-width right">

![]({{ site.baseurl }}/assets/19/goodreads/compound_diversity_Fic_Nonfic.png)

<figcaption>
This is my reading habits for the last few years; pretty unbalanced. If I use a quota for this year's reading, the graph will be flat across all categories.
</figcaption>

</figure>

I used the categories that I used in the [analysis of last year's books](https://notionparallax.co.uk/2019/goodreads2019), which were:

-   Book is [fiction \| non-fiction]
-   Book age is [under 2 years old \| 2&ndash;15 years old \| over 15 years old]
-   Author is a [woman \| man]
-   Author is [black \| white \| Asian \| Hispanic]

That's 2&times;3&times;2&times;4=48 books. The more I look at these categories the more uncomfortable they make me, but given the combinatorial explosion of going deeper into the implications of intersectionality, I'm not sure my life is long enough. This seems like a good enough start as an experiment.

I really enjoyed reading a lot of [Ursula K. Le Guin](https://www.goodreads.com/author/show/874602.Ursula_K_Le_Guin), [N.K. Jemisin](https://www.goodreads.com/author/show/2917917.N_K_Jemisin) and [Octavia E. Butler](https://www.goodreads.com/author/show/29535.Octavia_E_Butler) last year, so I imagine that the trend of enjoyment will continue with increased diversity. (Fingers crossed.)

I'm going to need help finding these books to read, so I made a [spreadsheet that actually drives this page (it's here)](https://docs.google.com/spreadsheets/d/17dwAQMFu06MTK5rBdIMrXkCEu2d1yfmte0YuWHCqIrk/edit?usp=sharing). You can put comments on that if there's categories that you have a suggestion for.

If you need some idea of what I have been reading, here's [2019](https://www.goodreads.com/user_challenges/14706992) and [2018](https://www.goodreads.com/user_challenges/11862761).

---

<script src='https://cdnjs.cloudflare.com/ajax/libs/tabletop.js/1.5.1/tabletop.min.js'></script>
<script type='text/javascript'>    
  var publicSpreadsheetUrl = 'https://docs.google.com/spreadsheets/d/17dwAQMFu06MTK5rBdIMrXkCEu2d1yfmte0YuWHCqIrk/edit';

  function init() {
    Tabletop.init( { key: publicSpreadsheetUrl,
                     callback: showInfo,
                     simpleSheet: true } )
  }

  function showInfo(data, tabletop) {
    // console.log(data);
 
    htmlText = [];
    data.forEach(d=>{
        let by = "";
        if(d.authorName1 !== undefined && d.authorName1 != ""){
            if(d.authorName2 == ""){
                by = `by <a href="${d.authorLink}">${d.authorName}</a></dd>`
            } else {
                by = `by <a href="${d.authorLink}">${d.authorName}</a> and <a href="${d.authorLink2}">${d.authorName2}</a></dd>`
            }
        }
        htmlText.push(`<dt class="${d.status}">${d.fnf}, ${d.race} ${d.sex} author, ${d.age}</dt>`)
        htmlText.push(`<dd><a href="${d.bookLink}">${d.bookName}</a> ${by}`)
    });
    container = document.getElementById("book_list_div");
    container.insertAdjacentHTML("afterbegin", htmlText.join(" "));

    let fnf = [...new Set(data.map(x=>x.fnf))];        //["Fiction", "Non-fiction"];
    let age = [...new Set(data.map(x=>x.age))];        //["<2yo", "2–15yo", ">15yo"];
    let sex = [...new Set(data.map(x=>x.sex))];        //["Woman", "Man"];
    let race = [...new Set(data.map(x=>x.race))];      //["Black", "White", "Asian", "Hispanic"];
    let status = [...new Set(data.map(x=>x.status))];  //
    cats = [fnf, age, sex, race];
    labels = [];
    parents = [];
    colours = []
    cats[0].forEach(a => {
    labels.push(a);
    parents.push("");
    colours.push("");
    cats[1].forEach(b => {
        labels.push(`${a}:${b}`);
        parents.push(a);
        colours.push("");
        cats[2].forEach(c => {
        labels.push(`${a}:${b}:${c}`);
        parents.push(`${a}:${b}`);
        colours.push("");
        cats[3].forEach(d => {
            let book = data.filter(x=>x.fnf==a && x.age==b && x.sex == c && x.race == d)[0];
            console.log(data);
            
            labels.push(`${book.status}:<br>`+
                        `${a}:<br>`+
                        `${b}:<br>`+
                        `${c}:<br>`+
                        `${d}:<br>`+
                        `${book.bookName}<br>`+
                        `${book.authorName}`);
            parents.push(`${a}:${b}:${c}`);

            cols = [
                "hsl(30, 100%, 48%)",  //"Looking-for-suggestions"
                "hsl(174, 100%, 29%)", //"finished"
                "silver",              //"planned"
                "hsl(30, 100%, 48%)"   //"in-progress"
            ]
            colours.push(cols[status.indexOf(book.status)]);
        });
        });
    });
    });
    // console.log("labels", labels);
    // console.log("parents", parents);

    treemapData = [
    {
        type: "treemap",
        labels: labels,
        parents: parents,
        marker: {colors: colours}
    }
    ];

    Plotly.newPlot("plotly_div", treemapData, {scrollZoom: true, editable: true});

  }

  window.addEventListener('DOMContentLoaded', init)
</script>

<script src='https://cdn.plot.ly/plotly-latest.min.js'></script>
<div id='plotly_div'><!-- Plotly chart will be drawn inside this DIV --></div>
<div id='book_list_div'><!-- Book list will be dropped inside this DIV --></div>
