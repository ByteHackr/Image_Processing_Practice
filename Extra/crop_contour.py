#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 6:10:40 2019

@author: sandipan
"""

import cv2
import numpy as np
from pathlib import Path
import os
from glob import glob
#img = cv2.imread('13001257143242.png')
#img=cv2.imread('messigray25.png')
k = 0

new = input("ENTER YOUR INPUT IMAGE DIRECTORY: ")
inpath = os.getcwd() + new
entries = os.listdir(inpath)
for entry in entries:        
#for img in glob('*.png'):
    img = cv2.imread(os.path.join(inpath,entry))
    print(entry)
#grayimage = cv2.cvtColor(bounding_box_image, cv2.COLOR_BGR2GRAY)
#ret, mask = cv2.threshold(grayimage, 254, 255, cv2.THRESH_BINARY)
    ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                128, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #print(len(contours))


    for contour in contours:

        if cv2.contourArea(contour) > 500:
            print(len(contour))
            print(k)
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            
            ext_left = tuple(contour[contour[:, :, 0].argmin()][0])
            ext_right = tuple(contour[contour[:, :, 0].argmax()][0])
            ext_top = tuple(contour[contour[:, :, 1].argmin()][0])
            ext_bot = tuple(contour[contour[:, :, 1].argmax()][0])
            roi_corners = np.array([box], dtype=np.int32)
#            cv2.polylines(img, roi_corners, 1, (255, 0, 0), 3)
#        cv2.imshow('image', img)
#        cv2.waitKey(0)
            cropped_image = img[ext_top[1]:ext_bot[1], ext_left[0]:ext_right[0]]
#for entry in entries:
#    k = 0
            #out_arr = 'cor'
            #outpath = os.getcwd() +  out_arr
            out_string = '/a/00000'+ str(k)+'.png'
            k=k+1
            #cv2.imwrite(os.path.join(outpath,out_arr,out_string),cropped_image)
            cv2.imwrite(out_string,cropped_image)
#cv2.imwrite('crop.jpg', cropped_image)