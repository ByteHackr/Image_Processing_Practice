# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 21:57:56 2019

@author: BILU
"""
import numpy as np

arr = np.empty((0),int)
with open("slid_time.txt","r") as file:
    n_data = file.readlines()
    for n_line in n_data:
        if len(n_line) > 1:
            print(int(n_line))
            arr = np.append(arr,([int(n_line)]))
            
print(arr)
n_file = open('new_data.txt','a')

with open("eye_possition_iris.txt","r") as file:
    data = file.readlines()
    
    for i in np.arange(len(arr) - 1):
        for line in data:
            word = line.split()
            if len(word) > 0:
                if int(word[-1]) >= arr[i] and int(word[-1]) < arr[i+1]:
                    n_file.write(line)
        n_file.write('@@')
        n_file.write('\n')
n_file.close()