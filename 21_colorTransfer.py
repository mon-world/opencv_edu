'''
dst 이미지를 src의 색감으로 변환하기
LAB 사용
L : Luminosoty 명도
A : red / green의 보색축
B : yello / blue의 보색축
'''

import cv2
import numpy as np

src = cv2.imread('data/images/image1.jpg', 1)
dst = cv2.imread('data/images/image2.jpg', 1) # 데스티네이션 이미지

cv2.imshow('src',src)
cv2.imshow('dst', dst)

# 위 두 이미지의 컬러를 조합하여, 결과로 만들 이미지 생성
output = dst.copy()

## LAB는 장치 독립성과 균일성을 가진 색 표기이다.
srcLab = cv2.cvtColor(src, cv2.COLOR_BGR2LAB)
dstLab = cv2.cvtColor(dst, cv2.COLOR_BGR2LAB)
outputLab = cv2.cvtColor(output, cv2.COLOR_BGR2LAB)

# 연산을 위해서, float32로 변환
## 넘파이의 다른 방법
srcLab = srcLab.astype('float32') # np.float32(srcLab)
dstLab = dstLab.astype('float32') # np.float32(dstLab)
outputLab = outputLab.astype('float32')

print(srcLab)

# 채널 분리!
# 3개의 채널로 분리한다.
srcL, srcA, srcB = cv2.split(srcLab) 
dstL, dstA, dstB = cv2.split(dstLab)
outL, outA, outB = cv2.split(outputLab)


# dst의 값에서, dst의 평균을 뺀다.
outL = dstL - dstL.mean()
outA = dstA - dstA.mean() ## 밝기도 낮아지고 색도 변한다.
outB = dstB - dstB.mean()

# 이번엔 표준편차
outL = outL * ( srcL.std() / dstL.std() )
outA = outA * ( srcA.std() / dstA.std() )
outB = outB * ( srcB.std() / dstB.std() )

outL = outL + srcL.mean()
outA = outA + srcA.mean()
outB = outB + srcB.mean()


# 우리가 눈으로 보는 이미지는 음수도 없고, 255보다 큰 값도 있으면 안된다.
# 따라서 우리의 이미지는 0 ~ 255 까지의 값으로 되어 있어야 하므로
# np.clip 함수를 이용해서, 0보다 작은것은 0으로 만들고, 255보다 큰 것은 255로 만들어 준다.
outL = np.clip(outL, 0, 255)
outA = np.clip(outA, 0, 255)
outB = np.clip(outB, 0, 255)



# 다시 분리되어있는 채널을, 하나로 합쳐준다.
# 즉, 하나의 행렬로 만들어준다.
outputLab = cv2.merge([outL, outA, outB]) ## 합칠때는 리스트로 들어간다. 순서 중요.

print(outputLab.dtype) ## float32

# float32로 되어있고, 이미지는 uint8이기 때문에, uint8로 변환해줘야 한다.
outputLab = np.uint8(outputLab)

print(outputLab.dtype) ## uint8

# 화면에 표시하려고 하는데, 화면에 표시하는 함수는 cv2.imshow 이다.
# cv2.imshow는 BGR 컬러 스페이스를 화면에 표시하는 함수이므로,
# 우리는 현재 LAB로 되어있는 컬러 스페이스를, BGR로 먼저 바꿔줘야 한다.

outputLab = cv2.cvtColor(outputLab, cv2.COLOR_LAB2BGR)

cv2. imshow("output", outputLab)


cv2.waitKey(0) 
cv2.destroyAllWindows()