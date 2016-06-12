---
layout: post
title: East Van and friends
date: 2016-06-11 19:00:00   PDT
type: post
published: true
status: publish
categories: []
tags: []

#this goes on the index page, and into facebook shares
description: How many words can you pair up like the East Van Sign?

# This is what twitter will pick up if someone tweets the link to this page 
# 110 marker 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
twitter-body: How many words can you pair up like the East Van Sign?
#Twitter and facebook will pick up this image. you can also use it in a post with:
# ![alt text]({{ site.baseurl }}/assets/{{page.featuredimg}}) 
featuredimg: 16/east-van1.jpg
---
<style type="text/css">
    .definition{
        border-bottom: 2px solid;
        display: inline-block;
        width: 25%;
    }
    .cross-frame {
        background-color: black;
        display: inline-block;
        height: 20em;
        text-align: center;
        vertical-align: top;
        width: 33%;
    }
</style>

<figure>
![The East Van Sign at night]({{ site.baseurl }}/assets/{{page.featuredimg}})
<figcaption>
From [“…that’s gangster and now the whole world will see…”](https://matthewjvandeventer.wordpress.com/2010/01/)
</figcaption>
</figure>

<figure class="half-width right">
![A can of beer that says Craft Lager in the style of the east van sign]({{ site.baseurl }}/assets/16/tinny.png)
<figcaption>
Looks like everyone's on the band wagon
</figcaption>
</figure>

We were having [ramen for lunch](https://drive.google.com/file/d/1xPCi3ebZ6V-9p6F4Z5M48Z_s5h_3eMnd3w/view?usp=sharing)[^1], and I saw a can of beer doing the [East Van sign](https://en.wikipedia.org/wiki/East_Van_Cross) thing. I started wondering how many other things you could do that way.

It turns out that you can actually make a LOT of these things. I downloaded a word list and did a bit of magic processing. If you aren't interested in the how, and just want to look at the funny combinations of words then skip over all the words to follow and just look at the pictures! They are generated live, so just keep hitting refresh for a new set.

One thing that has struck me is just how many of these words _seem_ to have a relationship. Making patterns is so baked into the brain!

I downloaded a list of [English words](https://github.com/dwyl/english-words) that has over 350k words in it. It really shows because I have no idea what about half of these words mean. It'd be interesting to see what comes up if I used [simple English](https://en.wikipedia.org/wiki/Basic_English). I then processed these words into two sets of bins; one for the horizontal words and one for the vertical words.

Horizontal words need to have an odd number of letters and be more than three letters long. Vertical words just need to be more than 4 letters long. They are then 'binned' or grouped by the letter at the crossing. That's the middle letter for horizontal words and the second letter for vertical ones.

[^1]: That's my sketches on a chopstick wrapper. I was also faffing about with the [ESPN penis](https://www.buzzfeed.com/mrloganrhoades/fan-made-penis-sign-shown-on-live-tv-to-nations-delight) thing too.

<div id="cross-box"></div>
<div id="definitions"></div>

The [repo for all of this is here](https://github.com/notionparallax/east-van). Thanks to dwyl for the [english-words](https://github.com/dwyl/english-words).

<script type="text/javascript">
"use strict";
    document.addEventListener("DOMContentLoaded", function(event) { 
        var App = {};
        $.getJSON("/js/posts/east-van/hwords.json",  function( data ) { 
            App.hwords = data;
        
            $.getJSON("/js/posts/east-van/vwords.json",  function( data ) { 
                App.vwords = data;
                for (var i = 0; i < 10; i++) {
                  let random_letter = "abcdefghijklmnopqrstuvwxyz"[Math.floor(Math.random()*26)]
                  let hword = getWord(App.hwords, random_letter, 7);
                  let vword = getWord(App.vwords, random_letter, 8);
                  console.log(hword,vword);
                  addNewCross (hword, vword);
                  addDefinitions(hword, vword, "#definitions");
                }
            });
        });
        
        function getWord(words, letter, limit){
            let wordLength = 100;
            let word = "";
            while (wordLength>limit) {
                word = words[letter][Math.floor(Math.random() * words[letter].length)];
                wordLength = word.length;
            }
            return word;
        }

        function addDefinitions(hword, vword, selector){
            $(selector).append(`<ol class='definition'>
                                <li><a href='${"http://www.thefreedictionary.com/"+vword}' target='_blank'>${vword}</a></li>
                                <li><a href='${"http://www.thefreedictionary.com/"+hword}' target='_blank'>${hword}</a></li>
                                </ol>`);
        }

        function addNewCross (h_test_word, v_test_word){
            h_test_word = h_test_word.toUpperCase();
            v_test_word = v_test_word.toUpperCase();
             
            let h_letters = h_test_word.length;
            let v_letters = v_test_word.length;
             
            let rad = 8;
            let pad = 9;
            let box = 50;
             
            let vll = (0) + pad;
            let vlm = (Math.floor(h_letters/2) * box) + pad;
            let vrm = (vlm + box) + pad;
            let vrr = (h_letters * box) + pad;
             
            let htt = (0) + pad;
            let htm = (box) + pad;
            let hlm = (box * 2) + pad;
            let hll = (v_letters * box) + pad;
             
            let v_nudge = 7;
             
            let blur = 10;

            let svg_head = `<svg viewbox=\"0 0 ${vrr+(2*pad)} ${hll + (2 * pad)}\" xmlns=\"http://www.w3.org/2000/svg\">`;
            let svg_filter = `<filter id=\"blurMe\"><feGaussianBlur in=\"SourceGraphic\" stdDeviation=\"${blur}\" /></filter>`;
            let svg_bg = `<rect x=\"0\" y=\"0\" width=\"${vrr + (2 * pad)}\" height=\"${hll + (2 * pad)}\" fill=\"black\" />`;

            let path = `M${vll + rad} ${htm}`+ //1       
                       `L ${vlm - rad} ${htm}`+ //2
                       `A ${rad} ${rad}, 0, 0, 0, ${vlm} ${htm - rad}`+ //3
                       `L ${vlm}  ${htt + rad}`+ //4
                       `A ${rad} ${rad}, 0, 0, 1, ${vlm + rad} ${htt}`+ //5
                       `L ${vrm-rad}  ${htt}`+ //6
                       `A ${rad} ${rad}, 0, 0, 1, ${vrm} ${htt + rad}`+ //7
                       `L ${vrm} ${htm - rad}`+ //8
                       `A ${rad} ${rad}, 0, 0, 0, ${vrm + rad} ${htm}`+ //9
                       `L ${vrr-rad} ${htm}`+ //10
                       `A ${rad} ${rad}, 0, 0, 1, ${vrr} ${htm + rad}`+ //11
                       `L ${vrr} ${hlm-rad}`+ //12
                       `A ${rad} ${rad}, 0, 0, 1, ${vrr - rad} ${hlm}`+ //13
                       `L ${vrm+rad} ${hlm}`+ //14
                       `A ${rad} ${rad}, 0, 0, 0, ${vrm} ${hlm + rad}`+ //15
                       `L ${vrm} ${hll-rad}`+ //16
                       `A ${rad} ${rad}, 0, 0, 1, ${vrm-rad} ${hll}`+ //17
                       `L ${vlm+rad} ${hll}`+ //18
                       `A ${rad} ${rad}, 0, 0, 1, ${vlm} ${hll-rad}`+ //19
                       `L ${vlm} ${hlm+rad}`+ //20
                       `A ${rad} ${rad}, 0, 0, 0, ${vlm-rad} ${hlm}`+ //21
                       `L ${vll+rad} ${hlm}`+ //22
                       `A ${rad} ${rad}, 0, 0, 1,  ${vll} ${hlm-rad}`+ //23
                       `L  ${vll} ${htm+rad}`+ //24
                       `A ${rad} ${rad}, 0, 0, 1, ${vll + rad} ${htm}`;

            let svg_path = `<path id=\"glow_path\" d=\"${path}\" stroke=\"blue\" `+
                           `fill=\"none\" stroke-width=\"2\" fill-opacity=\"0.5\" filter=\"url(#blurMe)\"></path>`+
                           `<path id=\"main_path\" d=\"${path}\" stroke=\"white\" `+
                           `fill=\"none\" stroke-width=\"2\" fill-opacity=\"0.5\"></path>`;


            let svg_text = ""
            for (let index = 0, len = h_test_word.length; index < len; index++) {
              let letter = h_test_word[index];
              svg_text += `<text class=\"blur-text\"   text-anchor=\"middle\" x=\"${vll + index*box + (box/2)}\" y=\"${hlm - v_nudge}\" font-size=\"${box}\" font-family=\"sans-serif\" fill=\"white\" filter=\"url(#blurMe)\">${letter}</text>`;
              svg_text += `<text class=\"bright-text\" text-anchor=\"middle\" x=\"${vll + index*box + (box/2)}\" y=\"${hlm - v_nudge}\" font-size=\"${box}\" font-family=\"sans-serif\" fill=\"white\">${letter}</text>`;
            }

            for (let index = 0, len = v_test_word.length; index < len; index++) {
              let letter = v_test_word[index];
              if(index !== 1){
                svg_text += `<text class=\"blur-text\"   text-anchor=\"middle\" x=\"${vlm + box/2}\" y=\"${htt + (index*box)+box - v_nudge}\" font-size=\"${box}\" font-family=\"sans-serif\" fill=\"white\" filter=\"url(#blurMe)\">${letter}</text>`;
                svg_text += `<text class=\"bright-text\" text-anchor=\"middle\" x=\"${vlm + box/2}\" y=\"${htt + (index*box)+box - v_nudge}\" font-size=\"${box}\" font-family=\"sans-serif\" fill=\"white\">${letter}</text>`;
              }
            }

            let svg = svg_head + 
                      svg_filter + 
                      svg_bg + 
                      svg_path +
                      svg_text +
                      "</svg>"

            //let container = document.getElementById("cross-box");
            $("#cross-box").append("<div class='cross-frame'>"+svg+"</div>");
        }

        addNewCross ("van", "east");
        addNewCross ("craft", "lager");
        addDefinitions("van", "east", "#definitions");
        addDefinitions("craft", "lager", "#definitions");
    });
</script>
