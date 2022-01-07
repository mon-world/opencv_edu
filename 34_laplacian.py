import cv2
import numpy as np

img = cv2.imread('data/images/truth.png',1 )


laplacian = cv2.Laplacian(img, cv2.CV_32F, ksize = 3, scale = 1)

## 1.이미지 2.?? 3.커널 사이즈 4.스케일? 보통 1 쓴대

cv2.imshow('lap',laplacian)







cv2.waitKey(0)
cv2.destroyAllWindows()