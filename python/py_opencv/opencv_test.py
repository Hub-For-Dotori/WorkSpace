import numpy as np
import matplotlib
import cv2

path = 'C:/Users/dotor/OneDrive/문서/AboutProgramming/programming_folder/PYTHON/py_opencv'
file_name = 'testing.jpg'


def showImage(path,file_name):
    full_path = path+'/'+file_name    
    img_array = np.fromfile(full_path, np.uint8)
    print("이미지 배열 : ",img_array)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    
    print("\n 이미지 : ")
    print(img)

    cv2.imshow('model',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

showImage(path,file_name)

# 경로 한글 이슈 발생시 참고 사항 https://bskyvision.com/entry/python-cv2imread-%ED%95%9C%EA%B8%80-%ED%8C%8C%EC%9D%BC-%EA%B2%BD%EB%A1%9C-%EC%9D%B8%EC%8B%9D%EC%9D%84-%EB%AA%BB%ED%95%98%EB%8A%94-%EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95
# OpenCV 사용법 https://076923.github.io/posts/Python-opencv-1/ || https://blog.naver.com/samsjang/220499281999
# OpenCV 함수 정리 https://deep-learning-study.tistory.com/99 || https://bskyvision.com/entry/pythonopencv-opencv-python-%ED%8C%A8%ED%82%A4%EC%A7%80-%EC%9C%A0%EC%9A%A9%ED%95%9C-%ED%95%A8%EC%88%98%EB%93%A4-%EC%A0%95%EB%A6%AC