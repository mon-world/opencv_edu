'''
conv를 통해 노이즈를 줄인다.
'''

import cv2
import numpy as np

img = cv2.imread('data/images/gaussian-noise.png',1 )
# 노이즈 있는 이미지

cv2.imshow("img",img )

# 컨볼루션 하기 위해서는 kernel(커널) 또는 filter 의 사이즈가 있어야 한다.

kernel_size = 5

# 이미지는 위치 정보도 포함하기 때문에 행렬로 한다.
kernel = np.ones( (kernel_size, kernel_size) ) / kernel_size ** 2 

print(kernel)

# opencv 에서의 컨볼루션 함수는 cv2.filter2D 라는 함수를 이용한다.

result = cv2.filter2D(img, -1, kernel)
# 피쳐맵 출력

combined = np.hstack([img, result])
cv2.imshow("combined", combined)





cv2.waitKey(0)
cv2.destroyAllWindows()