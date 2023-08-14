import cv2

src = cv2.imread("C:/AboutProgramming/programming_folder/PYTHON/py_opencv/learning sample/using_sample/glass.jpg", cv2.IMREAD_COLOR) # 이미지를 불러옴
dst = cv2.flip(src, 1) # 이미지를 반전 시킴 cv2.flip(src, flipCode) == 대칭 적용 || src == 원본 이미지, flipCode == 대칭 축
"""
lipCode < 0은 XY 축 대칭(상하좌우 대칭)을 적용합니다.

flipCode = 0은 X 축 대칭(상하 대칭)을 적용합니다.

flipCode > 0은 Y 축 대칭(좌우 대칭)을 적용합니다.
"""

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()