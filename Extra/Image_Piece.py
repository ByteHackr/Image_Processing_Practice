# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:34:40 2019

@author: RIMPA
"""
import numpy as np
import cv2

"""
div=4
img = cv2.imread('Penguins.jpg',1)

height, width, channels = img. shape

new_height=(int)(1+height/div)
new_width=(int)(1+width/div)

img1 = np.zeros((new_height,new_width,3), np.uint8)


for i in range(div):
	for j in range(div):
		for ih in range(new_height):
    			for iw in range(new_width):
       				img1[ih][iw]=(img[min(height-1,i*new_height+ih)][min(width-1,j*new_width+iw)])
		name="CROP/Penguins"
		name =name+str(i)
		name =name+str(j)
		name =name+".jpg"
		cv2.imwrite((name.format(i,j)),img1)
"""
