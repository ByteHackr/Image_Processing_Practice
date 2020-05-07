import cv2
import numpy as np

img = cv2.imread('Scan1.jpg')

img_height , img_width , dim = img.shape

cv2.imshow('image1',img[0:int(img_height/2),0:int(img_width/2)])
cv2.imshow('image2',img[int(img_height/2):img_height,0:int(img_width/2)])
cv2.imshow('image3',img[0:int(img_height/2),int(img_width/2):img_width])
cv2.imshow('image4',img[int(img_height/2):img_height,int(img_width/2):img_width])

cv2.waitKey(0)
cv2.destroyAllWindows()
