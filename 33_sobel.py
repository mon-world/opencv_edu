'''
소벨 마스크

수직 마스크 : 세로 성분을 검출한다.
[[-1  0 -1]
 [-2  0 -2]
 [-1  0 -1]]

수평 마스크 : 가로 성분을 검출한다.
[[ 1  2  1]
 [ 0  0  0]
 [-1 -2 -1]]
'''

import cv2
import numpy as np

img = cv2.imread('data/images/truth.png',1 )

cv2.imshow('sobel', img)


sobelX = cv2.Sobel(img, cv2.CV_32F, 1, 0)

sobelY = cv2.Sobel(img, cv2.CV_32F, 0,1 )


cv2.imshow('sobelX', sobelX)
cv2.imshow('sobelY', sobelY)




cv2.waitKey(0)
cv2.destroyAllWindows()