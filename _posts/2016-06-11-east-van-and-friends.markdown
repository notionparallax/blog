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
    label {
      margin-top: 1em;
      display: inline-block;
    }
    #diy-cross-box {
      background-color: black;
      display: inline-block;
      height: 30em;
      margin-bottom: 2em;
      padding-top: 1em;
      text-align: center;
      width: 50%;
    }
    #diy-cross-box .cross-frame {width: 70%;}
    #cb-manual {
      display: inline;
      width: 2em;
    }
    .diy-input-box {
      display: inline-block;
      padding-left: 1em;
      vertical-align: top;
      width: 48%;
    }
</style>

<div class="diy-box">
<div id="diy-cross-box"></div>
<div class="diy-input-box">

# DIY

If you want to make your own, go right ahead. It'll find you a matching word for whatever you put in.

<label for="across">Across<input type="" name="across"></label>
<label for="down">Down<input type="" name="down"></label>
<!-- <label><input type="checkbox" id="cb-basic"  value="basic" > Basic</label><br> -->
<label for="cb-manual">Full manual<input type="checkbox" id="cb-manual" value="manual"></label>

Tick this if you want to be able to write in both boxes without it generating you the other word.
</div>
</div>

<figure class="half-width right">
![A can of beer that says Craft Lager in the style of the east van sign]({{ site.baseurl }}/assets/16/tinny.png)
<figcaption>
Looks like everyone's on the band wagon
</figcaption>
</figure>

