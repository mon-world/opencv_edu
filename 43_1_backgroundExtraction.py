# 백그라운드 처리하는 코드를, 클래스로 만들어 본다.

import cv2
import numpy as np

class BackgroundExtraction :
    def __init__(self, width, height, scale):
        self.last_frame = np.zeros( (height//scale, width//scale), np.uint8 )
        self.new_frame = None

    def update_frame(self, frame) :
        self.new_frame = frame

    def get_background(self) :
        background = self.last_frame
        self.last_frame = self.new_frame
        return background

width = 640
height = 480
scale = 2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

bg_buffer = BackgroundExtraction(width, height, scale)

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (width, height))
    frame = cv2.flip(frame, 1)

    down_scale = cv2.resize(frame, (width//scale, height//scale)) ## //는 몫 구하기.
    gray = cv2.cvtColor(down_scale, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)

    bg_buffer.update_frame(gray)

    abs_diff = cv2.absdiff(bg_buffer.get_background(), gray)

    _, ad_mask = cv2.threshold(abs_diff, 15, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(ad_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours :
        if cv2.contourArea(contour) < 250 :
            continue

        x,y,w,h = cv2.boundingRect(contour)
        x,y,w,h = x*scale, y*scale, w*scale, h*scale

        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break



