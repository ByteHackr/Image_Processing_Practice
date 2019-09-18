# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 21:13:54 2019

@author: BILU
"""

import cv2
from scikit-image import feature
import numpy as np
from matplotlib import pyplot as plt
import  math

img = np.array([],dtype=int)
img = cv2.imread('ScanImage001.tif')

"""
ker = (1/273) * (np.array([[1,4,7,4,1],
                         [4,16,26,16,4],
                         [7,26,41,26,7],
                         [4,16,26,16,4],
                         [1,4,7,4,1]]))
"""
ker = (1/25) * (np.array([[1,1,1,1,1],
                          [1,1,1,1,1],
                          [1,1,1,1,1],
                          [1,1,1,1,1],
                          [1,1,1,1,1]]))

print(math.pow(2,4))

row , col , dim = img.shape

img_in = np.ones(shape=(row,col,2),dtype=int)

img_in = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#plt.subplot(1,2,1)

hist = cv2.calcHist([img_in],[0],None,[256],[0,256])

#print(hist.max())

#hist = (hist / (row*col))*100

plt.hist(img_in.ravel(),100)

img_in = cv2.filter2D(img_in,-1,ker)

#img_in = cv2.GaussianBlur(img_in,(5,5),1)

cv2.imwrite('blur.png',hist)

img_out = np.ones(shape=(row,col,dim),dtype=int)

#ret , img_out = cv2.threshold(img_in,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#img_out = img.copy()
img_out = feature.local_binary_pattern(img_in,8,1,method='default')

#img_out = cv2.adaptiveThreshold(img_in,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#            cv2.THRESH_BINARY,11,2)

"""
for i in range(1,int(row)-1):    
    for j in range(1,int(col)-1):
        
        bin_arr = [0,0,0,0,0,0,0,0]
        k=0
        loc_threshold = img[i][j][0]
        
        if img[i-1][j+1][0] >= loc_threshold:
            bin_arr[k] = 1
        
        k+=1
        if img[i][j+1][0] >= loc_threshold:
            bin_arr[k] = 1
       
        k+=1
        if img[i+1][j+1][0] >= loc_threshold:
            bin_arr[k] = 1
       
        k+=1    
        if img[i+1][j][0] >= loc_threshold:
            bin_arr[k] = 1
        
        k+=1
        if img[i+1][j-1][0] >= loc_threshold:
            bin_arr[k] = 1
       
        k+=1
        if img[i][j-1][0] >= loc_threshold:
            bin_arr[k] = 1
            
        k+=1
        if img[i-1][j-1][0] >= loc_threshold:
            bin_arr[k] = 1
            
        k+=1
        if img[i-1][j][0] >= loc_threshold:
            bin_arr[k] = 1
            
        sum = 0
        for k in range(0,8):
            if bin_arr[k] == 1:
               sum = sum + math.pow(2,k)
        
        if sum > 0:
            img_out[i][j] = sum

"""
"""
for i in range(1,int(row)-1):
    for j in range(1,int(col)-1):
        if img[i][j][0] > 127:
            img_out[i][j] = 255
        else:
            img_out[i][j] = 0
"""

print(img_out.shape)
print(img.shape)
#plt.subplot(1,2,2)
#plt.hist(img_out.ravel(),256)
#cv2.imwrite('blur.png',hist)
cv2.imwrite('LOC.png',img_out)
plt.show()