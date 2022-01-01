import cv2
import numpy as np

source = cv2.imread('data/images/sample.jpg', 1)

cv2.imshow('original', source)

warpMat = np.array([1.2, 0.2, 2, -0.2, 1.3, 1])

warpMat = warpMat.reshape(2, 3)

result = cv2.warpAffine(source, warpMat,( int(1.5*source.shape[1]), int(1.5*source.shape[0])))
# 내가 만든 행렬로 변환하라
# 1.원본이미지 2.변환 행렬 3.데스티네이션 사이즈
# 행렬과 좌표 변환이기 때문에 크기를 저런 순서로 써준다.

cv2.imshow("result", result)

warpMat2 = np.array([1.2, 0.3, 2, 0.2, 1.3, 1])
warpMat2 = warpMat2.reshape(2, 3)

result2  = cv2.warpAffine(source, warpMat2,( int(1.5*source.shape[1]), int(1.5*source.shape[0])))

cv2.imshow("result2", result2)

cv2.waitKey(0)
cv2.destroyAllWindows()