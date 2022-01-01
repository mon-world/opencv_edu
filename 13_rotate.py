import cv2

source = cv2.imread('data/images/book1.jpg', 1)

print(source.shape)
## 회전하려면 중심 좌표 필요

cv2.imshow('original', source)

# 센터 좌표를 얻기!!
# 넘파이의 행렬인 행과 열의 정보로부터, 센터 좌표를 만들 때 주의점!!!
# 행렬을 좌표로 바꿀 때, 행열은 각각 행은 좌표의 y, 열읜 좌표의 x가 된다.
## 버그 발생 주의

centerY = source.shape[0] / 2
# 튜플의 첫번째 원소를 가져온다.

centerX = source.shape[1] / 2


rotationAngle = 300 # dgree 값
scaleFactor = 2 # 확대 축소

rotationMatrix = cv2.getRotationMatrix2D((centerX,centerY), rotationAngle, scaleFactor)
# 이거 이용하면 회전 할 수 있는 행렬을 가져다 줌.
# 1.센터 2.앵글 3.스케일

# 회전을 시킬 수 있는, 행렬을 우리한테 준다!!!!!!!

print(rotationMatrix)

result = cv2.warpAffine(source, rotationMatrix, (2*source.shape[1],2*source.shape[0]) )
# 1.원본 넘파이 어레이 2.로테이션 행렬 3.변환 후 이미지 사이즈 : 여기도 좌표로
# 행렬은 보통 대문자
# 여기도 이미지 사이즈도 좌표로 하기 때문에 주의하자

cv2.imshow('rotation img', result)

cv2.waitKey(0)
cv2.destroyAllWindows()