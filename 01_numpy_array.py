import cv2

imageName = 'data/images/sample.jpg'

# opencv 로 이미지 열기
# 파일을 칼라로 읽어와라
image = cv2.imread(imageName, cv2.IMREAD_COLOR) # 파일을 칼라로 읽어와라

if image is None : # 이미지 변수 안에 아무것도 없다면?
    print('이미지 파일을 열 수 없습니다.')


# print(image)
# print()
# print(image.shape)

# 그레이 스케일 이미지 : 1개의 행렬이고, 0~255 까지의 숫자로 채워짐. 실제 우리 눈으로 보면
# 말 그대로 회색으로 나온다.

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 칼라를 그레이로 바꿔라

print(image.shape)
# 우리 눈으로 직접 볼 수 있는 함수 cv2.imshow()

cv2.imshow("image", image) 
cv2.imshow("gray", grayImage)

# 위의 이미지를 화면에 표시하는 코드는, 실행되었다가 바로 종료된다.
# 왜냐하면, 파일 자체를 cpu가 위에서부터 한번에 끝내기 때문에,
# imshow()가 바로 종료가 된다.

# 따라서 프로그램이 종료되지 않도록 기다리는 함수인 아래 함수를 사용해서,
# 프로그램 종료를 지연시킨다.
cv2.waitKey(0)
cv2.destroyAllWindows()