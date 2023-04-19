#ROI - Region of Interest := Taking specific object , space from an object
#Background Subtraction - := From complete image just remove background
#Extracting object from the image and place on another image
#Random figure ROI or Background subtraction

import cv2
import numpy as np

img1 = cv2.imread(r"C:\Users\MSI\Desktop\1\21_thor.jpg")
img2 = cv2.imread(r"C:\Users\MSI\Desktop\1\21_storm_breaker.jpg")

img1 = cv2.resize(img1,(1024,750))
img2 = cv2.resize(img2,(450,450))


#I want to fix image 2 data into image 1 .
r,c,ch = img2.shape
roi = img1[0:r,0:c]

img_gry = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)


_,mask = cv2.threshold(img_gry,50,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

#put mask into roi 
img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
#cv2.imshow("image 1",img1_bg)

#Take only region of figure from original image
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)
#cv2.imshow("image 2",img2_fg)

#add
finali = cv2.add(img1_bg,img2_fg)
#cv2.imshow("final",finali)
img1[0:r,0:c]=finali
cv2.imshow("result",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

