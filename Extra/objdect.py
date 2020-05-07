#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 09:26:25 2019

@author: sandipan
"""

import cv2
import numpy as np
import matplotlib.pylab as plt

#img = cv2.pyrDown(cv2.imread('lol.jpg', cv2.IMREAD_UNCHANGED))
img=cv2.imread('grey0.jpg')
#img=cv2.imread('13001257143242.png')

# threshold image
ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                128, 255, cv2.THRESH_BINARY)
# find contours and get the external one
contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
rect = cv2.minAreaRect(contours[0])

def crop_minAreaRect(img, rect):

    # rotate img
    angle = rect[2]
    rows,cols = img.shape[0], img.shape[1]
    M = cv2.getRotationMatrix2D((cols,rows),angle,1)
    img_rot = cv2.warpAffine(img,M,(cols,rows))

    # rotate bounding box
    rect0 = (rect[0], rect[1],1)
#    cnt = np.array([[0,0], [1,1], [2,0]])
#    rect0 = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect0)
    pts = np.int0(cv2.transform(np.array([box]), M))[0]    
    pts[pts < 0] = 0

    # crop
    img_crop = img_rot[pts[1][1]:pts[0][1], 
                       pts[1][0]:pts[2][0]]

    return img_crop


# crop
img_croped = crop_minAreaRect(img, rect)



#def crop_rect(img, rect):
#    # get the parameter of the small rectangle
#    center, size, angle = rect[0], rect[1], rect[2]
#    center, size = tuple(map(int, center)), tuple(map(int, size))
#
#    # get row and col num in img
#    height, width = img.shape[0], img.shape[1]
#
#    # calculate the rotation matrix
#    M = cv2.getRotationMatrix2D(center, angle, 1)
#    # rotate the original image
#    img_rot = cv2.warpAffine(img, M, (width, height))
#
#    # now rotated rectangle becomes vertical and we crop it
#    img_crop = cv2.getRectSubPix(img_rot, size, center)
#
#    return img_crop, img_rot
#
#img_croped = crop_rect(img, rect)


#for c in contours:
#    # get the bounding rect
#    if cv2.contourArea(c) > 500:
##		continue
#        x, y, w, h = cv2.boundingRect(c)
#    # draw a green rectangle to visualize the bounding rect
#        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
#
#        rect = cv2.minAreaRect(c)
#        box = cv2.boxPoints(rect)
#        box = np.int0(box)
#        cv2.drawContours(img, [box], 0, (0, 0, 255),2)

    # finally, get the min enclosing circle
#    (x, y), radius = cv2.minEnclosingCircle(c)
#    center = (int(x), int(y))
#    radius = int(radius)
#    img = cv2.circle(img, center, radius, (255, 0, 0), 2)

print(len(contours))
#cv2.drawContours(img, contours, -1, (255, 255, 0), 1)

#cv2.imshow("nemo", img)
#
#cv2.imshow("nemo", img)
#
#while True:
#    key = cv2.waitKey(1)
#    if key == 27: #ESC key to break
#        break
#
#cv2.destroyAllWindows()
#plt.figure()
#plt.subplot(1,2,1)
#plt.imshow(img)
#plt.subplot(1,2,2)
plt.imshow(img_croped)
plt.savefig("jj.png",dpi=300)

plt.show()