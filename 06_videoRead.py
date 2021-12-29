
import cv2
import numpy as np

cap = cv2.VideoCapture('data/videos/chaplin.mp4')
## 비디오 파일 가져오는 클래스

if cap.isOpened() == False:
    print('Error opening video stream or file')

else :

    # 비디오는 여러장의 사진으로 구성되어 있으므로!
    # 반복문을 통해서, 여러 사진을 한 장씩 처리해야 한다.

    # isOpened : 비디오 실행중
    while cap.isOpened() :

        # 사진 1장씩 가져온다.
        # ret는 ture or false 값을 주고 사진을 저장

        ret, frame = cap.read()

        # ret : 사진을 제대로 가져왔는지의 정보가 ture or false로 들어왔다.
        # 따라서 ret가 ture이면, 우리는 화면에 사진-np( frame )을 표시하면 된다.
        if ret == True:

            cv2.imshow("Frame",frame)

            # 키보드에서 esc키를 누르면 exit 하라는 코드작성.
            # 이 코드가 필요한 이유 : 비디오 실행 중간에 끄고 싶을 때.
            # 27=ESC
            if cv2.waitKey(25) & 0xFF == 27 :
                break

        else :  # ret가 ture가 아니면 사진이 다 끝났다는 것.
                # 동영상 제생이 끝난 경우 or 동영상 사진에 이상이 있는 경우
            break 

    cap.release()

    cv2.destroyAllWindows()