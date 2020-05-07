#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 21:54:52 2019

@author: sandipan
"""

import cv2
import numpy
from os.path import join
import time
from datetime import datetime
import keyboard
import matplotlib.image as ip 
import matplotlib.pyplot as plt
import pyglet
from PIL import Image  
import threading
import time
import logging
import multiprocessing

#import pic
def show_image_with_data(frame, blinks, irises, err=None):
    font = cv2.FONT_HERSHEY_SIMPLEX
    if err:
        cv2.putText(frame, str(err), (20, 450), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
#    cv2.putText(frame, 'blinks: ' + str(blinks), (10, 30), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
#    cv2.putText(frame, 'moved: ' + str(moved), (10, 30), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

    for w, h in irises:
        cv2.circle(frame, (w, h), 2, (0, 255, 0), 2)
#        print(h,w)
        now = datetime.now()
        s = now.strftime("%H")
        t = now.strftime("%M")
        u = now.strftime("%S")
        w = now.strftime("%f")
        ctime=(s+t+u+w)
        eye_possition=open("eye_possition.txt","a")
#        print(h,w,ctime)
        
        print(h, w, ctime, "\n", file=eye_possition)            
        eye_possition.close()
    cv2.imshow('nemo', frame)
#    pic.slid()    
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

class ImageSource:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)

    def get_current_frame(self, gray=False):
        ret, frame = self.capture.read()
        frame = cv2.flip(frame, 1)
        if not gray:
            return frame
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    def release(self):
        self.capture.release()


class CascadeClassifier:
    def __init__(self, glasses=True):
        if glasses:
            self.eye_cascade = cv2.CascadeClassifier(join('trained_data', 'haarcascade_eye_tree_eyeglasses.xml'))
        else:
            self.eye_cascade = cv2.CascadeClassifier(join('trained_data', 'haarcascade_eye.xml'))

    def get_irises_location(self, frame_gray):
        eyes = self.eye_cascade.detectMultiScale(frame_gray, 1.3, 5)  # if not empty - eyes detected
        irises = []

        for (ex, ey, ew, eh) in eyes:
            iris_w = float(ex + float(ew / 2))
            iris_h = float(ey + float(eh / 2))
            irises.append([numpy.float32(iris_w), numpy.float32(iris_h)])
            now = datetime.now()
            s = now.strftime("%H")
            t = now.strftime("%M")
            u = now.strftime("%S")
            w = now.strftime("%f")
            ctime=(s+t+u+w)
            eye_possition_iris=open("eye_possition_iris.txt","a")     
            print(iris_h,iris_w, ew,eh,ctime, "\n", file=eye_possition_iris)            
            eye_possition_iris.close()

        return numpy.array(irises)


class LucasKanadeTracker:
    def __init__(self, blink_threshold=9):
        # Parameters for lucas kanade optical flow
        self.lk_params = dict(winSize=(15, 15),
                         maxLevel=2,
                         criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
        self.blink_threshold = blink_threshold

    def track(self, old_gray, gray, irises, blinks, blink_in_previous):
        lost_track = False
        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, gray, irises, None, **self.lk_params)
        if st[0][0] == 0 or st[1][0] == 0:  # lost track on eyes
            lost_track = True
            blink_in_previous = False
        elif err[0][0] > self.blink_threshold or err[1][0] > self.blink_threshold:  # high error rate in klt tracking
            lost_track = True
            if not blink_in_previous:
                blinks += 1
                blink_in_previous = True
        else:
            blink_in_previous = False
            irises = []
            for w, h in p1:
                irises.append([w, h])
            irises = numpy.array(irises)
        return irises, blinks, blink_in_previous, lost_track

   
class EyerisDetector:
    def __init__(self, image_source, classifier, tracker):
        self.tracker = tracker
        self.classifier = classifier
        self.image_source = image_source
        self.irises = []
        self.blink_in_previous = False
        self.blinks = 0
#        self.slidshow=slidshow

    def run(self):
        k = cv2.waitKey(30) & 0xff
        while k != 27:  # ESC
            frame = self.image_source.get_current_frame()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if len(self.irises) >= 2: 
                track_result = self.tracker.track(old_gray, gray, self.irises, self.blinks, self.blink_in_previous)
                self.irises, self.blinks, self.blink_in_previous, lost_track = track_result
                if lost_track:
                    self.irises = self.classifier.get_irises_location(gray)
            else:  # cannot track for some reason -> find irises
                self.irises = self.classifier.get_irises_location(gray)


            show_image_with_data(frame, self.blinks, self.irises)
#            b=slid()
#            p1 = multiprocessing.Process(name='p1', target=show_image_with_data(frame, self.blinks, self.irises))
#            p = multiprocessing.Process(name='p', target=slid())
#            p.start()
#            p1.start()
            k = cv2.waitKey(30)
            old_gray = gray.copy()

        self.image_source.release()
        cv2.destroyAllWindows()

    
#SlidShow()

eyeris_detector = EyerisDetector(image_source=ImageSource(), classifier=CascadeClassifier(),
                                 tracker=LucasKanadeTracker())
eyeris_detector.run()
#time.sleep(5000)
#pic.slid()