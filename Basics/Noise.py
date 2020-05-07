# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 09:57:44 2019

@author: BILU
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
import random

img = np.array([])

img = cv2.imread('Scan1.jpg',1)
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

rows, columns, dim = img.shape
p = 0.05

output = np.zeros(shape=(rows,columns,dim),dtype = int)

for i in range(rows):
    for j in range(columns):
        r = random.random()
        if r < p/2:
            output[i][j] = 0
        elif r < p:
            output[i][j] = 255
        else:
            output[i][j] = img[i][j]
        
plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Original Image')

plt.subplot(1,2,2)
plt.imshow(output)
plt.title('Noise Image')
plt.show()
#output = cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
cv2.imwrite('Noise_image.jpg',output)