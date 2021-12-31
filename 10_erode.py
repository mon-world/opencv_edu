
'''
이미지 형태학적 변환 : 침식
'''
import cv2

imageName = "data/images/truth.png"

image = cv2.imread(imageName, 1)

cv2.imshow("original", image)

# 이미지 경계 축소(침식)

dilationSize = 6

element = cv2.getStructuringElement(cv2.MORPH_RECT, (2*dilationSize+1,2*dilationSize+1) )
## 1.사각형. 2.커널사이즈

imageEroded = cv2.erode(image,element)

cv2.imshow("Erosion", imageEroded)

cv2.waitKey(0)
cv2.destroyAllWindows()