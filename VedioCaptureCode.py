import cv2
cap = cv2.VideoCapture("C:\\Users\\MSI\\Desktop\\1\\vedio.mp4")
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter("C:\\Users\\MSI\\Desktop\\1\\outputs14561007.mp4",fourcc,20,(frame_width,frame_height))
while cap.isOpened():
    ret,frame = cap.read()
    if ret==True:
       cv2.imshow("frame",frame)
       output.write(frame)
       if cv2.waitKey(1) & 0xFF == ord('q'):
           break
       
cap.release()
output.release()
cv2.destroyAllWindows()