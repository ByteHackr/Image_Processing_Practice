import numpy as np
import cv2
from matplotlib import pyplot as plt



path = "me.png"
img = cv2.imread(path,0)

#To display image before equalization
# cv2.imshow('image',img)
# cv2.waitKey(0)


# a = np.zeros((256,),dtype=np.float16)
# b = np.zeros((256,),dtype=np.float16)

height,width=img.shape
hist = np.zeros(256,dtype=int)

""" Histogram Manually Create """
print(hist)
for i in range(0,int(height)):
    for j in range(0,int(width)):
        hist[img[i][j]]+= 1

plt.plot(hist)
#finding histogram
# for i in range(width):
#     for j in range(height):
#         g = img[j,i]
#         a[g] = a[g]+1

# print(a)   
# plt.plot(a)


# #performing histogram equalization
# tmp = 1.0/(height*width)
# b = np.zeros((256,),dtype=np.float16)

# for i in range(256):
#     for j in range(i+1):
#         b[i] += a[j] * tmp;
#     b[i] = round(b[i] * 255);

# # b now contains the equalized histogram
# b=b.astype(np.uint8)

# print(b)

# #Re-map values from equalized histogram into the image
# for i in range(width):
#     for j in range(height):
#         g = img[j,i]
#         img[j,i]= b[g]

# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 
