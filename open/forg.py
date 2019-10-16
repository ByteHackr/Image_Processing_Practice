#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:52:04 2019

@author: sandipan
"""


import numpy as np
import cv2
from scipy.fftpack import fft, dct
import math
import os


def euclidianDistance(a, b):
    e = []
    for i in range(0, len(a)):
        e.append(a[i] - b[i])
    return math.sqrt(sum([i * i for i in e]))


def block(img):
    mboy = 8
    row = len(img)
    col = len(img[1])
    vektör = []
    ct = (row - mboy) * (col - mboy)
    print(ct)
    print("Satir : ", row)
    print("Sütun : ", col)
    liste = []
    for i in range(0, row - mboy):
        for j in range(0, col - mboy):
            for a in range(i, i + mboy):
                for b in range(j, j + mboy):
                    vektör.append(img[a, b])
            vektör.append(i)
            vektör.append(j)
            liste.append(vektör)
            vektör = []
    return liste


def eslesme(sirali, esikdegeri):
    sonHali = []
    for i in range(0, len(sirali) - 20):
        a = i + 20
        for j in range(i + 1, a):
            if euclidianDistance(sirali[i, :-2], sirali[j, :-2]) < esikdegeri:
                sonHali.append(sirali[i, -2:])
                sonHali.append(sirali[j, -2:])
    return sonHali


def removeimage(img, sonHali):
    for i in sonHali:
        img[i[0]:i[0] + mboy, i[1]:i[1] + mboy] = 0
    return img


def makeimage(img, imgname):
    cv2.imwrite(imgname, img)


def qualityImages(img):
    for i in range(90, 101):
        imgname = "kum." + str(i) + ".jpg"
        cv2.imwrite(imgname, img, [int(cv2.IMWRITE_JPEG_QUALITY), i])

# 100:150,150:200


def accuracy(img, ct, uzaklık):
    toplamsifir = ct
    d1x = [50, 100]
    d1y = [100, 150]
    d2x = [50, 100]
    d2y = [150, 200]
    # d1 kesişim r1
    d1 = 0

    print("ct = ", ct)
    for i in range(d1x[0], d1x[1]):
        for j in range(d1y[0], d1y[1]):
            if img[i, j] == 0:
                d1 = d1 + 1
    d2 = 0
    for i in range(d2x[0], d2x[1]):
        for j in range(d2y[0], d2y[1]):
            if img[i, j] == 0:
                d2 = d2 + 1

    p = (d2 + d1) / (2 * 50 * 50)

    toplam = 0
    for i in range(0, len(img)):
        for j in range(0, len(img[i])):
            if img[i, j] == 0:
                toplam = toplam + 1
    print("toplam:", toplam)
    toplam = toplam - toplamsifir
    birlesim = (toplam - d1 - d2) + (2 * (50 * 50))
    print(d1, d2)
    f = birlesim / (2 * 50 * 50)
    print(f)
    f = f - p
    print(f)
    file = open("uzalıklar.txt", 'a')
    file.write("p:" + str(p) + "\n" + "F:" + str(f) + "\n")
    file.write("\n" + "Uzaklık:" + str(uzaklık) + "\n")


def detectImages(ct):
    for i in range(5, 35):
        # imgname = "cat." + str(i) + ".jpg"
        imgname = "kum.png"
        img = cv2.imread(imgname, 0)
        print("Making block for " + str(imgname))
        liste = block(img)
        liste = np.int_(liste)
        print("Lex Sort..")
        sirali = liste[np.lexsort((liste[:, 1], liste[:, 0]))]
        print("Calculate distance..")
        # esikdegeri = esikdegeri - 3
        sonuclar = eslesme(sirali, i)
        print("Remove dublicate items..")
        img = removeimage(img, sonuclar)
        imgname = str("detect.") + str(i) + "." + str(imgname)
        makeimage(img, imgname)
        accuracy(img, ct, i)


def dublicateImage(img):
    dublicate = img[50:100, 100:150]
    img[50:100, 150:200] = dublicate
    return img



if __name__ == "__main__":
    mboy = 8
    ct = 0
    imagename = "DSC_0812tamp1.jpg"
    img = cv2.imread(imagename, 1)
    renksiz = cv2.imread(imagename, 0)
    for i in range(0, len(renksiz)):
        for j in range(0, len(renksiz[i])):
            if renksiz[i, j] == 0:
                ct = ct + 1
    img = dublicateImage(img)
    qualityImages(img)
    detectImages(ct)