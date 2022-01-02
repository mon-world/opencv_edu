'''
호모그래피 변환
대응되는 4쌍의 점으로 이미지를 변환시킬 수 있다.
'''

import cv2
import numpy as np

img_src = cv2.imread('data/images/booke.jpg')


# 첫 번쨰 이미지의 점 4개
point_src = np.array([141, 131, 480, 159, 493, 630, 64, 601], dtype=float)
# 마우스 클릭 이벤트로 찾을 수 있다.
point_src = point_src.reshape(4,2)

print(point_src)

img_dst = cv2.imread('data/images/book1.jpg')

# 두 번째 이미지의 점 4개
point_dst = np.array([318,256, 534,372, 316,670, 73,473], dtype=float)
point_dst = point_dst.reshape(4,2)

print(point_dst)

# H : 호모그래피 변환에 사용된 3x3 행렬을 찾을 수 있다.

H, status = cv2.findHomography(point_src, point_dst)
## status는 1111 이네.
print(H)
print(status)


img_output = cv2.warpPerspective(img_src, H, (img_dst.shape[1], img_dst.shape[0]))
# 행렬을 좌표로 부를 때는 (열,행) 이다.
# 위 함수는 좌표를 받기 때문에 열 행 으로 해야한다.

cv2.imshow('SRC', img_src)

cv2.imshow('DST', img_dst)

cv2.imshow("Warp", img_output)






cv2.waitKey(0)
cv2.destroyAllWindows()