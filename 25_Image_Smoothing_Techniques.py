#Image Smoothing or bluring is most common used operation in Image Processing.
#It is use to remove noise from the images.
#There are so many filter  which is use for smoothing the image.
#There are LOW Pass Filter(LPS) which use to remove Noise from the images.
#There are High Pass Filter which use to detect and finding edges in an image.

#we discuss about various filters --
#like , homogeneous,blur(averaging),homogeneous,median,bilateral

import cv2
import numpy as np

img = cv2.imread(r"C:\Users\MSI\Desktop\1\noisy.jpg")
img = cv2.resize(img,(320,280))
cv2.imshow("blurredd image",img)

kernel = np.ones((9,9),np.float32)/81

#FILTER NUMBER -----1
#this filter  work like, each output pixel is the mean of its kernal neigbours
#it is aka homogeneous filter in this all pixel contribute with equal weight.
#kernal is a small shape or matrix which we apply on image.
#in this filter kernal is [(1/kernal(h,w))*kernal]
h_filter = cv2.filter2D(img,-1,kernel)
cv2.imshow("homogeneous",h_filter)

#FILtER NUMBER 2-----
#blur method or averaging
#takes the avg of all the pixels under kernel area and 
#replaces the central element with this average.
blur = cv2.blur(img,(8,8))
cv2.imshow("blur=",blur)

#Filter Number 3------
#Gaussian Filter -here it using different weight kernel,in  row as well as col.
#means side values are small then centre .It manage distance b/w value of pixel.
gau_blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("gau blur",gau_blur)

#Filter Number 4--
#Median Filter --computes the median of all the pixels under the 
#kernel window and the central pixel is replaced with this median value.
# This is highly effective in removing salt-and-pepper noise. 
#here kernal size must be odd except one
med = cv2.medianBlur(img,5)
cv2.imshow("median blur",med)

#bilateral filter --- is highly effective at noise removal while preserving edges.
#It work like gaussian filter but more focus on edges
#it is slow as compare with other filters
#argument (img, neigbour_pixel_diameter,sigma_color,sigma_space)
bi_f = cv2.bilateralFilter(img,9,75,75)
cv2.imshow("bilateral filter",bi_f)

cv2.waitKey(0)
cv2.destroyAllWindows()