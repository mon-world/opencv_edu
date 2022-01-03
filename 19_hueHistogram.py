'''
HSV
H : Hue 색상
S : Saturation 채도
V : Value 명도
'''

import cv2
import numpy as np

img = cv2.imread('data/images/sample.jpg', 1)

cv2.imshow("color", img)

# gray scale image

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

cv2.imshow("gray", gray_img)

# HSV image

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("hsv", hsv_img)
# imshow는 BGR이라 생각하고 화면에 표시함. 따라서 HSV로 되어있는 것도 BGR값으로 인식한다.

# 밝기를 -100 한 후에, 이미지를 다시 표시해보자.

hsv_img[2] = hsv_img[2] - 100 # 2번째 array가 value. 즉, brightness 이므로.

# 밝기 조절을 했으니, 화면에 표시하기 위해서는, BGR로 다시 바꿔주면 된다.

bgr_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

cv2.imshow("bgr_img", bgr_img)

cv2.waitKey(0) 
cv2.destroyAllWindows()

