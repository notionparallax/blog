---
layout: post
title: Drawing a bell curve
date: 2010-01-24 21:43:50.000000000 +11:00
type: post
published: true
status: publish
categories: []
tags:
- GC

---
<p>I've got to Illustrate why questions on a questionnaire need to be of a range of difficulties. If they are all too hard then the distribution of answers will all be pushed up to one end, and too easy, the opposite. So I needed to <a href="http://en.wiktionary.org/wiki/yak_shaving">shave a yak</a> until I had a good way to show this.</p>
<p>I parallel-posted this on the GC forum too, so if I'm going to be forced to open IE to post to the GC forum, I thought I'd do a decent job of it.</p>
<p>Below is the GCscript that draws a bell curve. It is almost entirely based on Daniel Shiffman's processing code on his website at  <a href="http://www.shiffman.net/teaching/nature/week-1/">http://www.shiffman.net/teaching/nature/week-1/</a></p>
<p>It is driven by a point that controls the standard deviation (**?**<sup>**2** </sup>width of the bell) and the offset from zero (**?**) .</p>
<p>There are a few other variables, but these just change the size of the curve.</p>
<p>See how you get on with it and if it is at all useful.</p>
<p><img title="Bell Curve" src="{{ site.baseurl }}/assets/original.aspx" border="0" alt="this is a few versions of the bell curve under different transformations" width="490" /></p>
<p>the code is after the fold </p>
<pre name="code" class="c-sharp">
transaction modelBased 'draw a bell curve'
{
    feature User.Objects.baseCS Bentley.GC.CoordinateSystem
    {
        SymbolSize                = 10;
    }
    feature User.Objects.width Bentley.GC.GraphVariable
    {
        Value                     = 100;
    }
    feature User.Objects.point02 Bentley.GC.Point
    {
        CoordinateSystem          = baseCS;
        XTranslation              = <free> (51.55);
        YTranslation              = <free> (-3.22);
        ZTranslation              = 0.0;
    }
    feature User.Objects.point01 Bentley.GC.Point
    {
        Function                  = 
    function (CoordinateSystem CS, double varX, double width, double xcoord, double amplification, double widthAmp)
    {
       /* 2010 01 24 Ben Doherty 
        * This function draws a bell curve
        * it is based on Daniel Shiffman's processing code
        * http://www.shiffman.net/teaching/nature/week-1/
        * the comments are his*/

        //"e", see http://mathforum.org/dr.math/faq/faq.e.html for more info
        double e = 2.71828183;                 
        //a list to store all the "y" values
        double normal = {};                    
        //default mean of 0 
        double m = 0;                          
        //standard deviation based on varX, driven here by the position of a point
        double sd = (0.5 + varX)/width;        

        //double xcoord = -3;                  
        //uncomment to start the graph at -3, i.e. centred
        for (int i = 0; i < ToInt(width); ++i)
        {
            //square root of 2 * PI
            double sq2pi = Sqrt(2*PI);                
            //-(x - mu)^2
            double xmsq = -1*(xcoord-m)*(xcoord-m);   
            //variance (standard deviation squared)
            double sdsq = sd*sd;                      
            //P(x) function
            normal[i] = (1 / (sd * sq2pi)) * (Pow(e, (xmsq/sdsq)));  
           //increment x coordinate
            xcoord += 6 / width;                      
        }
        //breakpoint;
        Point graphPoints = new Point();
        graphPoints.ByCartesianCoordinates(CS,Series(0,width,1)*widthAmp,normal*amplification,0);
        return graphPoints;
    };
        FunctionArguments         = {baseCS,point02.X,width, point02.Y, 100, 3};
    }
}
</free></free></pre>
