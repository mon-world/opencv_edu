# 앞에서 했던 것을, cv2 에서 함수로 제공한다.

import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

back_sub = cv2.createBackgroundSubtractorMOG2()

while True :
    _, frame = cap.read()

    fg_mask = back_sub.apply(frame) # last프레임으로 들어감.
    # 현재와 1개 전의 차이를 봄

    cv2.imshow('Frame',frame)
    cv2.imshow('FG mask', fg_mask)
    
    if cv2.waitKey(1) == ord('q'):
        break

    # 플립을 안해서 반대 손을 든다. 가만히 있으면 움직임이 없다
    # 움직이는 부분이 흰색으로 하긴 하는데 되게 윤곽선 잘 잡는다.
    # 조금의 움직임도 잘 잡음.