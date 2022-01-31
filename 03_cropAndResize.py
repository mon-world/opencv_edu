# 이미지를 자르는 것을 crop 이라 함
# 사이즈 조절을 resize 라고 함

import cv2

# 1은 칼라 이미지, 0은 그레이스케일, -1은 알파채널포함한 이미지
source = cv2.imread('data/images/sample.jpg' , 1)
# 뒤에 1 이란 것도 칼라 가져와라 임. cv2.IMREAD_COLOR 임
# 레퍼런스를 알고 싶으면 python opencv cv2.imread로 검색
# 3개의 flag대신에 1, 0, -1을 사용해도 됨.

# 실수 값을 사용.
# 확대와 축소 
scaleX = 0.6 # x축은 60%
scaleY = 0.6

scaleDown = cv2.resize( source, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR) 
# 원하는 비율대로 조정 가능
# 이미지, x비율, y비율 순서
# 확대 축소 했을 떄 픽셀 유실됨. interpolation으로 채움

cv2.imshow('Original', source)
cv2.imshow('Scaled Down', scaleDown)

scaleX = 2.3
scaleY = 1.6

scaleUp = cv2.resize( source, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR) 

# cv2.imshow('Scaled Down', scaleUp)
# Crop : 내가 원하는 부분만 이미지를 자르는 것!
# 넘파이를 슬라이싱 하는것과 같다!!

crop_img = source[ 10:200 , 150:250  ]

cv2.imshow("Crop Img",crop_img)

cv2.waitKey(0)
cv2.destroyAllWindows()