# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 09:11:06 2019

@author: BILU
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 22:05:44 2019

@author: BILU
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import  math
from skimage import feature
import os
import shutil

def Adaptive_Thresolding():
    inpath = os.path.join(os.getcwd(),".\\Scaned image\\.","")
    for x in os.listdir(inpath):
        if os.path.isfile(x): 
            print ('f-', x)
        elif os.path.isdir(x): 
            print ('d-', x)
        elif os.path.islink(x): 
            print ('l-', x)
        else: print ('---', x)
    
    new = input("ENTER YOUR INPUT IMAGE DIRECTORY: ")
    inpath = os.getcwd() + '\\Scaned image\\' + new
    
    if not os.path.exists(inpath):
        print("ENTER CORRECT DIRECTORY...")
        return 0
        
    out_arr = ['Adaptive_Threshold','Global_Thresold','Otsus_Threshold','Local_Binary']
    
    entries = os.listdir(inpath)
    
    for i in range(len(out_arr)):
        outpath = os.getcwd() + '\\Scaned image\\OUT\\' + out_arr[i]
        if os.path.exists(outpath):
            shutil.rmtree(outpath)
        
        os.mkdir(outpath)
    
    outpath = os.getcwd() + '\\Scaned image\\OUT\\'
    #src_fname, ext = os.path.splitext(x)
    k = 0
    for entry in entries:
        
        img = np.array([],dtype=int)
        
        img = cv2.imread(os.path.join(inpath,entry))
        
        #img = img[1150:2900,0:img.shape[1]]
        
        print(entry)
        
        Gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        """Adaptive Thresolding"""
        img_in = cv2.medianBlur(Gray_img,5)
        img_out = cv2.adaptiveThreshold(img_in,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
        output = np.concatenate((img_in, img_out), axis=1)
        out_string = 'Original + Adaptive 0000'+ str(k)+'.tif'
        i = 0
        cv2.imwrite(os.path.join(outpath,out_arr[i],out_string),output)
        
        
        """Global Thresolding"""
        b , img_out = cv2.threshold(Gray_img,127,255,cv2.THRESH_BINARY)
        output = np.hstack((Gray_img, img_out))
        out_string = 'Original + Global 0000'+ str(k)+'.tif'
        i = 1
        cv2.imwrite(os.path.join(outpath,out_arr[i],out_string),output)
        
        
        """Otsus Thresolding"""
        b , img_out = cv2.threshold(Gray_img,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        output = np.hstack((Gray_img , img_out))
        out_string = 'Original + Otsus 0000'+ str(k)+'.tif'
        i = 2
        cv2.imwrite(os.path.join(outpath,out_arr[i],out_string),output)
    
    
        """Local Binary Pattern"""
        img_out = feature.local_binary_pattern(Gray_img,8,1,method='default')
        output = np.hstack((Gray_img , img_out))
        out_string = 'Original + LBP 0000'+ str(k)+'.tif'
        i = 3
        cv2.imwrite(os.path.join(outpath,out_arr[i],out_string),output)
        k+=1
        
    # cwd = os.getcwd()   "USE TO GET THE CURRENT DIRECTORY"
    print("VIEW OUTPUT FROM THIS DIRECTORY.... " , outpath)
    return 1

def main():
    i=0
    while i < 1:
       n = Adaptive_Thresolding()
       if n == 0:
           Adaptive_Thresolding()
       else:
           break
       
main()