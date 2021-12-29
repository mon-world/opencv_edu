import cv2
import numpy as np

# 캠으로부터 데이터 가져오기, 0은, 해당 기기에 있는 첫번째 카메라 가져오라는 뜻.

cap = cv2.VideoCapture(0)

if cap.isOpened() == False :
    print('Unable to read camera feed')

else :
    # 프레임의 정보 가져오기 : 화면 크기 (width, height)

    # 좌표 정보는 항상 정수여야 한다.
    frame_width = int( cap.get(3) )
    frame_height = int( cap.get(4) )

    # 데이터의 프레임 정보를 저장. == 사진을 저장
    out = cv2.VideoWriter('data/videos/output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

    # 캠으로부터 사진을 계속 입력 받는다.
    # 이걸 out에 반복적으로 저장
    while True :
        ret, frame = cap.read()

        if ret == True :
            # 동영상으로 저장
            out.write(frame)
            # 화면에 표시
            cv2.imshow('frame', frame)

            # 키보드에서 esc키를 누르면 exit 하라는 코드작성.
            # 이 코드가 필요한 이유 : 캠 실행 중간에 끄고 싶을 때 사용한다.
            if cv2.waitKey(25) & 0xFF == 27 :
                break

        else :
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()