import cv2
import numpy as np

image = cv2.imread('data/images/mark.jpg')

cv2.imshow('img', image) ## 넘파이로 불러와보림 'img'는 넘파이로 인듯?

# 선 그리기

imageLine = image.copy()

cv2.line(imageLine, (322,179), (400,183), (20,20,210), 2, lineType=cv2.LINE_AA ) 
# 선 그리는 함수
# 1.이미지(np) 2.선의 시작점 3.끝점 4.BGR 선 칼라 5.선의 두께
# 6.라인 타입
cv2.imshow('image line', imageLine)


# 원 그리기
imageCircle = image.copy()

cv2.circle(imageCircle, (350,200), 150, (0, 0, 255), thickness=3, lineType=cv2.LINE_AA)
# 원 그리는 함수
# 1.이미지(np) 2.원 중심 3.반지름 4.칼라 5.선 두께
# cv2.line_AA는 선을 부드럽게 해준다.

cv2.imshow('image circle', imageCircle)


# 타원 그리기
imageEllipse = image.copy()

cv2.ellipse(imageEllipse, (360,200), (100,170), 45, 0, 360, (0, 0, 255), thickness=2)
# 1.이미지 2.중심 3.찌그러짐 4.시작 앵글 5.끝 앵글 6.칼라
cv2.ellipse(imageEllipse, (360,200), (100,170), 135, 0, 360, (0, 255, 0), thickness=2)
# 이미지가 같으면 같은 이미지에 타원 하나 더 그리는 코드.

cv2.imshow('ellipse',imageEllipse)


# 사각형 그리기
imageRectangle = image.copy()

cv2.rectangle(imageRectangle, (208, 55), (450, 355),(255,0,0),thickness=3)
# 1.이미지 2.시작점 3.반대점 => 왼쪽위~오른쪽아래 같은 식

cv2.imshow('rec',imageRectangle)


# 글자 넣기
imageText = image.copy()
cv2.putText(imageText,"Mark Zuckerberg", (205, 50), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0), thickness=2)
# 1.이미지 2.쓸 글자, 3.글자 시작점 4.폰트 5.폰트 스케일 6.두께

cv2.imshow("test", imageText)


# 마크 주커버그 얼굴에 사각형을 그리고 그 위에 Mark Zuckerberg 라고 글자를 넣기.
image1 = image.copy()
cv2.putText(image1,"Mark Zuckerberg", (205, 50), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0), thickness=2)
cv2.rectangle(image1, (208, 55), (450, 355),(255,0,0),thickness=3)
cv2.imshow("image1",image1)




cv2.waitKey(0)
cv2.destroyAllWindows()