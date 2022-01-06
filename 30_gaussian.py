'''
가우시안 블러 처리하기.
거리에 따른 가중치를 이용한다.

중심 픽셀이 가장 큰 가중치를 가지고, 인접 픽셀의 가중치는 줄인다.
sigma 값이 커질수록 흐릿해진다.
'''

import cv2
import numpy as np

img = cv2.imread('data/images/gaussian-noise.png',1 )

dst1 = cv2.GaussianBlur(img, (5,5), 1)
# 이미지, 커널 크기, 시그마 값 : 커질수록 흐릿해진다.

dst2 = cv2.GaussianBlur(img, (25,25), 10)

combined = np.hstack([img,dst1,dst2])

cv2.imshow("combined",combined)




cv2.waitKey(0)
cv2.destroyAllWindows()