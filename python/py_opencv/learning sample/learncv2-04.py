import cv2

capture = cv2.VideoCapture("Image/Star.mp4") # 동영상 파일에서 정보를 읽어옴.

while cv2.waitKey(33) < 0:
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT): 
        # cv2.CAP_PROP_POS_FRAMES == 동영상의 현재 프레임 수
        # cv2.CAP_PROP_FRAME_COUNT == 동영상의 총 프레임 수
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0) # 현재 프레임을 마지막 프레임으로 설정함. 
        #위에서 재생을 진행하고 있으므로 종료에 다가가기 위해 카운트 개념으로 
        # 매 진행 프레임을 마지막 프레임으로 설정해주는 것임. 

    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

capture.release()
cv2.destroyAllWindows()

# VideoCapture 메서드와 속성은 다음 페이지에서 참고
# https://076923.github.io/posts/Python-opencv-4/#%EC%B6%9C%EB%A0%A5-%EA%B2%B0%EA%B3%BC