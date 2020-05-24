# Python 3.6 (v3.6.3:1880cb95a742, Jan 16 2019, 16:02:32) 
# Type "copyright", "credits" or "license()" for more information.
# >>> Code by A.M

import cv2
import os
import numpy as np

im_dir = 'images/'
files = [i for i in os.listdir(im_dir) if i.endswith(".jpg") or i.endswith(".png")]

for file in files:
## Read
	img = cv2.imread(im_dir+file)

	ORANGE_MIN = np.array([32, 50, 50],np.uint8)
	ORANGE_MAX = np.array([60, 255, 255],np.uint8)

	hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	frame_threshed = cv2.inRange(hsv_img, ORANGE_MIN, ORANGE_MAX)

## save 
	cv2.imwrite("output/" + file, frame_threshed)