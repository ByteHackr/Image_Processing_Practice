#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:26:25 2019

@author: sandipan
"""

#import cv2 
#image = cv2.imread("13001257143242.png")
#gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#edged = cv2.Canny(image, 10, 250)
#(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#idx = 0
#for c in cnts:
#    x,y,w,h = cv2.boundingRect(c)
#    if w>50 and h>50:
#        idx+=1
#        new_img=image[y:y+h,x:x+w]
#        cv2.imwrite(str(idx) + '.png', new_img)
#cv2.imshow("im",image)
#cv2.waitKey(0)
import cv2
import numpy as np

#img = cv2.imread('13001257143242.png')
img=cv2.imread('lol.jpg')

#grayimage = cv2.cvtColor(bounding_box_image, cv2.COLOR_BGR2GRAY)
#ret, mask = cv2.threshold(grayimage, 254, 255, cv2.THRESH_BINARY)
ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                128, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


for contour in contours:

    if cv2.contourArea(contour) > 500:
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)

        ext_left = tuple(contour[contour[:, :, 0].argmin()][0])
        ext_right = tuple(contour[contour[:, :, 0].argmax()][0])
        ext_top = tuple(contour[contour[:, :, 1].argmin()][0])
        ext_bot = tuple(contour[contour[:, :, 1].argmax()][0])
        roi_corners = np.array([box], dtype=np.int32)
#        cv2.polylines(img, roi_corners, 1, (255, 0, 0), 3)
#        cv2.imshow('image', img)
#        cv2.waitKey(0)

    cropped_image = img[ext_top[1]:ext_bot[1], ext_left[0]:ext_right[0]]
    cv2.imwrite('crop.jpg', cropped_image)