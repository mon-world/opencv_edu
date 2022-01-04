'''
lookupTable을 만들어 이미지의 밝기를 조절할 수 있다.
cv2.LUT()에 lookupTable과 이미지를 넣어서, lookupTable값으로 이미지를 변경해준다.
'''

import cv2
import numpy as np
from numpy.core.numeric import full

img = cv2.imread('data/images/candle.jpg',1 )


gamma = 1.5

# 이미지는 0부터 255까지 이므로, 이 이미지 범위에 해당하는 모든 숫자를 가져온다.
fullRange = np.arange(0, 255+1) ## 0~255로 숫자 표시

print(fullRange)

# 감마 보정을 통해서, 원래의 0~255 까지의 숫자를 => 보정한 숫자로 변경한다.
# fullRange^gamma : 감마 커렉션
# np.power(a,b) = a^b
lookupTable =  255 * np.power((fullRange / 255.0), gamma)

# 감마보정을 통해서 나온 연산 결과는, float 이므로, uint8로 다시 변경해줘야 한다.
lookupTable = np.uint8(lookupTable)

# 즉, 0~255를, 감마보정을 통해 매칭된 숫자를 얻어온다.
print(lookupTable) 

# 이를, cv2.LUT함수를 통해서, 원본 이미지를, 내가 원하는 룩업테이블의 값으로 매칭하여,
# 변경해 준 이미지로 얻어온다.
output = cv2.LUT(img,lookupTable ) # img를 lookupTable에 적용한다.
# 0~255가 매칭된 룩업테이블 가지고 매칭 시켜서 변환시켜준다. 
# 1은 0으로, 244는 그 자리 수인 253으로...


combined = np.vstack([img, output])

cv2.imshow("combined",combined)






cv2.waitKey(0)
cv2.destroyAllWindows()