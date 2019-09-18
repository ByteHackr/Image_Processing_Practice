# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 22:31:37 2019

@author: BILU
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


name = input()
img = cv2.imread(name)

#print(img.shape)

img_height , img_width , dim = img.shape

print("\n Image Width: ",img_width ,"\n Image Height: ", img_height ,"\n Image Dimention: ", dim)
#print(img.ndim)
hist = cv2.calcHist([img],[0],None,[256],[0,256])

cv2.imshow('image',img)
plt.hist(img.ravel(),256,[0,256]) 
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
