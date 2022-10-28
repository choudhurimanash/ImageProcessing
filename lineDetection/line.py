# pyhton program to detect lines

import cv2
import numpy as np

src_img = cv2.imread('l01.jpg')
# gray = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)

dst_img = cv2.Canny(src_img, 50, 200, None, 3)

linesP = cv2.HoughLinesP(dst_img, 1, np.pi / 180, 50, None, 50, 10)

for i in range(0, len(linesP)):
            lin = linesP[i][0]
            cv2.line(src_img, (lin[0], lin[1]), (lin[2], lin[3]), (0,0,255), 3, cv2.LINE_AA)

cv2.imshow("Image with lines", src_img)
cv2.waitKey(0)