'''
cv2.threshold
threshold 가 기준값이다.
'''


import cv2

# 0은 그레이스케일을 의미한다.
src = cv2.imread('data/images/threshold.png', 0)

cv2.imshow("Original", src)

# 이 값이 기준값이 되는 것
thresh = 100

# 이 값이, 위의 기준값보다 큰 것들을 전부 이 값으로 바꾸기 위해서 사용
maxValue = 255

# 두번째 리턴값인 dst가 쓰레숄드 적용된 이미지(np) 이다.
th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY)
# 1.이미지(np) 2.threshold 3.맥스벨류 4.타입(여기선 2개만 하므로 binary)
# 쓰레쉬 홀드는 거의 바이너리이다.


# dst를 화면에 표시한다.
cv2.imshow("Thresholded Image", dst)




cv2.waitKey(0)
cv2.destroyAllWindows()