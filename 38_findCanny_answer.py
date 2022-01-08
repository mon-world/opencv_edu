import cv2
import numpy as np
import random

threshold = 0

maxThreshold = 255 * 3

random.seed(12345)

def callback():
    # 케니 에지로, 에지를 검출한다. 이때는 에지만 검출하기 때문에, 끊어진 선들도 많다.
    imCanny = cv2.Canny(img, threshold, threshold*2, apertureSize=3)


    # findContours  함수를 통해, 끊어진 에지들을 연결 시킨다.
    contours, heirarchy = cv2.findContours(imCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    print(contours)

    display = np.zeros( (imCanny.shape[0], imCanny.shape[1]) )

    for i in range(0, len(contours)) :
        lineColor = (255, 0, 0)
        cnt = contours[i]
        cv2.drawContours(display, [cnt], -1, lineColor, 2)
    
    cv2.imshow("Contours", display/255.0 )

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
