import cv2


img = cv2.imread('sample1.jpg') #READ AN IMAGE
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshImg = cv2.threshold(grayImage, 180,255,cv2.THRESH_BINARY)[1]
cv2.imwrite('thresholdImage2.jpg',threshImg) #WRITE AN IMAGE
