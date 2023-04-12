#Screen Recording

import cv2
import pyautogui as p
import numpy as np

#create resolution
rs = p.size()

#filename in which we store recording
fn = input("please input file path")

#fix the frame rate
fps = 60.0

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter(fn,fourcc,fps,rs)

#create recording module
cv2.namedWindow("Live Recording",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live Recording",(760,660))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    output.write(f)
    cv2.imshow("Live Recording",f)
    if cv2.waitKey(1)==ord("q"):
        break

output.release()
cv2.destroyAllWindows()




#Break Video into Multiple images and save in folder

import cv2

vidcap = cv2.VideoCapture(0)
ret,image = vidcap.read()
count = 0

while True:
    if ret==True:
        cv2.imwrite("C:\\Users\\MSI\\Desktop\\1\\frames\\imgN%d.jpg"%count,image)
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(10*count**100))
        ret,image=vidcap.read()
        #image=cv2.resize(image,(600,360))
        cv2.imshow("res",image)
        count += 1
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
            cv2.destroyAllWindows()
    else:
        break

vidcap.release()
cv2.destroyAllWindows()

