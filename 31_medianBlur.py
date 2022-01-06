'''
메디안 블러 처리
관심화소 주변으로 지정한 커널크기 내의 픽셀을 크기순으로 정련한 후,
중간값을 뽑아서 픽셀값으로 사용한다.
'''

import cv2
import numpy as np

img = cv2.imread('data/images/gaussian-noise.png',1 )

dst1 = cv2.medianBlur(img, 5)
dst2 = cv2.medianBlur(img, 7)
# 1.이미지 2.필터 크기

combined = np.hstack([img,dst1,dst2])

cv2.imshow("combined", combined)




cv2.waitKey(0)
cv2.destroyAllWindows()