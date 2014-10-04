
all: fframes

webm:
	ffmpeg -i aurelia_aurita.mp4 -vcodec libvpx -crf 10 -b:v 2M -an jelly.webm

fframes:
	ffmpeg -i aurelia_aurita.mp4 -an -f image2 "frames/frame_%03d.png"

clean:
	rm -f frames/*.png
