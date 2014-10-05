---
layout: article
title: Jellyscan
---

# Jellyscan

A [slitscan](http://en.wikipedia.org/wiki/Slit-scan_photography) of a swimming
jellyfish.

## First Try

I starting [this video](https://www.youtube.com/watch?v=o0Us2migjf0) of a
jellyfish swimming:

<video autoplay loop preload="auto" style="max-height: 400px;" class="col-sm-12">
 <source src="jelly.webm" type="video/webm">
</video>

And broke it out into a bunch of png images, one for each frame in the video
with ffmpeg:

    $ ffmpeg -i aurelia_aurita.mp4 -an -f image2 "frames/frame_%03d.png"

Then I chose a line to use as the slit, in this case a vertical line 300 pixels
from the left, right here:

![slit position](images/slit.png)

Then I used python to go through each frame image, copy out a singe line of
pixels and paste them into a new image. This stacked up to create a "slitscan":

![jelly slitscan](images/slitscan.png)

The x-axis (pixel number) of the output image is time! You can see swirling from
the jelly movement show up as "warping" of the suspended particles (little white
dots) in the slitscan.

## Second Try

I combined all these scripts so you can

    $ make run VID=YOUTUBE_URL

and it will make a slitscan (with the slit in the center of the frame.

So [this video](https://www.youtube.com/watch?v=3_oMQZuznyc) gives this scan:

<a href="images/slitscan_tank.png"><img src="images/slitscan_tank.png" class="img-responsive"></a>



