import cv2

image = cv2.imread("C:/AboutProgramming/programming_folder/PYTHON/py_opencv/learning sample/using_sample/lunar.jpg", cv2.IMREAD_REDUCED_GRAYSCALE_2)
image.shape
# 절대 경로로 이미지를 불러오고 \인 디렉터리 구분을 /로 유니코드 에러를 해결하고 flags 속성을 정하여 불러옴.
'''
flags 세부 속성
cv2.IMREAD_UNCHANGED : 원본 사용
cv2.IMREAD_GRAYSCALE : 1 채널, 그레이스케일 적용
cv2.IMREAD_COLOR : 3 채널, BGR 이미지 사용
cv2.IMREAD_ANYDEPTH : 이미지에 따라 정밀도를 16/32비트 또는 8비트로 사용
cv2.IMREAD_ANYCOLOR : 가능한 3 채널, 색상 이미지로 사용
cv2.IMREAD_REDUCED_GRAYSCALE_2 : 1 채널, 1/2 크기, 그레이스케일 적용
cv2.IMREAD_REDUCED_GRAYSCALE_4 : 1 채널, 1/4 크기, 그레이스케일 적용
cv2.IMREAD_REDUCED_GRAYSCALE_8 : 1 채널, 1/8 크기, 그레이스케일 적용
cv2.IMREAD_REDUCED_COLOR_2 : 3 채널, 1/2 크기, BGR 이미지 사용
cv2.IMREAD_REDUCED_COLOR_4 : 3 채널, 1/4 크기, BGR 이미지 사용
cv2.IMREAD_REDUCED_COLOR_8 : 3 채널, 1/8 크기, BGR 이미지 사용
'''
cv2.imshow("Moon",image)
cv2.waitKey()
cv2.destroyAllWindows