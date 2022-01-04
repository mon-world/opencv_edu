'''
YCrCb의 Y값을 수정함으로써 밝기를 조절한다.

cv2.equalizeHist() 함수를 사용.
각각의 값이 전체 분포에 차지하는 비중에 따라 분포를 재분배해서, 명암 대비를 개선한다.
특정 영역에 집중되어 있는 분포를 골고루 분포시켜 평탄화 시킨다.
'''

import cv2
import numpy as np

img = cv2.imread('data/images/candle.jpg',1 )

ycbImage = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

Y, Cr, Cb = cv2.split(ycbImage)

# 히스토그램 균일화 화는 함수! cv2.equalizeHist() 함수를 이용하면 된다.
# 이 함수 자체가, 연산을 해서 결과를 주기 때문에, 이 함수 내부에서 알아서, float으로 바꾸고,
# 알아서 0~255사이의 값으로 다시 세팅해서, uint8로 바꿔서 돌려준다.

# 따라서 우리는 함수 호출만 하면 된다.

Y = cv2.equalizeHist(Y)

print(Y)
print(Y.dtype)

ycbImage = cv2.merge( [Y, Cr, Cb] )

ycbImage = cv2.cvtColor(ycbImage, cv2.COLOR_YCrCb2BGR)

combined = np.vstack( [img, ycbImage] )

cv2.imshow("combined", combined)


cv2.waitKey(0)
cv2.destroyAllWindows()