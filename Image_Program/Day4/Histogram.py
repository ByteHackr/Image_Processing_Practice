# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:48:15 2019

@author: BILU
"""

import numpy as np
from matplotlib import pyplot as plt
arr = np.array([0,1,1,1,1,2,2,2,3,3,3,3,4,4,4,5,5,6,6,6,7,7,8])


#arr = np.array([0,0,0,2,2,2,2,2,2,3,3,3,3,6,6,6,6,6,6,6,6,6,7,8,9])
hist , bins = np.histogram(arr,bins=np.arange(10))
plt.title('Numpy Histogram')
plt.plot(hist)
plt.show()
sum = 0 
for i in range(0,len(hist)):
    sum = sum + i*hist[i]
    
print('Threshold: ',sum/len(arr))