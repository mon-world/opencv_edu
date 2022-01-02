import cv2
import numpy as np

from utils import get_four_points

# 이미지 코렉션을 하기 위한 원본 이미지 가져오기.
img_src = cv2.imread('data/images/my1_thumb.jpg')

cv2.imshow("Image", img_src)


# 원본 이미지로부터 correction 결과를 표시함, 결과 이미지 생성
# 까만색 이미지로 생성한다.

# 마우스 클릭 하면 새로운 사진이 나오게 함
dst_size = (300, 400, 3)

# 넘파이 어레이로 만들기
# 이미지이기 때문에 dtype을 np.uint8로 해야한다.
img_dst = np.zeros(dst_size, np.uint8)

###### cv2.imshow("Img dst", img_dst)
# 원본 이미지에 점 4개 찍으면 검은 화면에 표시됨.
# 마우스 클릭 이벤트 달아줌

# 원본 이미지에서, 마우스 클릭하면, 4개의 점을 가져오도록 마우스 클릭 이벤트를 처리해 준다.
points_img = get_four_points(img_src)

print(points_img)

print(points_img.shape)


# points_dst 에는, 우리가 마우스로 클릭한 4개의 점이 있고,
# 결과 이미지에 매칭할 점을 작성해 준다.

points_dst = np.array([0,0, dst_size[1],0, dst_size[1], dst_size[0], 0,dst_size[0]])

points_dst = points_dst.reshape(4,2)
# H행렬 가져올 수 있다.

H, status = cv2.findHomography(points_img, points_dst)

print(points_dst)
print(H)

img_dst = cv2.warpPerspective(img_src, H, (dst_size[1], dst_size[0]))


cv2.imshow("img dst", img_dst)


cv2.waitKey(0)
cv2.destroyAllWindows()