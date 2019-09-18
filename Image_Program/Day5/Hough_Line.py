# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 12:44:22 2019

@author: BILU
"""

import cv2
import numpy as np

img = cv2.imread('ScanImage001.tif')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,250,apertureSize=5,L2gradient=True)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,150,minLineLength,maxLineGap)
for line in lines:
    x1,y1,x2,y2 = lines[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),4)

cv2.imwrite('houghlines5.jpg',img)