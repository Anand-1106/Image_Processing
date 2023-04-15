#creating image border
#with the help of cv2.copyMakeBorder() function.
#it take parameters like (img,border_width(4 sides),bordertype,val_border)
#border width = top,bottom,right,left
import numpy as np
import cv2

img1 = cv2.imread("C:\\Users\\MSI\\Desktop\\1\\lion.jpg")
brdr = cv2.copyMakeBorder(img1,10,10,5,5,cv2.BORDER_CONSTANT,value = [255,0,125])

cv2.imshow("lion",img1)
cv2.imshow("border waala ",brdr)
cv2.imwrite("C:\\Users\\MSI\\Desktop\\1\\lion_border_waala.jpg",brdr)

cv2.waitKey(0)
cv2.destroyAllWindows()

