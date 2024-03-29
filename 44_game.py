import cv2
import numpy as np
from collections import deque

class BackgroundXxtractioon :
    def __init__(self, width, height, scale, maxlen = 10) :
        self.maxlen = maxlen
        self.scale = scale
        self.width = width // scale
        self.height = height // scale
        self.buffer = deque(maxlen=maxlen)
        self.background = None
    
    def calculate_background(self):
        self.background = np.zeros((self.height, self.width), dtype='float32')
        for item in self.buffer:
            self.background += item
        self.background /= len(self.buffer)

    # 업데이트 하는 코드
    def update_background(self, old_frame, new_frame):
        self.background -= old_frame/self.maxlen
        self.background += new_frame/self.maxlen
    # 올드 프레임과 뉴 프레임을 가지고 올드는 -, 새로운 프레임은 +
    
    # 게임 화면 갱신하는 코드
    def update_frame(self, frame):
        if len(self.buffer) < self.maxlen:
            self.buffer.append(frame)
            self.calculate_background()
        else:
            old_frame = self.buffer.popleft()
            self.buffer.append(frame)
            self.update_background(old_frame, frame)

    def get_background(self) :
        return self.background.astype('uint8')

    def apply(self, frame) :
        down_scale = cv2.resize(frame, (self.width, self.height))
        gray = cv2.cvtColor(down_scale, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5,5), 0)

        self.update_frame(gray)
        abs_diff = cv2.absdiff(bg_buffer.get_background(), gray)
        # 백그라운드 가져와서 현재 그레이와 달라진거 비교

        _, ad_mask = cv2.threshold(abs_diff, 15, 255, cv2.THRESH_BINARY)
        
        return cv2.resize(ad_mask, (self.width*self.scale, self.height*self.scale))

   
def apply(self, frame) :
        down_scale = cv2.resize(frame, (self.width, self.height))
        gray = cv2.cvtColor(down_scale, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5,5), 0)

        self.update_frame(gray)
        abs_diff = cv2.absdiff(bg_buffer.get_background(), gray)
        _, ad_mask = cv2.threshold(abs_diff, 15, 255, cv2.THRESH_BINARY)
        return cv2.resize(ad_mask, (self.width*self.scale, self.height*self.scale))

class Game:
    def __init__(self, width, height, size=50):
        self.width = width
        self.height = height
        self.size = size
        self.logo = cv2.imread("data/images/logo.png")
        self.logo = cv2.resize(self.logo, (self.size, self.size))
        gray = cv2.cvtColor(self.logo, cv2.COLOR_BGR2GRAY)
        self.mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)[1]
        self.x = np.random.randint(0, self.width - self.size)
        self.y = 0
        self.speed = 10
        self.score = 0

    def update_frame(self, frame):
        roi = frame[self.y:self.y + self.size, self.x:self.x + self.size]
        roi[np.where(self.mask)] = 0
        roi += self.logo
 
    def update_position(self, fg_mask):
        self.y += self.speed
        if self.y + self.size >= self.height:
            self.score += 1
            self.y = 0
            self.speed = np.random.randint(10, 15)
            self.x = np.random.randint(0, self.width - self.size)
 
        roi = fg_mask[self.y:self.y + self.size, self.x:self.x + self.size]
        check = np.any(roi[np.where(self.mask)])
        if check:
            self.score -= 1
            self.y = 0
            self.speed = np.random.randint(10, 20)
            self.x = np.random.randint(0, self.width - self.size)
        return check

width = 640
height = 480
scale = 2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

bg_buffer = BackgroundXxtractioon(width, height, scale, maxlen=5)
game = Game(width, height)

while True :
    _, farme = cap.read()
    frame = cv2.resize(frame, (width, height))
    frame = cv2.flip(frame,1)

    fg_mask = bg_buffer.apply(frame)

    hit = game.update_position(fg_mask)
    game.update_frame(frame)

    if hit :
        frame[ : , : , 2 ] = 255 # bgr 즉 빨간색으로 표시하라

    text = "Score : {game.score}" # 문자열 포메팅 함. 변수가 안에 들어간당 루프 돌면서 찍어줌
    cv2.putText(frame, text, (10,20), cv2.FONT_HERSHEY_PLAIN, 2.0 , (0,255,0))
    # 1.이미지 2.점수 붙힐거 3.붙힐 위치 4.폰트 5.글씨 크기 6.글씨 색

    cv2.imshow("FG Mask", fg_mask)

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break