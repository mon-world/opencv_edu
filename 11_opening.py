import cv2

imageName = "data/images/opening.png"

image = cv2.imread(imageName, 1)

cv2.imshow("original", image)

openingSize = 3

element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*openingSize+1,2*openingSize+1))

# 1.이미지(np) 2.오퍼레이션 
imageOpened = cv2.morphologyEx(image, cv2.MORPH_OPEN, element, iterations=5 )

cv2.imshow('opened', imageOpened)

cv2.waitKey(0)
cv2.destroyAllWindows()