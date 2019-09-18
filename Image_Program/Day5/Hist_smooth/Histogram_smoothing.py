# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 08:29:00 2019

@author: BILU
"""

import numpy as np
from matplotlib import pyplot as plt
import cv2
"""
arr = np.array([0,1,1,1,1,2,2,2,3,3,3,3,4,4,4,5,5,6,6,6,7,7,8])

hist , bins = np.histogram(arr,bins=np.arange(10))
plt.title('Numpy Histogram')
fig = plt.plot(hist)
plt.savefig('NumHistogram.png')
#plt.show()
sum = 0 
for i in range(0,len(hist)):
    sum = sum + i*hist[i]
    
print('Threshold: ',sum/len(arr))
"""
name = input("ENTER IMAGE NAME: ")
img1 = cv2.imread(name)
img = cv2.cvtColor(img1,cv2.COLOR_RGB2GRAY)
img_height , img_width  = img.shape

#for i in range(0,int(img_height)):
#	for j in range(0,int(img_width)):
#			img[i][j] = img[i][j][0]*0.21+ img[i][j][1]*0.72 + img[i][j][2]*0.07

hist = np.zeros(256,dtype=int)

""" Histogram Manually Create """
#print(hist)
#for i in range(0,int(img_height)):
#    for j in range(0,int(img_width)):
#       hist[img[i][j]] = hist[img[i][j]] + 1

#plt.plot(hist)

""" Histogram Create Using Opencv (calcHist Function)"""
print(hist)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
#hist = cv2.calcHist([img1[ : , : ,0:1]],[0],None,[256],[0,256])       #for input gray scale image histogram
fig = plt.plot(hist)
#for i in range(hist.size):
#    print(hist[i])

""" Histogram Create Using Numpy (histogram Function)"""
#hist,bins = np.histogram(img.ravel(),bins=np.arange(0,256))
#print(hist)
#fig=plt.plot(hist)

""" Histogram Create Using matplotlib (hist Function)"""
#fig = plt.hist(img.ravel(),256,[0,256])

plt.xlabel('Colors')
plt.ylabel('No. of Pixels')
plt.savefig('Non_Smooth_Hist.png')
plt.close()  
""" USING savefig FUNCTION WE SAVE THE PLOTED HISTOGRAM IN A .png IMAGE"""

hist_pic = np.zeros((1000,300),dtype=int)

#div = (hist.max()/200)+1

print(hist_pic.shape)
for i in range(0,256):
   #j = ((hist[i]/(img_height*img_width))*100)
   j = hist[i]/20
   print(j)
   k=hist_pic.shape[0] - 1
   while j > 0:
       hist_pic[k,i] = 255
       k = k - 1
       j = j - 1
       if k<0:
           break
       
cv2.imwrite("Hist_image.png",hist_pic)

hist1 = np.zeros(256,dtype=int)

for i in range(0,len(hist)-1):
    if i == 0:
        hist1[i]=(hist[i]+hist[i+1])/2
    else:
        hist1[i]=(hist[i-1]+hist[i]+hist[i+1])/3

hist1[255] = (hist[254]+hist[255])/2

hist_pic = np.zeros((1000,300),dtype=int)

#div = (hist.max()/200)+1

print(hist_pic.shape)
for i in range(0,256):
   #j = ((hist[i]/(img_height*img_width))*100)
   j = hist1[i]/20
   print(j)
   k=hist_pic.shape[0] - 1
   while j > 0:
       hist_pic[k,i] = 255
       k = k - 1
       j = j - 1
       if k<0:
           break
       
cv2.imwrite("Hist_image_Smooth_3.png",hist_pic)

fig = plt.plot(hist1)
plt.savefig('Smooth_Hist_(3).png')
plt.close()

hist2 = np.zeros(len(hist),dtype=int)


for i in range(0,len(hist)-2):
    if i == 0:
        hist2[i]=(hist[i]+hist[i+1]+hist[i+2])/3
    elif i == 1:
        hist2[i]=(hist[i]+hist[i+1]+hist[i+2])/3
    else:
        hist2[i]=(hist[i-2]+hist[i-1]+hist[i]+hist[i+1]+hist[i+2])/5

hist2[254] = (hist[253]+hist[254]+hist[255])/3

hist2[255] = (hist[253]+hist[254]+hist[255])/3
    
fig = plt.plot(hist1)
plt.savefig('Smooth_Hist_(5).png')

hist_pic = np.zeros((1000,300),dtype=int)

#div = (hist.max()/200)+1

print(hist_pic.shape)
for i in range(0,256):
   #j = ((hist[i]/(img_height*img_width))*100)
   j = hist2[i]/20
   print(j)
   k=hist_pic.shape[0] - 1
   while j > 0:
       hist_pic[k,i] = 255
       k = k - 1
       j = j - 1
       if k<0:
           break
       
cv2.imwrite("Hist_image_Smooth_5.png",hist_pic)
 
"""  
hist_pic = np.zeros((250,300),dtype=int)

div = (hist.max()/200)+1



print(hist_pic.shape)
for i in range(0,256):
   #j = ((hist[i]/(img_height*img_width))*100)
   j = hist[i]/div
   print(j)
   k=hist_pic.shape[0] - 50
   while j > 0:
       hist_pic[k,i] = 255
       k = k - 1
       j = j - 1
       
cv2.imwrite("Hist_image.png",hist_pic)
"""
