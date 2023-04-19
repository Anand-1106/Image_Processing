import cv2
import numpy as np

#Opening
#Opening is just another name of erosion followed by dilation
#means first erosion takes place then dilation

img = cv2.imread(r"C:\Users\MSI\Desktop\1\23_color-balls.jpg",0)
img = cv2.resize(img,(430,260))

_,mask = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((6,6),np.uint8)
o = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

cv2.imshow("image",img)
cv2.imshow("mask",mask)
cv2.imshow("opening",o)

#Closing
#It is opposite of opening
#Closing is just another name of dilation followed by erosion
#means first dilation takes place then erosion
kernel = np.ones((6,6),np.uint8)
c = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
cv2.imshow("closing",c)

#--------Optional ----

x1 = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)   #diff b/w mask and opening
x2 = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel) #diff b/w dilation and erosion
x3 = cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernel)  
cv2.imshow("x1",x1) 
cv2.imshow("x2",x2) 
cv2.imshow("x3",x3) 


cv2.waitKey(0)
cv2.destroyAllWindows()