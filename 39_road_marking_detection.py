## 복-습

import cv2
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = cv2.imread('data2/image.jpg',1 )
# cv2.imshow('original', img)

# 우리가 필요한 건, 그레이 스케일 이미지.
image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray',image_gray)


image_copy = image_gray.copy() # 넘파이의 카피는 행렬을 그대로 카피해줌

print(image_copy.shape)


# 값이 195 미만인 것들은, 전부 0으로 셋팅한다
print( image_copy[ : , :] < 195)


image_copy[image_copy[ : , :] < 195] = 0

# cv2.imshow("copy",image_copy) ## 날씨 흐리거나 비가 오거나 밤이면 적용하기 힘들다.

image = cv2.imread('data2/test_image.jpg')
# cv2.imshow('img',image)

print('Height = ', image.shape[0], 'pixcels')
print('Width = ', image.shape[1], 'pixcels')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imshow('gray', gray_image)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# cv2.imshow('hsv', hsv_image)


# Hue 채널만 가져와서, 화면에 보이기

# H, S, V = cv2.split(hsv_image) <= 이렇게 해도 됨.


hsv_image_hue = hsv_image[:,:,0]

# cv2.imshow('Hue', hsv_image_hue)

image_2 = cv2.imread('data2/test_image2.jpg')
# cv2.imshow('image', image_2)

M_rotation = cv2.getRotationMatrix2D((image_2.shape[1]/2, image_2.shape[0]/2), 90, 0.5)
## 1.x좌표 중심,y좌표 중심 2.각도 3.사이즈

rotated_img = cv2.warpAffine(image_2, M_rotation, (image_2.shape[1], image_2.shape[0]))
## 1.이미지 2.어찌 돌림 3.전체 크기(검은색 포함)

# cv2.imshow('rotated', rotated_img)

image_3 = cv2.imread('data2/test_image3.jpg')
# cv2.imshow('image', image_3)

T_matrix = np.array([1, 0, 120, 0, 1, -150], dtype='float32') ## 행렬은 꼭 float32
T_matrix = T_matrix.reshape(2,3) ## 와프 아파인에 들어갈건 2행 3열 기억!!!

print(T_matrix)
# x축 120, y축 -150이
# 1 0 0 1 이므로 그냥 둬라 라는 의미

translation_image = cv2.warpAffine(image_3, T_matrix, (image_3.shape[1], image_3.shape[0]))
# cv2.imshow('tran', translation_image)
# 이동시키고 나머지는 자동으로 까만색으로 채움. 

resized_image = cv2.resize(image_3, None, fx=0.5, fy= 1.2, interpolation=cv2.INTER_LINEAR)
cv2.imshow('resize', resized_image)


cv2.waitKey(0)
cv2.destroyAllWindows()