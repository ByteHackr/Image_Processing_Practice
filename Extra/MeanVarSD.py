#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 18:07:16 2019

@author: sandipan
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

img = np.array([])
img = cv2.imread('DSC_0812tamp131.jpg')

#img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
row, col, dim = img.shape
img1 = np.zeros(shape=(row,col),dtype=int)

output_m = np.zeros(shape=(row,col),dtype=int)
output_v = np.zeros(shape=(row,col),dtype=float)
output_sd = np.zeros(shape=(row,col),dtype=float)
output_mo = np.zeros(shape=(row,col),dtype=float)
output_s = np.zeros(shape=(row,col),dtype=float)


#ker = np.array(([1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]),dtype=int)
#print(ker)

for i in range(row):
    for j in range(col):
        x =  img[i][j][0]*0.07+img[i][j][1]*0.72+img[i][j][2]*0.21
        img1[i][j] = x
        #output[i][j] = x      
#i=1
#j=1
#print(img1[i-1:i+2,j-1:j+2])
#ker = img1[i-1:i+2,j-1:j+2]
#print(ker)
#ker = ker + (-200)
#print(ker)
#print(ker.ravel(),ker.sum())
#sum = ker.sum()
 
  
for i in np.arange(2,row-2):
    for j in np.arange(2,col-2):
        sum = img1[i-1:i+2,j-1:j+2].ravel().sum()
        sum = sum / 9
        output_m[i][j] = sum
        temp = img1[i-1:i+2,j-1:j+2]
#        temp = (temp+(-output_m[i][j]))*(temp+(-output_m[i][j]))
        temp = (temp+(-output_m[i][j]))
        temp = np.power(temp,2)
        sum = temp.ravel().sum()
        sum = sum/9
        output_v[i][j] = sum
        
        output_sd[i][j] = math.sqrt(output_v[i][j])
#
#for i in np.arange(0,row):
#        for j in np.arange(0,col):
#            sum1 = img1[i-2:i+3,j-2:j+3].ravel().sum()
#            sum1 = sum1 / 25
#            output_mo[i][j] = sum1
##sum2=sum1-sum
#output_s=(output_m[i][j]-output_mo[i][j])
           

print(np.amax(output_v),np.amax(output_sd))
plt.subplot(1,2,1)
#hill=plt.hist(output_v.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
#plt.plot(hill) 
#plt.show() 
plt.title('Original Image')
plt.imshow(img1)
cv2.imwrite('Gray Image.jpg',img1)

#print(output)
plt.subplot(1,2,2)
plt.title('Mean Filter Image')
plt.imshow(output_m)
cv2.imwrite('Mean_Image.jpg',output_m)
cv2.imwrite('Varence_Image.jpg',output_v)
cv2.imwrite('SD_Image.jpg',output_sd)
#cv2.imwrite('mo.jpg',output_s)


#cv2.subtract(output_v,img)
#output_v= np.int32(output_v)
#img=np.int32(img)
#
#img7=(output_v-img)
#cv2.imwrite('cl_4.jpg',img7)
#vare = np.var(img)
#cv2.imwrite('vare.jpg',vare)
#
#def normalizedGraylevelVariance(img):
#    ''''GLVN' algorithm (Santos97)'''
#    mean, stdev = cv2.meanStdDev(img)
#    s = stdev[0]**2 / mean[0]
#    return s[0]

#cc=normalizedGraylevelVariance(img)
#plt.imshow(cc)
#










