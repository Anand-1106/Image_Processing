#Detecting colors using webcam and trackbars
import cv2
import numpy as np

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

def nothing(x):
    pass

cv2.namedWindow("Color Adjustments")
#Creating Trackbars

cv2.createTrackbar("Lower_H","Color Adjustments",0,255,nothing)
cv2.createTrackbar("Lower_S","Color Adjustments",0,255,nothing)
cv2.createTrackbar("Lower_V","Color Adjustments",0,255,nothing)

cv2.createTrackbar("Higher_H","Color Adjustments",255,255,nothing)
cv2.createTrackbar("Higher_S","Color Adjustments",255,255,nothing)
cv2.createTrackbar("Higher_V","Color Adjustments",255,255,nothing)

while True:
    _,frame = cap.read()
    frame = cv2.resize(frame,(400,400))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
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
    res = cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow("original frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
