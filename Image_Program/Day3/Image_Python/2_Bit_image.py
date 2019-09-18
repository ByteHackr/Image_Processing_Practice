# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 08:33:30 2019

@author: BILU
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = np.array([])
img = cv2.imread('Scan1.jpg')

img_height , img_width , dim = img.shape

img1 = np.zeros(shape=(img_height,img_width,3),dtype = int,order = 'C')

for i in range(0,int(img_height)):
    for j in range(0,int(img_width)):
       x = (img[i][j][0]*0.21+ img[i][j][1]*0.72 + img[i][j][2]*0.07)
      
       if x <= 64:
           img1[i][j] = 0
    
      
       elif x <= 128:
           img1[i][j] = 64
      
       elif x <= 192:
           img1[i][j] = 192
      
        
       else:
           img1[i][j] = 255
        
#plt.hist(img.ravel(),256,[0,256]) 
#plt.show()
print(img)
print("\nNEW: ",img1)

cv2.imshow('image',img1)
cv2.imshow('image1',img)

#plt.imshow(img1)
cv2.imwrite('Scan3.jpg',img1)
#cv2.calcHist([img],[0],None,[256],[0,256])
cv2.waitKey(0)
cv2.destroyAllWindows()