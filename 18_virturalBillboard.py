'''
이미지 찌그러뜨리기 - 합성
'''

import cv2
import numpy as np
from utils import get_four_points

# 이번에는,  똑바른 이미지를, 찌그러 뜨린 이미지로 변환하고자 한다.

img_src = cv2.imread('data/images/first-image.jpg', 1)
img_dst = cv2.imread('data/images/times-square.jpg', 1)
cv2.imshow("img src", img_src)
print(img_src.shape)
# (477, 600, 3)

# 똑바른 이미지의 4개 점 좌표를 가져오고,,
points_src = np.array([0,0,  img_src.shape[1], 0,   img_src.shape[1], img_src.shape[0] , 0, img_src.shape[0] ])
points_src = points_src.reshape(4,2)

print(points_src)
# 찌그러진 이미지의 4개 점은, 바로 못가져오니까, 마우스로 찍어서 점의 좌표를 받아온다.
points_dst = get_four_points(img_dst)
print(points_dst)

H, status = cv2.findHomography(points_src, points_dst)
print(H)
img_temp = cv2.warpPerspective(img_src, H, (img_dst.shape[1], img_dst.shape[0]))
cv2.imshow("Img temp", img_temp)

cv2.waitKey()
cv2.destroyAllWindows()
