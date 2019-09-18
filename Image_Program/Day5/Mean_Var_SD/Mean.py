# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 08:44:11 2019

@author: BILU
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

img = np.array([])
img = cv2.imread('Scan1.jpg')


#img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

row, col, dim = img.shape
img1 = np.zeros(shape=(row,col),dtype=int)

output_m = np.zeros(shape=(row,col),dtype=int)
output_v = np.zeros(shape=(row,col),dtype=int)
output_sd = np.zeros(shape=(row,col),dtype=float)

ker = np.array(([1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]),dtype=int)
print(ker)

for i in range(row):
    for j in range(col):
        x =  img[i][j][0]*0.07+img[i][j][1]*0.72+img[i][j][2]*0.21
        img1[i][j] = x
        #output[i][j] = x
        
"""
i=1
j=1
print(img1[i-1:i+2,j-1:j+2])
ker = img1[i-1:i+2,j-1:j+2]
print(ker.ravel(),ker.sum())
sum = ker.sum()
"""
     
for i in np.arange(2,row-2):
    for j in np.arange(2,col-2):
        sum = img1[i-2:i+3,j-2:j+3].ravel().sum()
        sum = sum / 25
        output_m[i][j] = sum
        
        output_v[i][j] = (img1[i][j] - output_m[i][j])*(img1[i][j] - output_m[i][j])
        
        output_sd[i][j] = math.sqrt(output_v[i][j])
            
                
      

print(np.amax(output_v),np.amax(output_sd))
plt.subplot(1,2,1)
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