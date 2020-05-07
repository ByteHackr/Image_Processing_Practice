# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 09:25:49 2019

@author: BILU
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

img = np.array([])
img = cv2.imread('Denoise_Image.jpg')

img1 = img.copy()
#img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

row, col, dim = img.shape

#output = np.zeros(shape=(row,col,dim),dtype=int)

#ker = np.array(([-1,-1,-1],[-1,8,-1],[-1,-1,-1]),dtype=float)

#ker = np.array(([0,-1,0],[-1,4,-1],[0,-1,0]),dtype=float)

#ker = np.array(([1,2,1],[0,0,0],[-1,-2,-1]),dtype=float)

#ker = np.array(([1,0,-1],[2,0,-2],[1,0,-1]),dtype=float)

ker = np.array(([0,-1,0],[-1,5,-1],[0,-1,0]),dtype=float)

"""ker = (1/16)*np.array(([0, 0, -1, 0, 0],
                       [0, -1,-2, -1, 0],
                       [-1,-2, 16,-2, -1],
                       [0, -1,-2, -1, 0],
                       [0, 0, -1, 0, 0]),dtype=float)"""

for k in range(0,3):
    for l in range(0,3):
        print(ker[k][l],end="")
    print("")

output = np.zeros(shape=(row,col,dim),dtype=float)


for i in range(row):
    for j in range(col):
        x =  img1[i][j][0]*0.21+img1[i][j][1]*0.72+img1[i][j][2]*0.07
        img1[i][j] = x
        #output[i][j] = x

#print(output)  



for i in np.arange(1,row-1):
    for j in np.arange(1,col-1):
        m = -1
        sum = 0
        for k in range(0,3):
            n = -1
            for l in range(0,3):
                x = img1[i+m][j+n][0]
                y = ker[k][l]
                sum = sum + ( x * y)
                n=n+1
            m=m+1
            
        
        if sum <= 0:
            sum = 0
        if sum >= 256:
           sum = 255
        #if sum >=0 and sum <256:
        output[i][j] = sum
    

"""        
for i in np.arange(1,row-1):
    for j in np.arange(1,col-1):
        m = -1
        sum = 0
        sum1 = 0
        sum2 = 0
        for k in range(0,3):
            n = -1
            for l in range(0,3):
                x = img1[i+m][j+n][0]
                y1 = ker1[k][l]
                sum1 = sum1 + ( x * y1)
                
                y2 = ker2[k][l]
                sum2 = sum2 + ( x * y2)
                n=n+1
            m=m+1
            
        sum = sum1 * sum1 + sum2 * sum2
        sum = math.sqrt(sum)
        #if sum >=0 and sum <256:
        output[i][j] = sum
"""
  
""" 
for i in np.arange(2,row-2):
    for j in np.arange(2,col-2):
        if output[i][j][0] <= 5:
            output[i][j] = 255
        else:
            output[i][j] = 0
         
"""
#output = cv2.filter2D(img1,-1,ker)

"""
for i in np.arange(120,123):
    for j in np.arange(120,123):
        print(output[i][j]," ",end="")
    print("")




for i in np.arange(120,123):
    for j in np.arange(120,123):
        print(output[i][j]," ",end="")
    print("")
 """   
        

plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(img1)

#print(output)
plt.subplot(1,2,2)
plt.title('Mean Filter Image')
plt.imshow(output)
cv2.imwrite("EDGE.jpg",output)