import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('0.jpeg',0)
# img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

img_not = cv2.bitwise_not(img)

cv2.imshow("Pic",img)
 
cv2.imshow("Invert1",img_not)
cv2.imshow("Binary",th1)

cv2.waitKey(0)
cv2.destroyAllWindows()
