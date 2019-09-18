# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 21:10:47 2019

@author: BILU
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = np.array([])
img = cv2.imread('Scan1.jpg')

img1 = img.copy()
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

row, col, dim = img.shape

output = np.zeros(shape=(row,col,dim),dtype=int)

ker = np.array(([1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]),dtype=int)
print(ker)

for i in range(row):
    for j in range(col):
        x =  img1[i][j][0]*0.21+img1[i][j][1]*0.72+img1[i][j][2]*0.07
        img1[i][j] = x
        #output[i][j] = x

print(output)        
for i in np.arange(2,row-2):
    for j in np.arange(2,col-2):
        m = -3
        sum = 0
        for k in np.arange(0,5):
            n = -3
            for l in np.arange(0,5):
                x = img1[i+m][j+n][0]
                sum = sum + x
                n=n+1
            m=m+1
        sum = sum / 25
        output[i][j] = sum
            
                
        

plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(img1)

#print(output)
plt.subplot(1,2,2)
plt.title('Mean Filter Image')
plt.imshow(output)
cv2.imwrite('Mean_Image.jpg',output)
