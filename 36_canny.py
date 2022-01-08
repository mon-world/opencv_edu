import cv2
import numpy as np

img = cv2.imread('data/images/sample.jpg',0 ) # 엣지는 컬러에서 찾지 않는다.

cv2.imshow('gray', img)

threshold_max = 150
threshold_min = 50

result = cv2.Canny(img, threshold_max, threshold_min)
# max로 설정된 것과 이어진 것은 모두 살린다.
# min, max를 조절하면 원하는 대로 엣지 찾을 수 있다.
# 숫자를 그때마다 바꿔야 하기 때문에 비효율적.

cv2.imshow("Canny", result)



cv2.waitKey(0)
cv2.destroyAllWindows()