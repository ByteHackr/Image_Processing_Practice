import cv2

img = cv2.imread('Scan1.jpg')

img_height , img_width , dim = img.shape

#img = 255 - img

for i in range(0,int(img_height/3)):
	for j in range(0,int(img_width/3)):
		for k in range(0,dim):
			img[i][j][k] = 255 - img[i][j][k]

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
