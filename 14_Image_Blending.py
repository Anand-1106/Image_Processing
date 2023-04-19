#image blending with openCV
#Here we use two important functions cv2.add(),cv2.addweighted() etc.
#Blending means adding of two images
#if you want to blend two images then both should have same size.

import cv2
import numpy as np


img1 = cv2.imread("C:\\Users\\MSI\\Desktop\\1\\image_blend_1.jpg")
img1 = cv2.resize(img1,(700,500))

img2 = cv2.imread("C:\\Users\\MSI\\Desktop\\1\\image_blend_2.jpg")
img2 = cv2.resize(img2,(700,500))

cv2.imshow("image1",img1)
cv2.imshow("image2",img2)

#Now perform Blending

img3 = img1+img2

cv2.imshow("Blended image",img3)
cv2.imwrite("C:\\Users\\MSI\\Desktop\\1\\blended_image.jpg",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()