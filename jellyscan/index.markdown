---
layout: article
title: Jellyscan
---

# Jellyscan

I took this video of a jellyfish swimming:

<video autoplay loop preload="auto" style="max-height: 400px;" class="col-sm-12">
 <source src="jelly.webm" type="video/webm">
</video>

And broke it out into a bunch of png images, one for each frame in the video.

    $ ffmpeg -i aurelia_aurita.mp4 -an -f image2 "frames/frame_%03d.png"


