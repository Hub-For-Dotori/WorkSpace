import pyautogui
import pyperclip
import time

print(pyautogui.size()) #스크린 사이즈 출력
i = 50 
pyautogui.moveTo(i,i) # 커서 움직이기

time.sleep(0.5)
print(pyautogui.position())
pyautogui.moveTo(300,500)    
pyautogui.click(button='left') # 왼쪽 클릭하기
pyautogui.dragTo(0,500,button="left") # 드래그 하기 클릭 이후 사용 / x,y,button

pyperclip.copy("#안녕하세요") # 클립보드에 텍스트를 복사합니다. 

#맥은 핫키 명령어가 안먹어서 다음과 같이 작성함.
pyautogui.keyDown('command')
pyautogui.press('v')
pyautogui.keyUp('command')

a = pyautogui.alert(text='나가려면 아래 버튼 클릭', title='경고', button='확인')
print(a)
#안녕하세요
#안녕하세요
