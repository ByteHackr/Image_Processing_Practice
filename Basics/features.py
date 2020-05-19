#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:18:50 2020

@author: sandipan
"""

import cv2 as cv
import numpy as np

img_name = 'test.jpg'
img = cv.imread(img_name)
gray = cv.imread(img_name,0)
blur = cv.GaussianBlur(gray,(5,5),0)

hist = cv.calcHist([blur],[0],None,[256],[0,256])
hist_norm = hist.ravel()/hist.sum()
Q = hist_norm.cumsum()
bins = np.arange(256)
fn_min = np.inf
thresh = -1

for i in range(1,256):
    p1,p2 = np.hsplit(hist_norm,[i]) 

    q1,q2 = Q[i],Q[255]-Q[i] 
    
    if q1 < 1.e-6 or q2 < 1.e-6:
        continue
    
    b1,b2 = np.hsplit(bins,[i]) 
    

    m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
    v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2
    
    fn = v1*q1 + v2*q2
    if fn < fn_min:
        fn_min = fn
        thresh = i

Height , Width , _ = img.shape

mean = np.mean(img)

var = np.var(img)

std = np.std(img)

threshold_value = thresh

_, otsu = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

contours, _ = cv.findContours(otsu,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)[-2:]
no_of_contours = len(contours)


dst = cv.cornerMinEigenVal(gray, 2, 3, 0)
total_corner_detect = len(dst)

img_txt = img_name.split('.')[0]
file = open('Features_of_Image_' + img_txt + '.txt','w')

file.write('\nHeight          : ' + str(Height))
file.write('\nWidth           : ' + str(Width))
file.write('\nMean            : ' + str(mean))
file.write('\nVariance        : ' + str(var))
file.write('\nStd             : ' + str(std))
file.write('\nThreshold       : ' + str(threshold_value))
file.write('\nNo_of_Regions   : ' + str(no_of_contours))
file.write('\nNo._of_Corner   : ' + str(total_corner_detect))

file.close()

