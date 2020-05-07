import numpy as np 
import cv2

img = cv2.imread("parrotsec.png")
height, width, channels = img.shape

img_binary = np.zeros((height,width,1))

img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print (img_grayscale.shape)

#(thresh, img_binary) = cv2.threshold(img_grayscale, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

thresh = 15
for i in np.arange(height):
     for j in np.arange(width):
         x = img_grayscale.item(i,j)
         if x >= thresh:
             y = 1
         else :
             y = 0

         img_binary.itemset((i,j,0),int(y))

cv2.imwrite('image_binary.jpg',img_binary)
cv2.imshow('image',img_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
