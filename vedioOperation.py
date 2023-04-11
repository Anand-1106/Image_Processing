import cv2
"""
cap = cv2.VideoCapture("C:\\Users\\MSI\\Desktop\\1\\vedio.mp4")
print("capture",cap)

while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(1250,740))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    cv2.imshow("grayscale",gray)
    k = cv2.waitKey(25)
    if k==ord("q") & 0xFF:
        break
"""
#Now capture video from webcam and save into memory
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("C:\\Users\\MSI\\Desktop\\1\\outputs.mp4",fourcc,20.0,(640,480),0)
print(cap)
while cap.isOpened():
    ret,frame = cap.read()
    if ret==True:
       #frame = cv2.resize(frame,(250,140))
       frame = cv2.flip(frame,0)
       gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
       cv2.imshow("frame",frame)
       cv2.imshow("grayscale",gray)
       output.write(gray)
       if cv2.waitKey(1) & 0xFF == ord('q'):
           break
cap.release()
output.release()
cv2.destroyAllWindows()