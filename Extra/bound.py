#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:26:25 2019

@author: sandipan
"""

import cv2
import numpy as np

#img = cv2.pyrDown(cv2.imread('lol.jpg', cv2.IMREAD_UNCHANGED))
#img=cv2.imread('13001257143242.png')
img=cv2.imread('kk.png')


# threshold image
ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                128, 255, cv2.THRESH_BINARY)
# find contours and get the external one

contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    # get the bounding rect
    if cv2.contourArea(c) > 100:
#		continue
        x, y, w, h = cv2.boundingRect(c)
    # draw a green rectangle to visualize the bounding rect
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
#        cv2.drawContours(img, [box], 0, (0, 0, 255),2)

    # finally, get the min enclosing circle
#    (x, y), radius = cv2.minEnclosingCircle(c)
#    center = (int(x), int(y))
#    radius = int(radius)
#    img = cv2.circle(img, center, radius, (255, 0, 0), 2)

print(len(contours))
#cv2.drawContours(img, contours, -1, (255, 255, 0), 1)

cv2.imshow("nemo", img)

cv2.imshow("nemo", img)
cv2.imwrite("nemo.png",img)
while True:
    key = cv2.waitKey(1)
    if key == 27: #ESC key to break
        break

cv2.destroyAllWindows()