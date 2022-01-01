import cv2
import numpy as np


# 첫번째 사진의 3점의 좌표
input_triangle = np.array([50,50, 100,100, 200,150], dtype='float32')
# 플롯으로 연산하므로 데이터 타입을 이렇게 하였다.
# np.float32([50,50, 100,100 200,150])해도 된다.
# float 하면 float 64로 나오는데, cv2.getAffineTransform 함수는 float32를 받는다.

# 삼각형 세 점의 좌표로 변환
input_triangle = input_triangle.reshape(3,2)

print(input_triangle)



# 변환된 사진의 세 점의 좌표
output_triangle = np.array([70,76 , 142,101, 272,136], dtype='float32')

output_triangle = output_triangle.reshape(3,2)

print(output_triangle)

warpMat = cv2.getAffineTransform(input_triangle, output_triangle)

print(warpMat)