#Draw date and Time and Figures on video

import cv2
import datetime


#cap = cv2.VideoCapture("C:\\Users\\MSI\\Desktop\\1\\vedio.mp4")

cap = cv2.VideoCapture(0)
print("for width",cap.get(3)) #for width
print("for height",cap.get(4)) #for height
while(cap.isOpened()):
    ret,frame = cap.read()
    frame = cv2.resize(frame,(1270,450))
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "HEIGHT: "+str(cap.get(4))+" WIDTH: "+str(cap.get(3))
        frame = cv2.putText(frame,text,(55,64),font,1,(0,155,255),5,cv2.LINE_AA)
        date_data = "Data: "+str(datetime.datetime.now())
        frame = cv2.putText(frame,date_data,(485,434),font,1,(145,155,255),5,cv2.LINE_AA)
        cv2.imshow("frame",frame)
        
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()

