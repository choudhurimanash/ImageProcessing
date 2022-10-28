# python program for convert rgb image to gray scale image

import cv2

#read the image
img_rgb = cv2.imread('m02.jpg')

# Use the cvtColor() function to grayscale the image
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

#show the image  
cv2.imshow('Gray image', img_gray)

# waitKey and destroyAllWindows method to keep our window always open until we press any key or close our window   
cv2.waitKey(0)
cv2.destroyAllWindows()
