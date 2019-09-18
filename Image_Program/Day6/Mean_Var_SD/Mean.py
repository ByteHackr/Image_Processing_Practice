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
img = cv2.imread('Sample.jpg')


#img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

row, col, dim = img.shape
img1 = np.zeros(shape=(row,col),dtype=int)

output_m = np.zeros(shape=(row,col),dtype=int)
output_v = np.zeros(shape=(row,col),dtype=int)
output_sd = np.zeros(shape=(row,col),dtype=float)
output_img = np.zeros(shape=(row,col),dtype=float)

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
k = np.greater_equal(ker,[235])
print(k)
k = np.place(ker,ker==236,[1])
print(ker)
"""
k = 0.5   
for i in np.arange(2,row-2):
    for j in np.arange(2,col-2):
        sum = img1[i-2:i+3,j-2:j+3].ravel().sum()
        sum = sum / 25
        output_m[i][j] = sum
        
        temp = img1[i-2:i+3,j-2:j+3]
        temp = temp + (-output_m[i][j])
        temp = np.power(temp,2)
        sum = temp.ravel().sum()
        sum = sum/25
        output_v[i][j] = sum
        #output_v[i][j] = (img1[i][j] - output_m[i][j])*(img1[i][j] - output_m[i][j])
        
        output_sd[i][j] = math.sqrt(output_v[i][j])
        
        t = output_m[i][j]*(1+k*((output_sd[i][j]/128)-1))
        
        np.place(output_img[i-2:i+3,j-2:j+3],img1[i-2:i+3,j-2:j+3]>=t,[255])

"""
k=0.5          
t = output_m[20][20]*(1+k*(output_sd[20][20]/128-1))
print(t,img1[20-2:20+3,20-2:20+3])
t = output_m[21][21]*(1+k*(output_sd[21][21]/128-1))
print(t,img1[20-2:20+3,20-2:20+3])
t = output_m[22][22]*(1+k*(output_sd[22][22]/128-1))
print(t)
t = output_m[23][23]*(1+k*(output_sd[23][23]/128-1))
print(t)
t = output_m[250][24]*(1+k*(output_sd[250][24]/128-1))
print(t,img1[250-2:250+3,24-2:24+3])
"""
      

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
cv2.imwrite('Output_Image.jpg',output_img)