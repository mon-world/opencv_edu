import cv2
import numpy as np

img = cv2.imread('data/images/mountain.jpeg',1 )

cv2.imshow('ori', img)

sharpen = np.array([0, -1, 0, -1, 5, -1, 0, -1, 0], dtype='int') 
# 샤픈이란? 이미지 인텐서티가 높았다 낮았다 혹은 반대의 경우를 더 크게 만듦.
sharpen = sharpen.reshape(3,3)

print(sharpen)

result = cv2.filter2D(img, -1, sharpen)

cv2.imshow('sharp',result)



cv2.waitKey(0)
cv2.destroyAllWindows()