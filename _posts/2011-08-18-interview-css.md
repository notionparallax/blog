---
layout: post
title: Interview CSS
date: 2011-08-18 08:34:17.000000000 +10:00
type: post
published: true
status: publish
categories: []
tags:
- CSS
- internet
- trick

---
<p>If you were looking for some wise words about Brazilian electro then I'm terribly sorry :(</p>
<p><a href="http://www.notionparallax.co.uk/wordpress/wp-content/uploads/2011/08/cssUL.jpg"><img class="alignright size-full wp-image-757" title="This is a grab, but you can see it for real after the jump" src="{{ site.baseurl }}/assets/cssUL.jpg" alt="" width="265" height="146" /></a>I'm typing up some interviews at the moment, and while I was doing my dip thesis (a long time ago) I read an <a href="http://www.alistapart.com/articles/taminglists/">a list apart</a> article about lists and styling lists. At the same time I was using a javascript library to do the verification on my forms written by <a href="http://tetlaw.id.au/">Andrew Tetlaw</a>. By a stroke of such enormous coincidence that I was really very surprised by it, Andrew is now the web guy for BVN. </p>
<p>We talked through some stuff today and thought that you could make a CSS selector that would do the normal interview typesetting without too much effort.</p>
<ul class="interview">
<li>Can we do this with CSS?</li>
<li>yes, it's easy</li>
<li>I'm too stupid, show me how</li>
<li>here you go:</li>
</ul>
<pre>/*style applied to the whole interview*/
ul.interview{
  list-style: none;
  margin-bottom: 0.8em;
  list-style-position: outside;
}
/*interviewer bullet*/
ul.interview li:nth-child(odd)::before {
  content: 'BD ';
  color: rgb(0, 200, 0);
}
/*interviewer text*/
ul.interview li:nth-child(odd) {  
  color: rgb(0, 100, 0);
}
/*interviewee bullet*/
ul.interview li:nth-child(even)::before {
  content: 'JA ';
  color: rgb(200, 0, 0);
}
/*interviewee text*/
ul.interview li:nth-child(even) {
  color: rgb(100, 0, 0);
}
/*each line in the interview*/
ul.interview li{
  margin-bottom: 0.8em;
}</pre>
<p>There's a load more tidying up that you could do with hanging indents and stuff, but that's the basics of it.<br />
Here's something that Andrew wrote about <a href="http://reference.sitepoint.com/css/pseudoclass-nthchild">nth child CSS selectors</a> [Actually he says he was _just_ the technical editor]</p>
<p>The really flare thing to do would be to have first and second lines showing the full name, and then 3<sup>rd</sup> onwards showing initials.</p>
<p>P.S. The CSS in this post is made possible by using the <a href="http://wordpress.org/extend/plugins/scripts-n-styles/">scripts n styles</a> plugin for wordpress.</p>
