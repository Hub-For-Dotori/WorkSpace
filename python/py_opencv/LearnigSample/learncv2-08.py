import cv2

src = cv2.imread("C:/AboutProgramming/programming_folder/PYTHON/py_opencv/learning sample/using_sample/champagne.jpg", cv2.IMREAD_COLOR)

dst = cv2.resize(src, dsize=(1600,1200), interpolation=cv2.INTER_AREA)
dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR) # 이미지 크기 변경 함수 src : 입력 이미지, dstSize : 절대 크기, 상대크기(fx, fy), interpolation : 보간법, dst : 출력 이미지
"""
interpolation 속성

    cv2.INTER_NEAREST	이웃 보간법
    cv2.INTER_LINEAR	쌍 선형 보간법
    cv2.INTER_LINEAR_EXACT	비트 쌍 선형 보간법
    cv2.INTER_CUBIC	바이큐빅 보간법
    cv2.INTER_AREA	영역 보간법
    cv2.INTER_LANCZOS4	Lanczos 보간법
"""
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()