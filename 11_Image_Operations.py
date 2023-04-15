import cv2
import numpy as np

#image operations with pixels and co-ordinates
"""
#Read an image
img = cv2.imread("C:\\Users\\MSI\\Desktop\\1\\pikachu.jpg")
print("shape= ",img.shape) #returns the tuple of three values
print("no. of pixels",img.size) #return number of pixels 
print("datatype of image ",img.dtype)
print("type of img ",type(img))

#now try to split an image
#split - return 3 channels of image which is blue,green and red

#print(cv2.split(img))

b,g,r = cv2.split(img)

cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
cv2.imshow("pikachu",img)


#Now if you want to mix the channels then use merge
mr1 = cv2.merge((r,g,b))
cv2.imshow("merged",mr1)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""

#Working on pixel color values

img = cv2.imread("C:\\Users\\MSI\\Desktop\\1\\LION_hd.jpg")
cv2.imshow("lion",img)
print(img.shape)

#access a pixel value by its row and column coordinates value
px = img[520,580] #store coordinate in variable
print("the pixel values of that coordinates ",px)
#Now try to find selected channel value from coordinate
#we know we have three channels - 0,1,2

#for blue pixel
print("blue pixel= ",img[520,580,0])

#for green pixel
print("green pixel= ",img[520,580,1])

#for red pixel
print("red pixel = ",img[520,580,2])


cv2.waitKey(0)
cv2.destroyAllWindows()