We were having [ramen for lunch](https://drive.google.com/file/d/1xPCi3ebZ6V-9p6F4Z5M48Z_s5h_3eMnd3w/view?usp=sharing)[^1], and I saw a can of beer doing the [East Van sign](https://en.wikipedia.org/wiki/East_Van_Cross) thing. I started wondering how many other things you could do that way.

It turns out that you can actually make a LOT of these things. I downloaded a word list and did a bit of magic processing. If you aren't interested in the how, and just want to look at the funny combinations of words then skip over all the words to follow and just look at the pictures! They are generated live, so just keep hitting refresh for a new set.

One thing that has struck me is just how many of these words _seem_ to have a relationship. Making patterns is so baked into the brain!

I downloaded a list of [English words](https://github.com/dwyl/english-words) that has over 350k words in it. It really shows because I have no idea what about half of these words mean. <strike>It'd be interesting to see what comes up if I used Basic English.</strike> **Edit:** _I actually did add the [Basic English](https://en.wikipedia.org/wiki/Basic_English) list; the crosses it pumps out are amazing!_ I then processed these words into two sets of bins; one for the horizontal words and one for the vertical words.

Horizontal words need to have an odd number of letters and be more than three letters long. Vertical words just need to be more than 4 letters long. They are then 'binned' or grouped by the letter at the crossing. That's the middle letter for horizontal words and the second letter for vertical ones.

[^1]: That's my sketches on a chopstick wrapper. I was also faffing about with the [ESPN penis](https://www.buzzfeed.com/mrloganrhoades/fan-made-penis-sign-shown-on-live-tv-to-nations-delight) thing too.

# Basic English

<div id="cross-box"></div>
<div id="definitions"></div>

# Hard English

Here's some from the full list of english words:

<div id="hard-cross-box"></div>
<div id="hard-definitions"></div>

The [repo for all of this is here](https://github.com/notionparallax/east-van). Thanks to dwyl for the [english-words](https://github.com/dwyl/english-words).

<figure>
![The East Van Sign at night]({{ site.baseurl }}/assets/{{page.featuredimg}})
<figcaption>
From [“…that’s gangster and now the whole world will see…”](https://matthewjvandeventer.wordpress.com/2010/01/)
</figcaption>
</figure>

<script type="text/javascript">
// "use strict";
document.addEventListener("DOMContentLoaded", function(event) { 
  
  function triggerDIY(direction, input) {
    var words, letter, complementWord, url;
    input = input.trim();
    if (input.length >= 3) { //&& input.length % 2 == 0 fuck it, lets be permissive
      $("#diy-cross-box").html("");
      if (direction == "across"){
        words  = window.simple_words.vwords; //move this out if perf is an issue
        letter = input[Math.floor(input.length / 2)];
      } else {
        words  = window.simple_words.hwords;
        letter = input[1];
      }
      if($("#cb-manual").is(':checked')){
        if (direction == "across"){
          complementWord = $('input[name=down]').val();
        } else {
          complementWord = $('input[name=across]').val();
        }
      } else {
        complementWord = getWord(words, letter, 9);
      }

      if (direction == "across"){
        $('input[name=down]').val(complementWord);
        addNewCross(input, complementWord, "#diy-cross-box");
        url = `/2016/east-van-and-friends#diy?a=${input}&d=${complementWord}`;
      } else {
        $('input[name=across]').val(complementWord);
        addNewCross(complementWord, input, "#diy-cross-box");
        url = `/2016/east-van-and-friends#diy?a=${complementWord}&d=${input}`;
      }
      console.log(url);
      history.pushState({},"NP generator",url);

    }
  }

  function setDIY () {
    //Setup
    if(window.location.hash){
      var params = window.location.hash.split("?")[1].split("&");
      var a = params[0].split("=")[1]
      var d = params[1].split("=")[1]
      $('input[name=across]').val(a);
      $('input[name=down]'  ).val(d);
      addNewCross(a, d, "#diy-cross-box");
    } else{
      $('input[name=across]').val("Van");
      $('input[name=down]'  ).val("East");
      addNewCross("van", "east", "#diy-cross-box");
    }
    // action
    $('input[name=across]').on('input', function() {
      triggerDIY("across", $(this).val());
    });
    $('input[name=down]').on('input', function() { 
      triggerDIY("down", $(this).val());
    });
  }

  function addEverything (fileName, numberOfCrosses, hCharLimit, vCharLimit, defContainer, crossContainer) {  
    var App = {};
    $.getJSON(`/js/posts/east-van/h${fileName}.json`,  function( data ) { 
        App.hwords = data;
    
        $.getJSON(`/js/posts/east-van/v${fileName}.json`,  function( data ) { 
            App.vwords = data;
            var alphabet = "abcdefghiklmnoprstuvwxy";//jqz removed bezause simple english doesn't have any words in those bins
            for (var i = 0; i < numberOfCrosses; i++) {
              var random_letter = alphabet[Math.floor(Math.random()*alphabet.length)] ;
              var hword = getWord(App.hwords, random_letter, hCharLimit);
              var vword = getWord(App.vwords, random_letter, vCharLimit);
              console.log(random_letter, hword, vword);
              addNewCross (hword, vword, crossContainer);
              addDefinitions(hword, vword, defContainer);
            }
        });
    });
    window[fileName] = App;
  }
  addEverything("simple_words", 11, 7, 8, "#definitions", "#cross-box");
  addEverything("words", 12, 7, 8, "#hard-definitions", "#hard-cross-box");

  function getWord(words, letter, limit){
      var wordLength = 100;
      var word = "";
      while (wordLength>limit) {
        try{
          word = words[letter][Math.floor(Math.random() * words[letter].length)];
          wordLength = word.length;
        }
        catch(e){
          console.log(e, word, letter);
          break;
        }
      }
      return word;
  }

  function addDefinitions(hword, vword, selector){
      $(selector).append(`<ol class='definition'>
                          <li><a href='${"http://www.thefreedictionary.com/"+vword}' target='_blank'>${vword}</a></li>
                          <li><a href='${"http://www.thefreedictionary.com/"+hword}' target='_blank'>${hword}</a></li>
                          </ol>`);
  }

  function addNewCross (h_test_word, v_test_word, container){
      h_test_word = h_test_word.toUpperCase();
      v_test_word = v_test_word.toUpperCase();
       
      var h_letters = h_test_word.length;
      var v_letters = v_test_word.length;
       
      var rad = 8;
      var pad = 9;
      var box = 50;
       
      var vll = (0) + pad;
      var vlm = (Math.floor(h_letters/2) * box) + pad;
      var vrm = (vlm + box) + pad;
      var vrr = (h_letters * box) + pad;
       
      var htt = (0) + pad;
      var htm = (box) + pad;
      var hlm = (box * 2) + pad;
      var hll = (v_letters * box) + pad;
       
      var v_nudge = 7;
       
      var blur = 5;
      var letter_pad = "    "; //blur stops at box boundary, this makes the box bigger
      var blur_colour = "hsla(180,70%,52%,1)";

      var svg_head = `<svg viewbox=\"0 0 ${vrr+(2*pad)} ${hll + (2 * pad)}\" xmlns=\"http://www.w3.org/2000/svg\">`;
      var svg_filter = `<filter id=\"blurMe\">
                          <feGaussianBlur in=\"SourceGraphic\" 
                                          stdDeviation=\"${blur}\" 
                                          x="-50%" 
                                          y="-50%" 
                                          width="280%" 
                                          height="280%"/>
                        </filter>`;
      var svg_bg = `<rect x=\"0\" y=\"0\" width=\"${vrr + (2 * pad)}\" height=\"${hll + (2 * pad)}\" fill=\"black\" />`;

      var path = `M${vll + rad} ${htm}`+ //1       
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

      var svg_path = `<path id=\"glow_path\" d=\"${path}\" stroke=\"${blur_colour}\" stroke-width=\"10\"`+
                     `fill=\"rgba(255, 255, 255, 0.55)\" opacity=\"0.6\" filter=\"url(#blurMe)\"></path>`+
                     `<path id=\"main_path\" d=\"${path}\" stroke=\"white\" `+
                     `fill=\"none\" stroke-width=\"2\" fill-opacity=\"0.5\"></path>`;


      var svg_text = ""
      for (let index = 0, len = h_test_word.length; index < len; index++) {
        var letter = h_test_word[index];
        svg_text += `<text class=\"blur-text\"   text-anchor=\"middle\" x=\"${vll + index*box + (box/2)}\" y=\"${hlm - v_nudge}\" font-size=\"${box}\" font-family=\"sans-serif\" fill=\"${blur_colour}\" filter=\"url(#blurMe)\">${letter_pad}${letter}${letter_pad}</text>`;
        svg_text += `<text class=\"bright-text\" text-anchor=\"middle\" x=\"${vll + index*box + (box/2)}\" y=\"${hlm - v_nudge}\" font-size=\"${box}\" font-family=\"sans-serif\" fill=\"white\">${letter_pad}${letter}${letter_pad}</text>`;
      }

      for (let index = 0, len = v_test_word.length; index < len; index++) {
        var letter = v_test_word[index];
        if(index !== 1){
          svg_text += `<text class=\"blur-text\"   text-anchor=\"middle\" x=\"${vlm + box/2}\" y=\"${htt + (index*box)+box - v_nudge}\" font-size=\"${box}\" font-family=\"sans-serif\" fill=\"${blur_colour}\" filter=\"url(#blurMe)\">${letter_pad}${letter}${letter_pad}</text>`;
          svg_text += `<text class=\"bright-text\" text-anchor=\"middle\" x=\"${vlm + box/2}\" y=\"${htt + (index*box)+box - v_nudge}\" font-size=\"${box}\" font-family=\"sans-serif\" fill=\"white\">${letter_pad}${letter}${letter_pad}</text>`;
        }
      }

      var svg = svg_head + 
                svg_filter + 
                svg_bg + 
                svg_path +
                svg_text +
                "</svg>"

      //let container = document.getElementById("cross-box");
      $(container).append("<div class='cross-frame'>"+svg+"</div>");
  }

  setDIY ();
  addNewCross   ("craft", "lager", "#cross-box");
  addDefinitions("van", "east", "#definitions");
  addDefinitions("craft", "lager", "#definitions");
});
</script>
