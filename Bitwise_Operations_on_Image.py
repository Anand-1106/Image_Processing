#Bitwise Operations on Image
#Bitwise Operations includes AND,OR,NOT and XOR
#It is most important and used for various purpose like masking and find (ROI) which is in complex shape.

import cv2
import numpy as np

img1 = np.zeros((250,500,3),np.uint8)
img1 = cv2.rectangle(img1,(150,100),(200,250),(255,255,255),-1)


img2 = np.zeros((250,500,3),np.uint8)
img2 = cv2.rectangle(img2,(10,10),(170,190),(255,255,255),-1)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)

#bit_and_img = cv2.bitwise_and(img2,img1)

#bit_or_img = cv2.bitwise_or(img2,img1)

#bitNot01 = cv2.bitwise_not(img1)
#bitNot02 = cv2.bitwise_not(img2) 

bitXor = cv2.bitwise_xor(img1,img2)

cv2.imshow("opeartion image",bitXor)

cv2.waitKey(0)
cv2.destroyAllWindows()