# python program for convert an RGB image to a binary image

import cv2
#  read the image file as gray scale image
img = cv2.imread('m01.jpg',2)

# set the threshold value
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# show the image
cv2.imshow("Binary Image",bw_img)

# waitKey and destroyAllWindows method to keep our window always open until we press any key or close our window 
cv2.waitKey(0)
cv2.destroyAllWindows()