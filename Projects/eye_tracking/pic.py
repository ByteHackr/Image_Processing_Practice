#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 21:54:52 2019

@author: sandipan
"""



import os
import numpy as np
import cv2
import time
from PIL import Image  
from datetime import datetime


#img1=cv2.imread("pic/1.jpg",0)
#img2=cv2.imread("pic/2.jpg",0)
#img3=cv2.imread("pic/3.jpg",0)
#img4=cv2.imread("pic/4.jpg",0)
#img5=cv2.imread("pic/5.png",0)
#
#w, h = img1.shape[1], img1.shape[0]
#image_to_show = np.copy(img1)
#
#finish = False
#while not finish:
#    key = cv2.waitKey(0)
#    if key == ord('a'):
##        image_to_show = np.copy(img1)
#        cv2.imshow('img1',img1)
##    elif key == ord('b'):
##        img1=cv2.imread("pic/1.jpg",0)
##        cv2.imshow('img1',img1)
##    elif key == ord('c'):
##        img2=cv2.imread("pic/2.jpg",0)
##        cv2.imshow('img2',img2)
##    elif key == ord('d'):
##        img2=cv2.imread("pic/2.jpg",0)
##        cv2.imshow('img2',img2)
##    elif key == ord('e'):
##        img2=cv2.imread("pic/2.jpg",0)
##        cv2.imshow('img2',img2)
#    elif key == 27:
#        finish = True

#cv2.waitKey(5000)
##time.sleep(2)
#img2=cv2.imread("pic/2.jpg",0)
#img3=cv2.imread("pic/3.jpg",0)
#img4=cv2.imread("pic/4.jpg",0)
#
#finish=False
##cv2.imshow('img2',img2)
#while not finish:
#    k=cv2.waitKey(0)
#    if k == ord('s'):
#        cv2.imshow('img3',img3)
##        cv2.destroyAllWindows()
#    elif k == ord('a'): 
#        cv2.imshow('img4',img4)
#    elif k == 27:
#        cv2.destroyAllWindows()
#        finish-True
#    cv2.destroyAllWindows()
#cv2.namedWindow("lala")
#img = cv2.imread("pic/1.jpg") 
#
#while True:
#    cv2.imshow("lala", img)
#    dt = datetime.now()
#    ctime=dt.microsecond
#    cv2.imshow("lala", img)
#    k = cv2.waitKey(100) 
#    if k == ord("a"):                     
#        
#        dt = datetime.now()
#        ctime=dt.microsecond
#        print(ctime)
#        img = cv2.imread("pic/2.jpg")
#    elif k == ord("b"):
#        
#        dt = datetime.now()
#        ctime=dt.microsecond
#        print(ctime)
#        img = cv2.imread("pic/4.jpg")
#    elif k == ord("c"):
#        
#        dt = datetime.now()
#        ctime=dt.microsecond
#        print(ctime)
#        img = cv2.imread("pic/3.jpg")
#    elif k == ord("d"):
#        
#        dt = datetime.now()
#        ctime=dt.microsecond
#        print(ctime)
#        img = cv2.imread("pic/5.png")
#    elif k == 27:  
#        break
#cv2.destroyAllWindows()
#now = datetime.now()
#ctime = now.strftime("%M:%S")
#
slid_time=open("slid_time.txt","a")
#time.sleep(5)
now = datetime.now()
s = now.strftime("%H")
t = now.strftime("%M")
u = now.strftime("%S")
w = now.strftime("%f")
ctime=(s+t+u+w)
img3=cv2.imread("pic/3.jpg",0)
cv2.imshow('img3',img3)
print(ctime)
print(ctime, file=slid_time)
cv2.waitKey(5000)
now = datetime.now()
s = now.strftime("%H")
t = now.strftime("%M")
u = now.strftime("%S")
w = now.strftime("%f")
ctime=(s+t+u+w)
#cv2.waitKey(5000)
#time.sleep(5)
img4=cv2.imread("pic/4.jpg",0)
cv2.imshow('img4',img4)
print(ctime)
print(ctime, file=slid_time)

cv2.waitKey(5000)

#cv2.waitKey(5000)
#time.sleep(5)
now = datetime.now()
s = now.strftime("%H")
t = now.strftime("%M")
u = now.strftime("%S")
w = now.strftime("%f")
ctime=(s+t+u+w)
img5=cv2.imread("pic/5.png",0)
cv2.imshow('img5',img5)
print(ctime)
print(ctime, file=slid_time)
cv2.waitKey(5000)
now = datetime.now()
s = now.strftime("%H")
t = now.strftime("%M")
u = now.strftime("%S")
w = now.strftime("%f")
ctime=(s+t+u+w)
img2=cv2.imread("pic/2.jpg",0)
cv2.imshow('img2',img2)
print(ctime)
print(ctime, file=slid_time)
cv2.waitKey(5000)
now = datetime.now()
s = now.strftime("%H")
t = now.strftime("%M")
u = now.strftime("%S")
w = now.strftime("%f")
ctime=(s+t+u+w)
img1=cv2.imread("pic/1.jpg",0)
cv2.imshow('img1',img1)
print(ctime)
print(ctime, file=slid_time)
slid_time.close()
cv2.waitKey(5000)
#
##cv2.waitKey(5000)
##time.sleep(5)
##while True:
##            
##    im1 = Image.open(r"pic/1.jpg")
##    im1.show()
##    time.sleep(5)
##    im2 = Image.open(r"pic/2.jpg")  
##    im2.show()
##    time.sleep(5)
##    im3 = Image.open(r"pic/2.jpg")
##    im3.show()
##    time.sleep(5) 
#
##names = ['pic/5.png', 'pic/4.jpg', 'pic/3.jpg', 'pic/1.jpg'];
##window_titles = ['first', 'second', 'third', 'fourth']
##
##
##cap = [cv2.VideoCapture(i) for i in names]
##
##frames = [None] * len(names);
##gray = [None] * len(names);
##ret = [None] * len(names);
##
##while True:
##
##    for i,c in enumerate(cap):
##        if c is not None:
##            ret[i], frames[i] = c.read();
##
##
##    for i,f in enumerate(frames):
##        if ret[i] is True:
##            gray[i] = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
##            cv2.imshow(window_titles[i], gray[i]);
##            time.sleep(2)
##
##    if cv2.waitKey(1) & 0xFF == ord('q'):
##       break
##
##
##for c in cap:
##    if c is not None:
##        c.release();
##
cv2.destroyAllWindows()











#def slid():
#    cv2.namedWindow("lala")
#    img = cv2.imread("pic/1.jpg")
#    while True:
#        cv2.imshow("lala", img)
#        k = cv2.waitKey(0) 
#        if k == ord("a"):                     
#            img = cv2.imread("pic/2.jpg")
#        elif k == ord("b"):
#            img = cv2.imread("pic/4.jpg")
#        elif k == ord("c"):
#            img = cv2.imread("pic/3.jpg")
#        elif k == ord("d"):
#            img = cv2.imread("pic/5.png")
#        elif k == 27:  
#            break
#    cv2.destroyAllWindows()