#drawing function in opencv

import numpy as np
import cv2

img = cv2.imread("C:\\Users\\MSI\\Desktop\\1\\download.jpg")
img = cv2.resize(img,(760,480))

#here line accept five parameters (img,start,end,color,thickness)
img = cv2.line(img,(0,0),(756,474),(154,92,452),8)

#arrowed line also accept five parameters(img,start,end,color,thickness)
img = cv2.arrowedLine(img,(0,125),(256,324),(345,56,15),10)

#rectangle accept image,start_co,end_co,color,thickness
img = cv2.rectangle(img,(620,162),(716,268),(12,34,456),-3)

#circle accept image,start_co,radius,color,thickness
img = cv2.circle(img,(679,75),43,(214,255,0),-5)

#putText accept(image,text,start_co,font,fontsize,color,thickness,linetype)
font = cv2.FONT_ITALIC
img = cv2.putText(img,"Avengers",(20,250),font,4,(0,125,255),3,cv2.LINE_AA)

#ellipse accept(image,start_co,(length,height),color,thickness)
img = cv2.ellipse(img,(200,300),(100,50),0,0,270,200,2)

black_img = np.zeros([512,512,3],np.uint8)*255
white_img = np.ones([512,512,3],np.uint8)*255
pts = np.array([[100,150],[200,30],[170,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img_pts = cv2.polylines(img,[pts],True,(0,255,155))

cv2.imshow("black image",black_img)
cv2.imshow("white image",white_img)
cv2.imshow("image pts",img_pts)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

