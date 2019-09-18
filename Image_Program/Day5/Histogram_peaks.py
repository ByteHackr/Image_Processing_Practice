# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:26:20 2019

@author: BILU
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def Draw_Histogram(in_img):
    
    hist , bins_edge = np.histogram(in_img.ravel(),bins=np.arange(256),range=None,density=False)
    plt.hist(in_img.ravel(),256,[0,256])
    
    high1,in1 = hist[1],1
    high2,in2 = hist[0],0
    
    for i in range(0,hist.size):
        if hist[i] > high1:
            high2 = high1
            in2 = in1
            high1 = hist[i]
            in1 = i
        else:
            if hist[i] > high2:
                high2 = hist[i]
                in2 = i
            
    print(in1,high1,in2,high2)
    
    hist_pic = np.zeros((300,300),dtype=int)
    div = (hist.max()/200)+1

    for i in range(0,256):
       #j = ((hist[i]/(img_height*img_width))*100)
       if i == in1 or i == in2:
           j = hist[i]/div
           print(j)
           k=hist_pic.shape[0] - 1
           while j > 0:
               hist_pic[k,i] = 255
               k = k - 1
               j = j - 1
           
    cv2.imwrite("Hist_image_peaks.png",hist_pic)
    

def main():
    
    im_name = input("ENTER IMAGE FILE NAME :: ")
    
    img = np.array([],np.uint8)
    img = cv.imread(im_name)
    img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    
    #print(img.shape)
    
    #cv.imshow('Gray_Shiva',img)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    
    #print(type(img))
    
    Draw_Histogram(img)
    
main()
    
    