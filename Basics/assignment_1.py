#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:18:50 2020

@author: sandipan
"""

import cv2
img1 = cv2.imread('IMG_20191114_181410.jpg')
img = cv2.imread('0.jpeg',0)
# img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

img_not = cv2.bitwise_not(img1)

cv2.imshow("Pic",img)
 
cv2.imshow("Invert1",img_not)
cv2.imshow("Binary",th1)
cv2.imwrite("me_neg3.png",img_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
