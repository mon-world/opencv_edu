
'''
웹캠으로 이미지 받기

1. logo.png 파일을 읽어오기
2. 위 파일을 (100, 100) 으로 리사이징 하기
3. 그레이 스케일로 바꾸기
4. 쓰레숄드 이용해서, 로고를 마스킹 하기
5. 웹캠을 640,480 사이즈로 설정해서 켜고
6. 웹캠 이미지에서, 오른쪽 아래에 로고를 표시할 Region of Interest 를 셋팅합니다.
7. 로고와 웹캠 이미지를 합칩니다.
'''

import cv2
import numpy as np

logo_image = cv2.imread('data/images/logo.png')

# scaleX = 100 / logo_image.shape[1]
# scaleY = 100 / logo_image.shape[0]
# logo_resize = cv2.resize(logo_image, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR )
logo = cv2.resize(logo_image, (100,100))

# cv2.imshow('0', logo_image)
# cv2.imshow('1',logo_resize)

gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)


## 1보다 작은건 0, 아니면 255
_, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

cv2.imshow("gray",gray)
cv2.imshow("mask",mask)

## python opencv videocapture width 검색 ㄱㄱ
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True :
    ret, frame = cap.read()

    frame = cv2.resize(frame, (640,480))
    frame = cv2.flip(frame, 1) # 카메라가 좌우 반전이기 때문에 다시 반전시켜준다. 거울비슷하게

    roi = frame[-100-10 : -10 , -100-10 : -10]
    roi[np.where(mask)] = 0 # x,y의 컨디션을 가져온다. 마스크 부분 빼고는 0으로 채워라.

    roi = roi + logo

    # Here we show the image in a window
    cv2.imshow('Webcam', frame) 

    # Check if q was pressed
    # 탈출 조건
    if cv2.waitKey(1) == ord('q') : ## 키보드의 q버튼 이면
        break





cv2.waitKey(0)
cv2.destroyAllWindows()