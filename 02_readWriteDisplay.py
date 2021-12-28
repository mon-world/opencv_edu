import cv2

imageName = 'data/images/sample.jpg'
# 동일한 레벨에 데이타란 폴더가 있다.
image = cv2.imread(imageName, cv2.IMREAD_COLOR)

if image is None : #이미지가 아무것도 없으면
    print('잘못된 이미지 입니다.') #에러처리임

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
# 칼라 읽어오기 # OPENCV 에서는 BGR로 나오는 것 유의

# 이미지를 표시하는 창(윈도우)에 이름과 성질을 설정
# namedWindow : 해당 창을 재활용해서 사용가능
#1. 창 이름 2. 창 성질(크기 등)

cv2.namedWindow("gray image", cv2.WINDOW_AUTOSIZE)

# 위에서 설정한 내용을 반영하기 위해서는 CV2.imshow() 사용
# imread와 imshow는 같이 다닌다.

cv2.imshow('gray image', grayImage)


# 작업한 넘파이 이미지를 파일로 저장하는 코드
# cv2.imwrite('gray_img.jpg', grayImage)

# 파일 경로와 파일 명 쓰기.
# grayImage는 넘파이. 넘파이를 jpg로 만듦.
# data의 images에 하려면?
cv2.imwrite('data/images/gray_img.jpg', grayImage)



cv2.waitKey(0)
cv2.destroyAllWindows() 