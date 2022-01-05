'''
이미지의 느낌을 붉은 느낌이 강하도록 변경.
레드 커브를 사용하고, 그 값에 맞게 대응시켜준다.
'''

import cv2
import numpy as np

original = cv2.imread('data/images/girl.jpg',1 )
# 읽을 때도 BGR로 가져온다.

cv2.imshow("original", original)

img = original.copy()

# 행렬에 들어있는, 원래의 기준값. 6개를 세팅한다.
# 원래의 대칭값인, 0은0, 50은50, 100은 100
originalValue = np.array([0, 50, 100, 150, 200, 255])

# 위의 기준값에 매칭되는, 6개의 값 셋팅
# 이 값은, 기준값보다 높은 값들이다.
# 즉, 기준값이 있으면, 그 값을, 아래의 값으로 올려서 매칭됨.
rCurve = np.array([0, 80, 150, 190, 220, 255])   # 레드 커브
# 오리지널이 기준. 50 => 80, 200 => 220 등으로 바꿈

# 위 기준값에 매칭되는 6개의 값인데, 각 기준값보다 작은 값으로 매칭됨.
bCurve = np.array([0, 20, 40, 75, 150, 255])

# Lookup table 만들기
# 현재 6개의 기준점만 가지고 있다.
# 그렇지만 우리는, 256개의 모든 점으로 만들어 줘야 한다.
# 그래야, 0~255까지의 값들을, 해당 룩업테이블로 매칭시켜 줄 수 있기 때문에,
# 6개의 기준점을 가지고, 총 256개의 매칭점들을 도출해야함!

fullrange = np.arange(0, 255+1)

# 특정 갯수의 점들로, 점들을 늘리는 방법
rLUT = np.interp(fullrange, originalValue, rCurve)
# 1.기준점 2.원래 값 3.원래 값을 변경할 값
# 디스크립 데이터 포인트를 만들어 준다.
# 인터폴레이션은 사이값들을 채워준다. 보강.
# LUT = 룩 업 테이블

# print(fullrange)
# print(rLUT)

bLUT = np.interp(fullrange, originalValue, bCurve)


# 원래의 원본 이미지에서, 우리는 R채널만 가져와서, rLUT를 적용하면 되고,
# B 채널만 가져와서, bLUT를 적용하면 된다.
# 채널 만들기

# B, G, R = cv2.split(img)
# 슬라이싱으로도 split을 구현할 수 있다.
B = img[ : , : , 0 ]
G = img[ : , : , 1 ]
R = img[ : , : , 2 ]
# 1.행의 정보 2.열의 정보 3.채널

# B채널만 가져와서, bLUT를 적용하면 된다.
# rLUT를 R에 적용하라. 룩업테이블로.
B = cv2.LUT(B, bLUT)
R = cv2.LUT(R, rLUT)

img[ : , : , 0 ] = B
img[ : , : , 1 ] = G
img[ : , : , 2 ] = R

# 슬라이싱을 사용하였으므로, merge 할 필요가 없다.

combined = np.vstack([original, img])

cv2.imshow("combined", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()