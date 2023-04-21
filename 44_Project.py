#Face Detection using webcam
import cv2
import numpy as np
face = cv2.CascadeClassifier(r"C:\Users\MSI\Desktop\1\haarcascade_frontalface_default.xml")

eye = cv2.CascadeClassifier(r"C:\Users\MSI\Desktop\1\haarcascade_eye.xml")
def detector(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(127,0,125),2)
        
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        eyes = eye.detectMultiScale(roi_gray,1.3,3)
        for(ex,ey,ew,eh) in eyes:
            cv2.circle(roi_color,(ex+27,ey+27),20,(255,0,0),2)
        
    return img

cap = cv2.VideoCapture(r"C:\Users\MSI\Desktop\1\vedio2.mp4")
while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,2)
    cv2.imshow("face detection",detector(frame))
    if cv2.waitKey(1)==13:
        break
    
cap.release()
cv2.destroyAllWindows()

