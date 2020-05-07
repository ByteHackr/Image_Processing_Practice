#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 18:38:05 2019

@author: sandipan
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('13001257143242.png',0)
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
plt.subplot(), plt.plot(hist_full)
plt.savefig("hist.png",dpi=300)
plt.show()
