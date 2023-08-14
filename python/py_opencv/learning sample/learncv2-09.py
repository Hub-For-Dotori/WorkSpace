import cv2

src = cv2.imread("C:/AboutProgramming/programming_folder/PYTHON/py_opencv/learning sample/using_sample/chess.jpg", cv2.IMREAD_COLOR)
dst = src[100:600, 200:700].copy()
# OpenCv의 이미지는 numpy 배열 방식과 동일함. 
# 따라서 높이(행), 너비(열)을 특정 영역으로 배열을 특정 영역 나누듯 자르면 됨
#.copy를 진행하지 않으면 원본에도 영향이 생김

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()

src = cv2.imread("C:/AboutProgramming/programming_folder/PYTHON/py_opencv/learning sample/using_sample/chess.jpg", cv2.IMREAD_COLOR)
dst = src.copy() 
roi = src[100:600, 200:700]
dst[0:500, 0:500] = roi

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
# OpenCv의 이미지는 numpy 배열 방식과 동일함. 
# 따라서 높이(행), 너비(열)을 특정 영역으로 배열을 특정 영역 나누듯 자르면 됨

#https://076923.github.io/posts/Python-opencv-9/