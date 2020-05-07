import numpy as np
import cv2
from skimage.segmentation import slic
import matplotlib.pyplot as plt
from skimage.segmentation import mark_boundaries

def imageResize(image):
    resize_image = cv2.resize(src=image, dsize=(600, 600))
    return resize_image

img = imageResize(cv2.imread('img_tamp_1.bmp'))

bgrImage = img [:, :, ::-1]  
segmentedData = slic(image=bgrImage, n_segments=1000)

figure = plt.figure()
axis = figure.add_subplot(1,1,1)
axis.imshow(mark_boundaries(bgrImage, segmentedData))
plt.axis("on")
plt.show()

print('Number of unique segments :', len(np.unique(segmentedData)))

