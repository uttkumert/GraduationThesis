import cv2
import numpy as np
import glob
import os
from os.path import isfile, join 
import re
import time

img_array = []
pathIn = 'C:/Users/aslil/Desktop/NEW/' #Please fix the path path = this .py path
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
files.sort(key = lambda x: str(x[:-4]))
files.sort()

pre_imgs = os.listdir(pathIn)
img = []


for filename in glob.glob('C:/Users/aslil/Desktop/NEW/*.jpg'): #Please fix the path path = this .py path
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    time_ = 15 #time for each page
    for k in range (time_):
        img_array.append(img)
out = cv2.VideoWriter('test.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 1, size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

time.sleep(45)

files = glob.glob('./*.jpg', recursive=True)

for f in files:
    try:
        os.remove(f)
    except OSError as e:
        print("Error: %s : %s" % (f, e.strerror))

files2 = glob.glob('./*.pdf', recursive=True)

for f2 in files2:
    try:
        os.remove(f2)
    except OSError as e:
        print("Error: %s : %s" % (f2, e.strerror))
