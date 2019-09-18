import numpy as np
import cv2
from skimage.segmentation import slic
import matplotlib.pyplot as plt
from skimage.segmentation import mark_boundaries
def imageResize(image):
    resize_image = cv2.resize(src=image, dsize=(200, 200))
    return resize_image

#Main
img = imageResize(cv2.imread('images/img_orig_1.bmp'))

bgrImage = img[:, :, ::-1]  # convert to bgr
segmentedData = slic(image=bgrImage, n_segments=100, sigma=5)

#plotting
figure = plt.figure("SLIC Components")
axis = figure.add_subplot(1, 1, 1)
axis.imshow(mark_boundaries(bgrImage, segmentedData))
plt.axis("off")
plt.show()

print('Number of unique segments :', len(np.unique(segmentedData)))

