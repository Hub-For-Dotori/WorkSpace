import cv2

src = cv2.imread("C:/AboutProgramming/programming_folder/PYTHON/py_opencv/learning sample/using_sample/fruits.jpg", cv2.IMREAD_COLOR)
height, width, channel = src.shape

dst = cv2.pyrUp(src, dstsize=(width * 2, height * 2), borderType=cv2.BORDER_DEFAULT) # 이미지 확대 함수 인자로는 src, dstsize=(width * 배율, height * 배율), borderType=cv2.BORDER_DEFAULT
dst2 = cv2.pyrDown(src) # 둘다 외삼법을 이용한 축소 확대임

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()