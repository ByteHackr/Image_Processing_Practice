# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:31:51 2019

@author: BILU
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Scan1.jpg')

img_height , img_width , dim = img.shape


for i in range(0,int(img_height)):
	for j in range(0,int(img_width)):
			img[i][j] = img[i][j][0]*0.21+ img[i][j][1]*0.72 + img[i][j][2]*0.07

plt.subplot(1,2,1)
plt.title("Gray Image")
plt.imshow(img)
plt.subplot(1,2,2)            
plt.hist(img.ravel(),256,[0,256]) 
plt.show()

#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
