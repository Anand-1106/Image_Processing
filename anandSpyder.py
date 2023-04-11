import cv2
img1 = cv2.imread("C:\\Users\\MSI\\Desktop\\download.jpg",1)
img1 = cv2.resize(img1,(1280,780))
print(img1)
cv2.imshow("original",img1)

img2 = cv2.imread("C:\\Users\\MSI\\Desktop\\download.jpg",0)
img2 = cv2.resize(img2,(1280,780))
print(img2)
cv2.imshow("gray scale image",img2)

img3 = cv2.imread("C:\\Users\\MSI\\Desktop\\download.jpg",-1)
img3 = cv2.resize(img3,(1280,760))
print(img3)
cv2.imshow("unchanged",img3)

#image conversion from colored to grayscale

path = input("enter the path")
print("your path ",path)
img4 = cv2.imread(path,0)
img4 = cv2.resize(img4,(1260,760))
cv2.imshow("grayscale image",img4)

k = cv2.waitKey(0)

if k ==ord("s"):
    cv2.imwrite("C:\\Users\\MSI\\Desktop\\grayscale.png",img4)

else:
    cv2.destroyAllWindows()


