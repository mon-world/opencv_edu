'''
움직임이 있다면, 그 차이를 찾아낸다.
'''

# 방금 전까진 백그라운드와 디프였고
# 지금은 움직이는 것과의 디프

import cv2

cap = cv2.VideoCapture(0) # 비디오 캡쳐 가져오기
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

for _ in range(10) : # 10번 돌기
    _ , frame = cap.read()

frame = cv2.resize(frame, (640,480))
frame = cv2.flip(frame,1)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# 노이즈 감소는 이 시점에 함
gray = cv2.GaussianBlur(gray, (25,25), 0) 

background = gray # 그레이로 한걸 저장함

last_frame = gray # 전 프레임과 지금의 차이를 판단. 이것이 모션 디텍션

# cv2.imshow("Background", background)

while True :
    _, frame = cap.read() # 프레임 하나씩 가져옴
    frame = cv2.resize(frame, (640,480))
    frame = cv2.flip(frame,1)

    # Processing!
    # F : Foreground
    # B : Background
    
    # 지금까지는 아래처럼 동작하도록 하였지만,
    # F[i] = abs(Frame[i] - B)

    # 우리가 하고자 하는 것은 아래처럼, 바로 전 프레임과, 현재 프레임의 차이를 얻어오는 것!!!
    # F[i] = abs(Frame[i-1] - Frame[i])
    ## last_frame이 계속 바뀌어줘야함.

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (25,25), 0) # 가우시안 블러


    abs_diff = cv2.absdiff(last_frame, gray)
    # last와 gray의 차이

    last_frame = gray # 루프 돌면 돌수록 계속 last_frame이 바뀐다. 전 gray를 받아오기 때문!



    # 마스킹을 위해 쓰레숄드 기법 사용
    _, ad_mask = cv2.threshold(abs_diff, 63, 255, cv2.THRESH_BINARY)


    cv2.imshow("Abs diff mask", ad_mask) ## ??? 찾아봐

    if cv2.waitKey(1) == ord('q'):
        break

# 다른 부분이 있으면 하얀색으로 나옴. 마스킹.
# 전 프레임과 비교해서 바뀐 부분을 찾아낸다.