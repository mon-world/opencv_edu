'''
라플라시안 필터
[[ 0 -1  0]
 [-1  4 -1]
 [ 0 -1  0]]
 가로 세로 성분으로 물체의 edge를 출력한다.
'''

import cv2
import numpy as np

img = cv2.imread('data/images/truth.png',1 )


laplacian = cv2.Laplacian(img, cv2.CV_32F, ksize = 3, scale = 1)


cv2.imshow('lap',laplacian)







cv2.waitKey(0)
cv2.destroyAllWindows()