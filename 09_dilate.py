'''
이미지 형태학적 변환 : 늘리기
'''
import cv2

imageName = 'data/images/truth.png'

# 원본 읽어오기
image = cv2.imread(imageName, cv2.IMREAD_COLOR)
cv2.imshow("original", image)

# 이미지 확장 - dilation

dilationSize = 6

# 사각형으로 영역 확장
element = cv2.getStructuringElement(cv2.MORPH_RECT, (2*dilationSize+1,2*dilationSize+1 ))
# 1.쉐입 2.확장 크기 (13,13)

imageDilate = cv2.dilate(image, element)
# 13행 13열짜리 커널(사각형)을 만들어서 경계를 딜레이트 한다.

cv2.imshow("Dilation",imageDilate)




cv2.waitKey(0)
cv2.destroyAllWindows()