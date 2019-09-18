#from PIL import Image
#import numpy as np
#import sys
#import os
#import csv
#
##Useful function
#def createFileList(myDir, format='.jpg'):
#    fileList = []
#    print(myDir)
#    for root, dirs, files in os.walk(myDir, topdown=False):
#        for name in files:
#            if name.endswith(format):
#                fullName = os.path.join(root, name)
#                fileList.append(fullName)
#                return fileList
#
## load the original image
#myFileList = createFileList('IMMG')
#
#for file in myFileList:
#    print(file)
#    img_file = Image.open(file)
#    # img_file.show()
#
#    # get original image parameters...
#    width, height = img_file.size
#    format = img_file.format
#    mode = img_file.mode
#
#    # Make image Greyscale
#    img_grey = img_file.convert('L')
#    #img_grey.save('result.png')
#    #img_grey.show()
#
#    # Save Greyscale values
#    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
#    value = value.flatten()
#    print(value)
#    with open("img_pixels.csv", 'a') as f:
#        writer = csv.writer(f)
#        writer.writerow(value)
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)