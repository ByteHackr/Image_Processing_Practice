import numpy as np 
import cv2
#from statistics import mean  

img = cv2.imread("art.jpg")


height, width, channels = img.shape

# Create blank grayscale image
img_grayscale = np.zeros((height,width,1))

#s img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#print( width ) 
#print( height )
for i in np.arange(height):
    for j in np.arange(width):
        r = img.item(i,j,0)
        g = img.item(i,j,1)
        b = img.item(i,j,2)

        # RGB to Grayscale equation from google
        y = 0.299*r + 0.587*g + 0.144*b

        img_grayscale.itemset((i,j,0),int(y))

cv2.imwrite('image_grayscale.jpg',img_grayscale)
cv2.imshow('image',img_grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()
