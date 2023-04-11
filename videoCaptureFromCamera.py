"""import cv2

camera = "https://192.168.113.154:8080/video"

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(camera)

print("check===",cap.isOpened())

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("C:\\Users\\MSI\\Desktop\\1\outputk.mp4",fourcc,20.0,(648,480),0)
print(cap)
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret==True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Colorframe",frame)
        output.write(gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
output.release()
cv2.destroyAllWindows()

"""

#Capture video from youtube

import cv2
import pafy

url = "https://www.youtube.com/watch?v=isFkFWxu21c"
data = pafy.new(url )
data = data.getbest(preftype="mp4")

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(data.url)

#print("check===",cap.isOpened())


#print(cap)

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret==True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Colorframe",frame)
        cv2.imshow("grayscale",gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()