#In image Processing , thresholding is the simplest method of segmenting images
#Used to extract selected data from the image by using pixel values
#Also used to manage pixels and divide values in two parts
#Thresholding - Simple and Adaptive thresholding
#simple thresholding (img,pixel_thresh,_max_thresh_pixel,style)

import cv2
import numpy as np

img = cv2.imread(r"C:\Users\MSI\Desktop\1\black_white_thresholding.jpg",0)
img = cv2.resize(img,(400,400))

_, th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
_,th4 = cv2.threshold(img,120,255,cv2.THRESH_TOZERO)
_,th5 = cv2.threshold(img,120,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("1-Thresh Image",th1)
cv2.imshow("2-Thresh Image",th2)
cv2.imshow("3-Thresh image",th3)
cv2.imshow("4-Thresh image",th4)
cv2.imshow("5-Thresh image",th5)
cv2.imshow("real image",img)


cv2.waitKey(0)
cv2.destroyAllWindows()

