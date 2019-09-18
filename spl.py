#import cv2
#import numpy as np
#from matplotlib import pyplot as plt
#
#im = cv2.imread('art.jpg',cv2.IMREAD_GRAYSCALE)
#
#plt.imshow(im, cmap = 'gray', interpolation = 'bicubic')
## to hide tick values on X and Y axis
#plt.xticks([]), plt.yticks([])
#plt.plot([200,300,400],[100,200,300],'c', linewidth = 5)
#plt.show()


                            ####Gray Image #####
import numpy as np
import cv2
#def rgb_to_gray(img):
#        grayImage = np.zeros(img.shape)
#        R = np.array(img[:, :, 0])
#        G = np.array(img[:, :, 1])
#        B = np.array(img[:, :, 2])
#
#        R = (R *.299)
#        G = (G *.587)
#        B = (B *.114)
#
#        Avg = (R+G+B)
#        grayImage = img
#
#        for i in range(3):
#           grayImage[:,:,i] = Avg
#
#        return grayImage       
#
#image = cv2.imread("art.jpg")   
#grayImage = rgb_to_gray(image)  
#cv2.imshow('image',grayImage)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#
#

#def dev(img):
#        grayImage = np.zeros(img.shape)
#        R = np.array(img[:, :, 0])
#        G = np.array(img[:, :, 1])
#        B = np.array(img[:, :, 2])

# using matplotlib and numpy 
#import numpy as npy 
#import cv2
## reading image in variable m 
#m = cv2.imread("parrotsec.png") 
#  
## determining dimesion of image width(w) height(h) 
#w, h,c = m.shape
#  
## required image size after cropping 
#xNew = int(w * 1 / 10) 
#yNew = int(h * 1 / 10) 
#newImage = npy.zeros([xNew, yNew, 1]) 
#  
## print width height of original image 
#print(w) 
#print(h) 
#  
#for i in range(1, xNew): 
#    for j in range(1, yNew): 
#       # cropping start from 100, 100 pixel of original image 
#        newImage[i, j,0]= m[100 + i, 100 + j,0] 
#  
#cv2.imshow('image',newImage)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


import numpy as np
import cv2
from PIL import Image
from scipy import ndimage 
#def vr(x):
#    rows, cols = 500, 50000
#    win_rows, win_cols = 5, 5
#    img = np.random.rand(rows, cols)
#    win_mean = ndimage.uniform_filter(img, (win_rows, win_cols))
#    win_sqr_mean = ndimage.uniform_filter(img**2, (win_rows, win_cols))
#    win_var = win_sqr_mean - win_mean**2
#    return win_var
#
#print (x)
#x=vr()
#img = cv2.imread("code.jpg")
#print (img.shape)

#def get_image(image_path):
#    """Get a numpy array of an image so that one can access values[x][y]."""
#    image = Image.open(image_path, 'r')
#    width, height = image.size
#    pixel_values = list(image.getdata())
#    if image.mode == 'RGB':
#        channels = 3
#    elif image.mode == 'L':
#        channels = 1
#    else:
#        print("Unknown mode: %s" % image.mode)
#        return None
#    pixel_values = np.array(pixel_values).reshape((width, height, channels))
#    return pixel_values
#
#
#get_image('parrotsec.png')

photo = Image.open('parrotsec.png') #your image
photo = photo.convert('RGB')

width = photo.size[0] #define W and H
height = photo.size[1]

for y in range(0, height): #each pixel has coordinates
    row = ""
    for x in range(0, width):

        RGB = photo.getpixel((x,y))
        R,G,B = RGB
#        for i in range(0,255):
#            add=R+(R+1)+(R+2)
#            print (add)
        print(R,G,B)
#        r=np.matrix(RGB)
#        S=r.var()
#        S=int(S)
#img=Image.new('RGB',(600,600),color=(S))
#img.save('sandipan.png')
#
#        for i in range(0,)



#import cv2
#
#img = cv2.imread('parrotsec.png')
#for i in range(0,600):
#    for j in range(0,600):
#        x=0
#        y=0
#        print img[x,y]
#for x in range(0,)            
#print photo[0,0]









#FILENAME='code.jpg' 
#im=Image.open(FILENAME).convert('RGB')
#pix=im.load()
#w=im.size[0]
#h=im.size[1]
##[m,n]=size(FILENAME)
#for i in range(w):
#  for j in range(h):
#    print pix[i,j]
#    add=(i+j)
#    print(add)
#countw=0
#block=cell(m/16,n/16)
#for i in range(1,16,m-15):
#    counti=countw+w
#    counti=0
#    for j in range(1,16,m-15):
#        countj=countj+1
#            


#import numpy as numpy
#
#grey_levels = 256
## Generate a test image
#test_image = numpy.random.randint(0,grey_levels, size=(11,11))
#
## Define the window size
#windowsize_r = 5
#windowsize_c = 5
#
#def crp():
## Crop out the window and calculate the histogram
#    for r in range(0,test_image.shape[0] - windowsize_r, windowsize_r):
#            for c in range(0,test_image.shape[1] - windowsize_c, windowsize_c):
#                window = test_image[r:r+windowsize_r,c:c+windowsize_c]
#                hist = numpy.histogram(window,bins=grey_levels)
#                #print(hist)
##                fim = np.zeros(window.shape)
#                print(r,c,hist)    
##                cv2.imshow('image',fim)
##                cv2.waitKey(0)
##                cv2.destroyAllWindows()
#
#
#crp()



#from PIL import Image
#import numpy as np
#import matplotlib.pyplot as plt
#
#
#
#grayImage = cv2.imread('parrotsec.png')
##cv2.imshow(grayImage)
#stdImage = cv2.meanStdDev(grayImage)
#varianceImage = (stdImage*2)
#cv2.imshow('var',varianceImage)
#cv2.waitKey(0)
#cv2.destroyAllWindows()












