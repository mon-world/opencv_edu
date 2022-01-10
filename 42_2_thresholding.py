# 모션 디텍션 예제 2/7

import cv2

cap = cv2.VideoCapture(0) # 비디오 캡쳐 가져오기
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

for _ in range(10) :
    _ , frame = cap.read()

frame = cv2.resize(frame, (640,480))
frame = cv2.flip(frame,1)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

background = gray # 그레이 저장

cv2.imshow("Background", background)

while True :
    _, frame = cap.read() # 프레임 하나씩 가져옴
    frame = cv2.resize(frame, (640,480))
    frame = cv2.flip(frame,1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    foreground = gray - background

    # 마스킹 하기 위한 쓰레숄드 작업 : 분리.
    _, mask = cv2.threshold(foreground, 127, 255, cv2.THRESH_BINARY) # 127 아래 0, 127 위 255

    cv2.imshow("Foreground", foreground)
    cv2.imshow('Mask', mask) # 마스크도 같이 표시한다.

    if cv2.waitKey(1) == ord('q'):
        break