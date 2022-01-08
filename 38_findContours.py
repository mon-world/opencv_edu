## Contours : 둘레
import cv2
import numpy as np
import random

threshold = 0

maxThreshold = 255 * 3 # 트랙바 용

random.seed(12345) 

def callback() :
    # 케니 에지로, 에지를 검출한다. 이 때는 에지만 검출하기 때문에, 끊어진 선들도 많다.
    imCanny = cv2.Canny(img, threshold, threshold * 2, apertureSize=3)


    # findContours 함수를 통해, 끊어진 에지들을 연결 시킨다.
    contours, heirarchy = cv2.findContours(imCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    print(contours)

    # 연결
    display = np.zeros( (imCanny.shape[0], imCanny.shape[1]) )

    for i in range(0, len(contours)) : ## 연결시킨 후보군 뽑아옴. 컨튜어스 에서
        lineColor = (255, 0, 0)
        cnt = contours[i]
        cv2.drawContours(display, [cnt], -1, lineColor, 2)
        # 1.까만 배경에 선 그리겠다는 것, 3.컨튜어 인덱스 4.라인컬러는 정해준 것
        # 5.선 두께 


    cv2.imshow("Contours", display/255.0)

# 트랙바 함수
def updateThreshold(*args):
    global threshold
    threshold = args[0]
    callback()

img = cv2.imread('data/images/threshold.png', 0)

cv2.namedWindow("Contours", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Contours", img)

cv2.createTrackbar("Canny and Contours", "Contours", threshold, maxThreshold, updateThreshold)






cv2.waitKey(0)
cv2.destroyAllWindows()

