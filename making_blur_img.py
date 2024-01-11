import cv2


img = cv2.imread('resizedImage.jpg') #READ AN IMAGE
gaussionaBlurImg = cv2.GaussianBlur(img,(21,21),0) #RESIZE AN IMAGE
cv2.imwrite('gaussianImage.jpg',gaussionaBlurImg) #WRITE AN IMAGE
