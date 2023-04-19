#HSV(Hue Saturation Value) Color scope

#detect color in an image

import cv2
import numpy as np
img = cv2.imread(r"C:\Users\MSI\Desktop\1\color-balls.jpg")

while True:
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    u_v = np.array([130,235,225])
    l_v = np.array([110,50,50])
    #Creating Mask
    mask = cv2.inRange(hsv,l_v,u_v)
    
    #filter mask with image
    res = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("frame",img)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    
    key = cv2.waitKey(1)
    if key==27:
        break

cv2.destroyAllWindows()