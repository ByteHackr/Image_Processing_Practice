# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:48:15 2019

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
img = cv2.imread(name)
img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
img_height , img_width  = img.shape

#for i in range(0,int(img_height)):
#	for j in range(0,int(img_width)):
#			img[i][j] = img[i][j][0]*0.21+ img[i][j][1]*0.72 + img[i][j][2]*0.07

hist = np.zeros(256,dtype=int)

""" Histogram Manually Create """
#print(hist)
#for i in range(0,int(img_height)):
#    for j in range(0,int(img_width)):
#       hist[img[i][j]]+ =  1

#plt.plot(hist)

""" Histogram Create Using Opencv (calcHist Function)"""
print(hist)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
#for i in range(hist.size):
#    print(hist[i])

""" Histogram Create Using Numpy (histogram Function)"""
#hist,bins = np.histogram(img.ravel(),bins=np.arange(0,256))
#print(hist)
#fig=plt.plot(hist)

""" Histogram Create Using matplotlib (hist Function)"""
fig = plt.hist(img.ravel(),256,[0,256])
plt.xlaok.jpgbel('Colors')
plt.ylabel('No. of Pixels')
plt.savefig('Hist.png')  
""" USING savefig FUNCTION WE SAVE THE PLOTED HISTOGRAM IN A .png IMAGE"""


hist_pic = np.zeros((200,256),dtype=int)

div = (hist.max()/200)+1



print(hist_pic.shape)
for i in range(0,256):
   #j = ((hist[i]/(img_height*img_width))*100)
   j = hist[i]/div
   print(j)
   k=hist_pic.shape[0] - 1
   while j > 0:
       hist_pic[k,i] = 255
       k = k - 1
       j = j - 1
       
#cv2.imwrite("Hist_image.png",hist_pic)
plt.subplot(), plt.plot(hist_pic)
plt.savefig("hist.png",dpi=300)
plt.show()