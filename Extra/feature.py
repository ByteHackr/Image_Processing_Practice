#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:18:50 2020

@author: sandipan
"""


import cv2
import numpy as np

filename = 'test.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

dimensions = img.shape
height = img.shape[0]
width = img.shape[1]
l=str(dimensions)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
img[dst>0.01*dst.max()]=[0,0,255]

# np.savetxt("feature.txt", dst)

# np.ndarray.tofile(dst, sep="", format="%s")


with open("feature.txt", 'a') as fp:
    # for result in dst.items():
    #     fp.write('%s:%s\n' % (dst))
    fp.write(l)        
    fp.close()
        
        



# cv2.imshow('dst',img)
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()