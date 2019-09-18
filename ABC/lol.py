#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:16:03 2019

@author: sandipan
"""

a=[2,58,65,47,64]
n=len(a)
x=input("Enter an Integer Number between 0 & 99 for search\n")
for i in range(0,n):
    if(a[i]==x):
        print('matched')
        print('found at index',a[x])
    else:
        print('not found')