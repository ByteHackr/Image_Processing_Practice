import numpy as np
import cv2

img1 = cv2.imread('Varence_Image_1.jpg')

img0 = cv2.imread('SD_Image_1.jpg')

img2 = cv2.imread('Gray Image.jpg')

img3 = 255 - img1

img0 = 255 - img0

img4 = (img3+img2)/2

cv2.imwrite("ABC.jpg",img4)

cv2.imwrite("DEF.jpg",img3)

t,img5= cv2.threshold(img2,127,255,cv2.THRESH_BINARY)

t,img6= cv2.threshold(img3,127,255,cv2.THRESH_BINARY)

t,img7 = cv2.threshold(img0,0,255,cv2.THRESH_BINARY)

cv2.imwrite("Org_b.jpg",img5)

cv2.imwrite("neg_v_b.jpg",img6)

cv2.imwrite("sd_b.jpg",img0)



