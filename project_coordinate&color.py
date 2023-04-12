#function to find coordinate and color of any pixel
import cv2
import numpy as np

def mouse_event(event,x,y,flag,param):
    print("x: ",x)
    print("y: ",y)
    print("flag: ",flag)
    print("param: ",param)
    font = cv2.FONT_HERSHEY_PLAIN
    if event== cv2.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        cord = ". "+str(x)+', '+str(y)
        cv2.putText(img,cord,(x,y),font,1,(0,255,255),2)
        #cv2.imshow("image",img)
    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[y,x,0] #for blue channel
        g = img[y,x,1] #for green channel
        r = img[y,x,2] #for red channel
        
        color_bgr = ". "+str(r)+", "+str(g)+", "+str(r)
        cv2.putText(img,color_bgr,(x,y),font,1,(5,2,245),2)
        #cv2.imshow("image",img)

cv2.namedWindow(winname="res")
cv2.setMouseCallback("res",mouse_event)


img = cv2.imread("C:\\Users\\MSI\\Desktop\\1\\download.jpg")
while True:
    cv2.imshow("res",img)
    if cv2.waitKey(1) & 0xFF==27:
        break

cv2.destroyAllWindows()

