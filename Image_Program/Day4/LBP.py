# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 01:15:39 2019

@author: BILU
"""

import cv2
from skimage import feature
import numpy as np
from matplotlib import pyplot as plt
import  math

img = np.array([],dtype=int)
img = cv2.imread('download.jpg')

row , col , dim = img.shape

img_in = np.ones(shape=(row,col,2),dtype=int)

img_in = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img_out = np.ones(shape=(row,col,dim),dtype=np.float32)

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
        


print(img_out[10][10])
print(img_out.dtype)


hist,bins = np.histogram(img_out[ : , : , 0:1],bins=np.arange(0,256))
print(hist.dtype)
plt.plot(hist)

for i in range(0,row):    
    for j in range(0,col):
       sum =sum + img_out[i][j][0]
print('sum = ',sum)
print(sum/(row*col))

sum = 0     

for i in range(0,len(hist)):
    #print(hist[i])
    sum = sum + (hist[i]*i)
print('np.sum : ',sum)    
print(sum/(row*col))
t = sum/(row*col)


for i in range(1,int(row)-1):
    for j in range(1,int(col)-1):
        if img[i][j][0] > t:
            img_out[i][j] = 255
        else:
            img_out[i][j] = 0


print(img_in.shape)
print(img.shape)
#plt.subplot(1,2,2)
#plt.hist(img_out.ravel(),256)
#cv2.imwrite('blur.png',hist)
cv2.imwrite('LOC.png',img_out)
plt.show()
