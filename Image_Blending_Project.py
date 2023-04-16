#Image Blending Project using Trackbars

import cv2
import numpy as np
img1 = cv2.imread(r"C:\Users\MSI\Desktop\1\blend_project_01.jpg")
img1 = cv2.resize(img1,(700,700))

img2 = cv2.imread(r"C:\Users\MSI\Desktop\1\blend_project_02.jpg")
img2 = cv2.resize(img2,(700,700))

cv2.imshow("image1",img1)
cv2.imshow("image2",img2)


def blend(x):
    pass

img = np.zeros((400,400,3),np.uint8)
cv2.namedWindow('win') #create track bar windows
cv2.createTrackbar('alpha','win',1,100,blend)
switch = '0:off \n 1:on' #create switch to invoke the trackbars

cv2.createTrackbar(switch,'win',0,1,blend) #create trackbars for switch

while True:
    s = cv2.getTrackbarPos(switch,"win")
    a = cv2.getTrackbarPos("alpha","win")
    n = float(a/100)
    
    if s==0:
        dst = img[:]
    else:
        dst = cv2.addWeighted(img1,1-n,img2,n,0)
        cv2.putText(dst,str(a),(20,50),cv2.FONT_ITALIC,2,(0,125,255),2)
    cv2.imshow("dst",dst)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
    

cv2.waitKey(0)
cv2.destroyAllWindows()

