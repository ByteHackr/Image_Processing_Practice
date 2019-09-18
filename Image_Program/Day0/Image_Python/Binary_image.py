import cv2
import numpy as np

img = cv2.imread('Scan1.jpg')

img_height , img_width , dim = img.shape


for i in range(0,int(img_height)):
	for j in range(0,int(img_width/2)):
			if img[i][j][0] >= 128 or img[i][j][1] >= 128 or img[i][j][2] >= 128:
				img[i][j][0] = 255
				img[i][j][1] = 255
				img[i][j][2] = 255
			if img[i][j][0] <128 or img[i][j][1] <128 or img[i][j][2] <128:
				img[i][j][0] = 0
				img[i][j][1] = 0
				img[i][j][2] = 0

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
