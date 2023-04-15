#In this vedio we talk about Region of Interest
import numpy as np
import cv2

#read

img = cv2.imread("C:\\Users\\MSI\\Desktop\\1\\thor.jpg")
img = cv2.resize(img,(1060,780))

#ROI (Region of Interest)
#(435,23) (645,196)

roi = img[23:196,435:645]

#Now passing data into image
img[23:196,645:855]=roi
img[23:196,225:435]=roi
cv2.imshow("head",roi)

cv2.imshow("thor image",img)
cv2.imwrite(r"C:\Users\MSI\Desktop\1\roi_image.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()