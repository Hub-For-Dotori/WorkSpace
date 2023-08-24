import cv2

src = cv2.imread("C:/AboutProgramming/programming_folder/PYTHON/py_opencv/learning sample/using_sample/ara.jpg",cv2.IMREAD_COLOR)

height, width, channel = src.shape # 이미지의 높이 너비 채널 값 저장 (회전 중심점을 위해 높이와 너비를 알아야함.)
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1) # 인자 값은 center(튜플), angle, scale을 사용하여 matrix 생성
dst = cv2.warpAffine(src, matrix, (width, height)) #인자값은 src, matrix(아핀 맵 행렬), (width, height)가 있다.

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()