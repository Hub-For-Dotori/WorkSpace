import cv2
import mediapipe as mp # 손가락 인식을 위한 패키지 임포트

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

volume = 0        
OnOff = False # 소리 조절 고정 모드


cap = cv2.VideoCapture(0) # 카메라 설정


def volumeMaxMinCheck(volume):
    if volume >= 100:
        volume = 100
    if volume <= 0:
        volume = 0 
    return volume
    
def volumeFixONOFF(ring_diff):
    if ring_diff > 50:
        mode = True
    if ring_diff <= 50:
        mode = False   
    return mode
        


with mp_hands.Hands(
    max_num_hands=1, # 최대 손 인식 개수
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        success, image = cap.read() # 카메라 인식
        if not success:
            continue

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            
            for hand_landmarks in results.multi_hand_landmarks:
                
                thumb = hand_landmarks.landmark[4] # 엄지
                index = hand_landmarks.landmark[8] # 검지
                
                ring_tip = hand_landmarks.landmark[16] # 약지 끝
                ring_mcp = hand_landmarks.landmark[13] # 약지 시작
                    
                ring_diff = abs(ring_tip.y - ring_mcp.y)
                    
                ring_diff = int(ring_diff * 220)
                OnOff = volumeFixONOFF(ring_diff)
                
                if OnOff == False: # 약지 접힘 : 볼륨 조절 // 약지 펴짐 : 볼륨 고정

                    diff = abs(index.y - thumb.y) # 검지와 엄지의 y좌표 차이를 통해 값을 지정함

                    volume = int(diff * 220) # 이때의 diff 값은 실수이므로 정수형으로 만들어주어야함. 추가적으로 거리에 따라서 계산 값이 달라지므로 개선은 필요할 듯.
                    volume = volumeMaxMinCheck(volume) # 최댓값 최솟값 체크
                
                cv2.putText(
                    image, text='testing..', org=(10, 30),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                    color=255, thickness=2)
                cv2.putText(
                    image, text='Volume: %d' % volume, org=(10, 60),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                    color=255, thickness=2) # volume 값 텍스트 인디케이터
                cv2.putText(
                    image, text='mode: %d' % OnOff, org=(10, 90),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                    color=255, thickness=2) # volume 값 텍스트 인디케이터

                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS) # 손에 있는 랜드마크를 그리기 위한 코드
                    
        cv2.imshow('image', image) # 카메라 화면 출력
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()

    print("끝")
    print("code uploading test..")

    