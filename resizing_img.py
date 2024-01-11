
import cv2
import imutils

img = cv2.imread('sample1.jpg') #READ AN IMAGE
resiveImg = imutils.resize(img, width=20) #RESIZE AN IMAGE
cv2.imwrite('resizedImage.jpg',resiveImg) #WRITE AN IMAGE
