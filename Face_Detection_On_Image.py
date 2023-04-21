# Face and Eye detection in image

#Face detection using Haarcascade file

import cv2
import numpy as np

image = cv2.imread(r"C:\Users\MSI\Desktop\1\faces.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #Convert into gray
#face = cv2.CascadeClassifier("C:\\Users\\MSI\\Desktop\\1\\haarcascade_frontalface_default.xml")
eye = cv2.CascadeClassifier("C:\\Users\\MSI\\Desktop\\1\\haarcascade_eye.xml")
#faces = face.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5)
eyes = eye.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
#for(x,y,w,h) in eyes:
    #image = cv2.rectangle(image,(x,y),(x+w,y+h),(127,232,205),3)
    #gray_roi = gray[y:y+h,x:x+w]
    #image_roi = image[y:y+h,x:x+w]
    
for(ex,ey,ew,eh) in eyes:
        cv2.rectangle(image,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

image = cv2.resize(image,(760,520))

cv2.imshow("Face detected",image)



cv2.waitKey(0)
cv2.destroyAllWindows()


