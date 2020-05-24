# Python 3.6 (v3.6.3:1880cb95a742, Jan 16 2019, 16:02:32) 
# Type "copyright", "credits" or "license()" for more information.
# >>> Code by A.M

from PIL import Image
import cv2

import os

im_dir = "output/"
files = [i for i in os.listdir(im_dir) if i.endswith(".jpg") or i.endswith(".png")]
print(files)
for file in files:
	im = Image.open(im_dir + file)
	pix_val = list(im.getdata())
	

	l=[]
	l1=[]
	
	for i in pix_val:
		if 0 == i:
			l1.append(i)
		else:
			l.append(i)

	# for i in pix_val:
	# 	if (36,25,25)<i and (70,255,255)>i:
	# 		l.append(i)
	# 	else:
	# 		l1.append(i) 


	print("file:",file)
	print("Leaf:",len(l))
	print("Image:",len(pix_val))
	sum = len(l)/len(pix_val)
	print("Area:",sum*100)
	print('----------------------')