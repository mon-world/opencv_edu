from typing import Counter
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

for _ in range(10):
    _, frame = cap.read()
frame = cv2.resize(frame, (640, 480))
frame = cv2.flip(frame, 1) # 이걸로 해야 자연스러움. 좌우 반대.
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray, (25,25), 0)

background = gray

last_frame = gray 
# 사각형을 그리기 위해선 그 전 프레임을 알고 있어야 한다.


# cv2.imshow("Background", background)
# 지금 실행하면 10번 째 이미지 볼 수 있다. 움직이진 않음.


while True : # 무한 루프. 이걸로 계속 웹캠 실행시킴
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (25, 25), 0) # 움직임만 보니까 블러 대충처리 (25,25)

    
    abs_diff = cv2.absdiff(last_frame, gray)
    # 둘의 차이를 구하는 함수
    # 1.방금 전 촬영한 프레임, 2.현재 프레임

    last_frame = gray ##라스트 프레임을 바꿔줌. 왜? 다음 루프 돌 때 바뀌어야 하니까

    _, ad_mask = cv2.threshold(abs_diff, 15, 255, cv2.THRESH_BINARY)
    # 쓰레숄드는 마스킹 할 때 사용한다.
    # 쓰레숄드는 하이퍼 파라미터
    # 255는 정해져있음. 차이 있는건 하얀색으로 해야하기 때문
    # 차이 없으면 검은색 이란 뜻 : abs_diff가 차이
    # cv2.THRESH_BINARY : 영역 잡아줌


    contours, _ = cv2.findContours(ad_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 둘레를 가지고 온다.

    # print(contours) # 움직이면 움직이는 좌표가 나온다.

    for contour in contours :

        # 컨투어 영역 면저거을 원하는 대로 셋팅할 수 있다. 작게 설정하면, 움직인 영역이 작은 영역도
        # 사각형을 그린다.(<100)
        if cv2.contourArea(contour) < 1000:
        # 면적 구함. 사각형 면적 찾아줌 좌표 주면
            continue # 1000보다 작으면 다른거 찾아라
        
        x, y, w, h = cv2.boundingRect(Counter)
        # 이 영역에 맞는 4각형을 그려라.
        # 시작점(x,y), 시작점으로부터 얼만큼(w,h)
        
        cv2.rectangle(frame, (x,y), (x+w, y+h) , (30,20,210), 5)
        # 칼라 이미지는 gray가 아닌 frame에 있으므로 이걸 가져와야 한다.
        # 즉, frame에 좌표를 그려야 한다.
        # contour 지날때마다 화면에 표시

    cv2.imshow("webcam", frame) # 캠 + 사각형 + 움직임 표시됨. 왜? 다 프레임에 넣었으니까
    cv2.imshow("Abs Diff Mask", ad_mask)

    if cv2.waitKey(1) == ord('q') :
        break