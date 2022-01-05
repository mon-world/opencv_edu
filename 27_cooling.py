'''
이미지의 느낌을 푸른 느낌이 강하도록 변경.
블루 커브를 사용하고, 그 값에 맞게 대응시켜준다.
'''
import cv2
import numpy as np

original = cv2.imread('data/images/girl.jpg',1 )

img = original.copy()

originalValue = np.array([0, 50, 100, 150, 200, 255])
rCurve = np.array([0, 40, 80, 120, 180, 255])
bCurve = np.array([0, 60, 120, 180, 220, 255])

fullrange = np.arange(0, 255+1)

rLUT = np.interp(fullrange, originalValue, rCurve)
bLUT = np.interp(fullrange, originalValue, bCurve)

R = img[:,:,2]
B = img[:,:,0]

R = cv2.LUT(R, rLUT)
B = cv2.LUT(B, bLUT)

img[:,:,2] = R
img[:,:,0] = B

combined = np.vstack([original, img])
cv2.imshow("img",combined)





cv2.waitKey(0)
cv2.destroyAllWindows()