'''
블러 처리한 이미지 출력하기
커널 사이즈가 커질수록 흐려진다.

픽셀의 값을 주변값의 평균으로 계산하게 하여 영상이 흐려진다.
'''
import cv2
import numpy as np

img = cv2.imread('data/images/gaussian-noise.png',1 )

# 3x3 커널을 컨볼루션해서 얻은 피쳐 맵 이미지 dst1
dst1 = cv2.blur(img, (3,3) )
# 블러 처리 : 이미지를 흐리게

# 7x7 커널을 컨볼루션 해서 얻은 피쳐 맵 이미지 dst2
dst2 = cv2.blur(img, (7,7))

print(dst1.shape)
print(img.shape)

cv2.imshow("dst1",dst1)
cv2.imshow("dst2",dst2)





cv2.waitKey(0)
cv2.destroyAllWindows()