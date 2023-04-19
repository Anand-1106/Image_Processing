#---------Morphological Transformation --------------
#Morphological transformations are some simple operations based on the image shape.
#It is normally performed on binary images. 
# It needs two inputs, 1)- original image, 2)- structuring element(kernel).
#Two basic Morphological Transformations are 1) - Erosion and 2) - Dilation

import cv2
import numpy as np
#Erosion---
#it erodes away the boundaries of foreground object

#kernal slides through all the image and all the pixel 
#from the original image conside 1 only if kernal's pixel is 1

img = cv2.imread(r"C:\Users\MSI\Desktop\1\23_color-balls.jpg",0)
img = cv2.resize(img,(430,260))
_,mask = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5),np.uint8)
e = cv2.erode(mask,kernel)

cv2.imshow("final",e)
cv2.imshow("mask",mask)
cv2.imshow("color-balls",img)

#Dilation -- 
#It is just opposite of erosion.
#Here, a pixel element is ‘1’ if atleast one pixel under the kernel is ‘1’
#So it inc. the white region in the image or size of foreground object in.
#Normally, in cases like noise removal, erosion is followed by dilation. 
#Because, erosion removes white noises, but it also shrinks our object. 

kernel = np.ones((3,3),np.uint8)
d = cv2.dilate(mask,kernel,iterations=4)
cv2.imshow("dilate",d)


import matplotlib.pyplot as plt

titles = ["images","mask","erosion","dilation"]
images = [img,mask,e,d]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

