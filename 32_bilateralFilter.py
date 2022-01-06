'''
bilateral filter
에지를 보전하면서 노이즈를 감소시킨다.
'''
import cv2
import numpy as np

img = cv2.imread('data/images/gaussian-noise.png',1 )

result = cv2.bilateralFilter(img, 15, 80, 80 )
# 1.이미지 2.커널 사이즈 
# 3.sigmaColor : 클수록 이웃한 픽셀과 기준 색상의 영향이 커짐
# 4. sigmaSpace : 커질수록 긴밀하게 주변 픽셀에 영향을 미침

combined = np.hstack([img,result])

cv2.imshow("combined", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()