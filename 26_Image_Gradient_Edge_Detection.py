# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 17:46:11 2023

@author: MSI
"""

import cv2
import numpy as np

img = cv2.imread(r"C:\Users\MSI\Desktop\1\avengers.webp")
img = cv2.resize(img,(560,380))
cv2.imshow("image",img)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image",img_gray)

lap = cv2.Laplacian(img_gray,cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("laplacian",lap)


sobelX = cv2.Sobel(img_gray,cv2.CV_64F,1,0,ksize=3)
sobelY = cv2.Sobel(img_gray,cv2.CV_64F,0,1,ksize=3)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))


cv2.imshow("sobelx",sobelX)
cv2.imshow("sobelY",sobelY)
added = cv2.add(sobelX,sobelY)
cv2.imshow("combined",added)
cv2.waitKey(0)
cv2.destroyAllWindows()