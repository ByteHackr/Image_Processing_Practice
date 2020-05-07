# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 22:03:08 2019

@author: BILU
"""

import cv2
import numpy as np

img = cv2.imread('input0.jpg')
img1 = np.copy(img)
Gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Blur_img = cv2.blur(Gray_img,(3,3))
t , B_img = cv2.threshold(Gray_img,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
contours,_ = cv2.findContours(B_img,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2:]
print ("Number of contours are: ",len(contours))
Out_img=cv2.drawContours(img1,contours,-1,(0,255,0),2)

max_len = 0
strat1 = 0
end1 = 0

for contour in contours:
    
    start = np.amax(contour,axis=0)
    end = np.amin(contour,axis=0)
    
    if end[0][0] != 0:
        if max_len < (start[0][0] - end[0][0]):
            start1 = np.amax(contour,axis=0)
            end1 = np.amin(contour,axis=0)
            max_len = (start[0][0] - end[0][0])
            Out_img1 = cv2.rectangle(img1,(start[0][0],start[0][1]),(end[0][0],end[0][1]),(0,255,0),2)
        
    
print (start1[0][0],start1[0][1],end1[0][0],end1[0][1])
cv2.imwrite("Contours.tif",Out_img)
cv2.imwrite("Contours1.tif",Out_img1)
cv2.imwrite("Contours_box.tif",img[end1[0][1]:start1[0][1],end1[0][0]:start1[0][0]])
 