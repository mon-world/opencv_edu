# 노이즈 처리를 위해 가우시안 사용.

import cv2

cap = cv2.VideoCapture(0) # 비디오 캡쳐 가져오기
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

for _ in range(10) : # 10번 돌기
    _ , frame = cap.read() 

frame = cv2.resize(frame, (640,480))
frame = cv2.flip(frame,1)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# 노이즈 감소 사용
gray = cv2.GaussianBlur(gray, (25,25), 0)

background = gray ## 그레이로 한걸 저장함

# cv2.imshow("Background", background)

while True :
    _, frame = cap.read() # 프레임 하나씩 가져옴
    frame = cv2.resize(frame, (640,480))
    frame = cv2.flip(frame,1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (25,25), 0) 


    abs_diff = cv2.absdiff(gray, background)
    # gray와 background 차이를 가져와라 라는 뜻. 마스킹.

    # 마스킹을 위해 쓰레숄드 기법 사용
    _, ad_mask = cv2.threshold(abs_diff, 63, 255, cv2.THRESH_BINARY)


    cv2.imshow("Abs diff mask", ad_mask) 

    if cv2.waitKey(1) == ord('q'):
        break