import cv2

capture = cv2.VideoCapture(0) # 카메라 불러오기 (인덱스 번호 0 == 내장카메라)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1600) # 카메라 프레임 가로폭 설정  
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200) # 카메라 프레임 세로폭 설정
# (인자값은 propid와 value가 있는데 propid는 카메라 설정이며 value는 속성값이다.)

while cv2.waitKey(10)<0: # waitKey(delay) 키 입력이 있을 때까지 프로그램을 delay만큼 지연 시킴. ex) while cv2.waitKey(33) != ord('q') 식으로도 사용 가능  
    ret, frame = capture.read() # capture.read() == 카메라 상태, 프레임 불러옴 || ret == 카메라 상태 (활성 == True, 비활성 == False) || frame == 현재 시점 프레임 저장
    cv2.imshow("Video Frame",frame) # imshow(Winname,frame) == 이미지  || winname == 출력 이미지틀 이름, mat == 불러올 이미지를 말함.

capture.release() # 메모리 해제 매서드로 카메라 장치에서 받아온 메모리를 해체함.
cv2.destroyAllWindows() # 모든 윈도우 창 제거 함수로 카메라 창을 닫아버림. 특정 윈도우만 닫고 싶을 떈 winname의 명을 사용하여 특정 윈도우만 닫을 수 있음.