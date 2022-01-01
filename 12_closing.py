import cv2

imageName = "data/images/closing.png"
# 아까는 까만색이었고 지금은 흰색

image = cv2.imread(imageName, 0)

cv2.imshow("original", image)

closingSize = 3

element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*closingSize+1,2*closingSize+1))
## 타원으로 한다. 그 다음은 행렬.


# 1.이미지(np) 2.오퍼레이션 
imageClosing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, element, iterations=5 )
# 1.이미지 2.클로징 3.타원(앞에 만듦) 4.반복횟수


cv2.imshow('closing', imageClosing)

cv2.waitKey(0)
cv2.destroyAllWindows()