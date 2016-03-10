---
layout: post
title: lists to trees
date: 2009-03-02 02:08:22.000000000 +11:00
type: post
published: true
status: publish
categories: []
tags:
- GC
- geek
description:
meta:
dsq_thread_id: '4503552113'

---
<p>Gennaro asked me about data structures to contain a tree for his genetic programming in GC (little does he know how clueless I am about data structures), and I recommended a nested list.</p>
<p>It seemed sensible to me, so I set about turning a nested list into a tree diagram, and I have to admit that there were moments that I doubted the plausibility of it, but it turned out OK in the end!</p>
<p>The way to look at it seems to be that you work from the outside in. The outside set of brackets is the root, and then everything inside that is a terminal, with this rule re-applied recursively for each time another list is found.</p>
<p><embed src="Images/list-to-tree.swf" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/shockwave/download/" width="500" height="500"></embed></p>
<p>You can read this diagram either way, as turning a list into a tree, or the other way arround.</p>
