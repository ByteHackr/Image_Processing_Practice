# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:03:38 2019

@author: BILU
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:31:51 2019

@author: BILU
"""
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = np.array([])
img = cv2.imread('Scan1.jpg')

img_height , img_width , dim = img.shape

img1 = np.zeros(shape=(2*img_height,2*img_width,3),dtype = int,order = 'C')

for i in range(0,int(img_height)):
    for j in range(0,int(img_width)):
       x = (img[i][j][0]*0.21+ img[i][j][1]*0.72 + img[i][j][2]*0.07)
       img1[i][j] = x
       img[i][j] = x
        
#plt.hist(img.ravel(),256,[0,256]) 
#plt.show()
print(img)
print("\nNEW: ",img1)
cv2.imwrite('Scan2.jpg',img1)
cv2.imshow('image',img1)
cv2.imshow('image1',img)
#cv2.calcHist([img],[0],None,[256],[0,256])
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = np.array([])
img = cv2.imread('Scan1.jpg')

img_height , img_width , dim = img.shape

img1 = np.zeros(shape=(2*img_height,2*img_width,3),dtype = int,order = 'C')

for i in range(0,int(2*img_height)):
    for j in range(0,int(2*img_width)):
        img1[i][j] = 255
        
for i in range(0,int(img_height)):
    k=0
    for j in range(0,int(img_width)):
       x = (img[i][j][0]*0.21+ img[i][j][1]*0.72 + img[i][j][2]*0.07)
       if x < 127:
           img1[i][j] = 0
           img1[i][img_width+10+k] = 0
           k=k+1
       else:
          img1[i][j] = 255

for i in range(0,int(img_width)):
    k=0
    for j in range(0,int(img_height)):
       x = (img[j][i][0]*0.21+ img[j][i][1]*0.72 + img[j][i][2]*0.07)
       if x < 127:
           img1[img_height+10+k][i] = 0
           k=k+1
        
#plt.hist(img.ravel(),256,[0,256]) 
#plt.show()
print(img)
print("\nNEW: ",img1)
cv2.imwrite('Scan2.jpg',img1)
cv2.imshow('image',img1)
cv2.imshow('image1',img)
#cv2.calcHist([img],[0],None,[256],[0,256])
cv2.waitKey(0)
cv2.destroyAllWindows()
