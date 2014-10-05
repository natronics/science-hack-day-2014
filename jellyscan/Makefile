webm:
	ffmpeg -i aurelia_aurita.mp4 -vcodec libvpx -crf 10 -b:v 2M -an jelly.webm

fframes:
	ffmpeg -i aurelia_aurita.mp4 -an -f image2 "frames/frame_%03d.png"

slitscan:
	python slitscan.py

run: clean
	youtube-dl $(VID) -o "video.mp4"
	ffmpeg -i video.mp4 -an -f image2 "frames/frame_%05d.png"
	python slitscan.py

clean:
	rm -f frames/*.png
