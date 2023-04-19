#Color Detection using trackbars

import cv2
import numpy as np

img = cv2.imread(r"C:\Users\MSI\Desktop\1\color-balls.jpg")
img = cv2.resize(img,(600,400))


def nothing(x):
    pass

cv2.namedWindow("Color Adjustments")

#Creating Trackbars

cv2.createTrackbar("Lower_H","Color Adjustments",0,255,nothing)
cv2.createTrackbar("Lower_S","Color Adjustments",0,255,nothing)
cv2.createTrackbar("Lower_V","Color Adjustments",0,255,nothing)

cv2.createTrackbar("Higher_H","Color Adjustments",0,255,nothing)
cv2.createTrackbar("Higher_S","Color Adjustments",0,255,nothing)
cv2.createTrackbar("Higher_V","Color Adjustments",0,255,nothing)



#u_v = np.array([130,235,225])
#l_v = np.array([110,50,50])

#mask = cv2.inRange(hsv,l_v,u_v)
#mask = cv2.resize(mask,(600,400))
#cv2.imshow("mask",mask)

#res = cv2.bitwise_and(img,img,mask=mask)
#cv2.imshow("result",res)


while True:
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hsv = cv2.resize(hsv,(600,400))
    cv2.imshow("image",img)
    lower_h=cv2.getTrackbarPos('Lower_H', 'Color Adjustments')
    lower_s=cv2.getTrackbarPos('Lower_S', 'Color Adjustments')
    lower_v=cv2.getTrackbarPos('Lower_V', 'Color Adjustments')
    lower_v=np.array([lower_h,lower_s,lower_v])
    
    higher_h=cv2.getTrackbarPos('Higher_H', 'Color Adjustments')
    higher_s=cv2.getTrackbarPos('Higher_S', 'Color Adjustments')
    higher_v=cv2.getTrackbarPos('Higher_V', 'Color Adjustments')
    higher_v=np.array([higher_h,higher_s,higher_v])
    print(lower_v,higher_v)
    mask=cv2.inRange(hsv,lower_v,higher_v)
    res = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

