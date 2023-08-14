
# ===================================================================
'''
셀레니움 버전 4 전용 

셀레니움 업데이트 버전 변경 사항
https://kibua20.tistory.com/228

정리 목록
https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/#import

영상 참고
https://www.youtube.com/watch?v=LoPvjfABlBA
'''
# ===================================================================

import time

import urltxtmaker

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

#크롬드라이버 설정 
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager



#자동 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

# 불필요 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 사용할 변수 초기화 
searching_keyword = ""
website_address = ""
bs_html = ""
html = ""
# path = "C:/Users/Kor_SW_Developer/Documents/AboutProgramming/programming_folder/PYTHON/personal_project/auto_attend/chromedriver.exe"
re = 1
# 텍스트 파일 초기화 과정
remo_txt_data1 = open(
    'C:/Users/Kor_SW_Developer/Desktop/꿀팁/개인 프로젝트 관련 텍스트/testing_txt.txt', 'w')
remo_txt_data2 = open(
    'C:/Users/Kor_SW_Developer/Desktop/꿀팁/개인 프로젝트 관련 텍스트/url_code.txt', 'w')
remo_txt_data1.close()
remo_txt_data2.close()
while(re):
    driver.get('https://www.google.com') # 주소 이동
    
    searching_keyword = input("검색 키워드 입력...   ")
    searching_mode = driver.find_element(By.NAME, 'q') # 이런 식으로 서칭 해야 적용됨 (버전 : 셀레니움 4)
    searching_mode.click() # 이런 식으로 서칭 해야 적용됨 (버전 : 셀레니움 4)
    searching_mode.send_keys(searching_keyword + Keys.ENTER) # 이런 식으로 서칭 해야 적용됨 (버전 : 셀레니움 4)
    
    urltxtmaker.spacemode() # CUI로 과정 구분
    cur_url = driver.current_url  # 검색 엔진을 통해 검색한 결과들의 현 url 가져옴
    html_text = urltxtmaker.urm(cur_url, searching_keyword) #url을 추출 할 전용 모듈 중 urm이라는 함수에 현재 주소, 검색 키워드를 넘김
    
    urltxtmaker.spacemode()
    print("html 추출 중..!")
    
    urltxtmaker.spacemode()
    print("url 추출 중..!\n")
    
    urltxtmaker.spacemode()
    # 여기서 html_text에 포함되어 있는 태그를 이용하여 연관 내용이 포함된 url 불러올 것
    print("작업 끝\n\n")
    
    re = int(input("게속 진행 할 것이면 1  아니면 0을 눌러주시오 : ")) # 여기 부턴 프로그램 재실행 및 종료 관련 부분
    if re == 0:
        time.sleep(2)
    elif re == 1:
        time.sleep(2)
        driver.quit()
    else:
        while (re != 1 and re != 0):
            re = int(input("다시 입력 : "))
            if re == 1:
                time.sleep(2)
                driver.quit()
driver.quit()
