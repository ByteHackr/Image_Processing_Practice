# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 22:31:37 2019

@author: BILU
"""

import cv2
import numpy as np

name = input()
img = cv2.imread(name)

#print(img.shape)

img_height , img_width , dim = img.shape

print("\n Image Width: ",img_width ,"\n Image Height: ", img_height ,"\n Image Dimention: ", dim)
#print(img.ndim)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
