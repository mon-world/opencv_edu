## 이미지 영역을 구분하겠다는 것. 의미 있게!

## 에러 찾기 요망.

import numpy as np
import argparse
import time
import cv2
import os
import matplotlib.pyplot as plt
import imutils

SET_WIDTH = int(600)

normalize_image = 1 / 255.0
resize_image_shape = (1024,512)

sample_img = cv2.imread('data4/images/example_04.png')


# 원래는 opencv의 리사이즈 했는데 이번엔 imutils 사용
sample_img = imutils.resize(sample_img, width=SET_WIDTH) # 자동으로 비율 맞게 조정해줌


# cv2.imshow('ori', sample_img)

# opencv 의 pre-trained model을 통해서, 예측하기 위해서는
# 입력 이미지를 blob 으로 바꿔줘야 한다.

blob_img = cv2.dnn.blobFromImage(sample_img, normalize_image, resize_image_shape, 0, swapRB = False, crop = False)
# 1.이미지 2.1/255.0 3.리사이징 4.? 5.bgr을 rgb로 6.자르는거 사용하지 않는다.

# 시멘틱 세그멘테이션에 사용할 E-Net 모델을 가져온다.
cv_enet_model = cv2.dnn.readNet('data4/enet-cityscapes/enet-model.net') 

print(cv_enet_model) ## 클래스가 찍힘. 인공지능 가져온 것.

# 이미지를 넣어준다.
cv_enet_model.setInput(blob_img)

# 중요!!! 포워드 함수를 실행해서, 예측해 준다.

cv_enet_model_output = cv_enet_model.forward()
# 결과는 ~~~ 놓쳤네...?

# (1, 20, 512, 1024)
# 1 : 1개의 이미지를 넣었다는 뜻.
# 20 : 분류하는 클래스의 갯수.
# 512 : 행렬의 행 갯수.
# 1024 : 행렬의 열 갯수.
print(cv_enet_model_output.shape)


### 과연, 20개의 클래스 안에는 어떤 값이 들어있는거냐???

label_values = open('data4/enet-cityscapes/enet-classes.txt').read().split('\n')
# 줄바꿈 삭제하고 읽기
print(label_values)

# 맨 마지막 원소가 공백이므로, 제거하기 위해서
label_values = label_values[0 : -2+1]

IMG_OUTPUT_SHAPE_START = 1
IMG_OUTPUT_SHAPE_END = 4
classes_num, h, w =  cv_enet_model_output.shape[IMG_OUTPUT_SHAPE_START : IMG_OUTPUT_SHAPE_END]
# (1, 20, 512, 1024) 0 1 2 3 가져오므로 1 2 3 가져옴

### 중요 2!!!!!! 모델의 아웃풋 20개 행렬을, 하나의 행렬로 만든다.
class_map = np.argmax(cv_enet_model_output[0], axis=0) ## 20, 512, 1024 다 옴


print(class_map) ## 숫자로 있는게 아니므로 각각을 숫자로 맵핑해줌


# 시멘틱 세그멘테이션에 사용될 색 정보도 가져온다.
# 각 특징들에 색 주기 위해서
CV_ENET_SHAPE_IMG_COLORS = open('data4/enet-cityscapes/enet-colors.txt').read().split('\n')

print(CV_ENET_SHAPE_IMG_COLORS)

# 콤마를 구분으로 해서 데이터를 뽑는다.
# 문자열이므로 넘파이 어레이로 바꿔야 한다.
color_list = []
for color in CV_ENET_SHAPE_IMG_COLORS[ 0 : -2 + 1]:
    array = np.array(color.split(',')).astype('int') ## , 단위로 자른 것을 int로 가져와라
    color_list.append(array)
    

color_list = np.array(color_list)
print(color_list)


### 중요 3!!!!!! 하나의 행렬을 => 이미지로 만든다.
# 각 픽셀별로, 클래스에 해당하는 숫자가 적한 class_map을
# 각 숫자에 매칭되는 색깔로 셋팅해 준 것이다.
# 따라서 각 픽셀별 색깔 정보가 들어가게 되었다.
# 2차원 행렬을, 3차원 채널이 있는 BGR 행렬로 만든다.

# 위에 있는 이미지에 각 위치마다 클래스 정보가 있다. 여기선 20개
# 그리고 512 X 1024가 20개 있다는 뜻

mask_class_map = color_list[class_map]

# 리사이즈 한다.

mask_class_map = cv2.resize(mask_class_map, (sample_img.shape[1],sample_img[0]),interpolation=cv2.INTER_NEAREST  )
# 샘플 이미지에 맞게 리사이즈 함
# 바로 옆에 있는걸로 보강

class_map = cv2.resize(class_map, (sample_img.shape[1],sample_img[0]),interpolation=cv2.INTER_NEAREST  )
# 인풋 쉐입 맞춰주려고 줄인걸 다시 늘림

# 가중치 주기 : 두개 더함
cv_enet_model_output = ((0.4*sample_img) + (0.6*mask_class_map).astype('uint8'))



#### 색과 클래스가 무엇인지 화면에 보여주기 위한 레전드 셋팅 ####

# 화면에 색 정보를 표기하기 위한 레전드 생성 == 없어도 됨
# 색과 정보
# my_legend = np.zeros((len(label_values) * 25, 300, 3), dtype='uint8')

cv2.imshow("ori",sample_img)
cv2.imshow("output image",cv_enet_model_output)







cv2.waitKey(0)
cv2.destroyAllWindows()