#!/usr/bin/env python
import os
import sys
import glob
from PIL import Image


project_directory = "./"
input_directory = "frames/"
output_directory = "output/"
SLIT = 300


input_file_list = sorted(glob.glob(project_directory+input_directory+"*.png"))
n_image = len(input_file_list)


input_im = Image.open(input_file_list[0])
width, height = input_im.size
output_im = Image.new(mode='RGB',size=(n_image, height))


for i, image in enumerate(input_file_list):
    print(i, image)

    image = Image.open(image)
    slit = (SLIT, 0, SLIT+1, height-1)
    line = image.crop(slit)
    paste = (i, 0, i+1, height-1)
    output_im.paste(line, paste)

output_im.save(project_directory+output_directory+"output.jpg","JPEG")
