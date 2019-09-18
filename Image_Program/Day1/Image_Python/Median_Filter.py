# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 20:54:21 2019

@author: BILU
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = np.array([])
img = cv2.imread('Noise_image.jpg')

img1 = img.copy()
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

row, col, dim = img.shape

output = np.zeros(shape=(row,col,dim),dtype=int)

for i in range(row):
    for j in range(col):
        x =  img1[i][j][0]*0.21+img1[i][j][1]*0.72+img1[i][j][2]*0.07
        img1[i][j] = x
        output[i][j] = x
        
for i in np.arange(1,row-1):
    for j in np.arange(1,col-1):
        neighbours = []
        for k in np.arange(-1,2):
            for l in np.arange(-1,2):
                x = output[i+k][j+l][0]
                neighbours.append(x)
        neighbours.sort()
        output[i][j] = neighbours[4]
        

plt.subplot(1,2,1)
plt.title('Noise Image')
plt.imshow(img1)
cv2.imwrite('(Gray)noise_Image.jpg',img1)

plt.subplot(1,2,2)
plt.title('Denoise Image')
plt.imshow(output)
cv2.imwrite('(Gray)Denoise_Image.jpg',output)

