import requests
import time
import string
import fileinput
import webbrowser
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from fake_useragent import UserAgent
import os
import chromedriver_autoinstaller as AutoChrome
import shutil

match_list = list()
url_list = list()

def urm(cur_url, searching_keyword):
    i = 0
    re = True
    print('\n', cur_url, '\n\n\n변환 중..')
    
    spacemode()
    req = urllib.request.Request(cur_url, headers={ # 자동 접속 방지 우회
                                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}) # 자동 접속 방지 우회
    
    response = urllib.request.urlopen(req).read()
    f = open('C:/Users/Kor_SW_Developer/Desktop/꿀팁/개인 프로젝트 관련 텍스트/testing_txt.txt',
             'a', -1, 'utf-8', 'w') # testing_txt에 작성 추후 f포메팅으로 키워드 명에 맞는 제목을 텍스트 파일 명으로 지정 할 생각 - 미완 / 작업 예정
    f.write(searching_keyword + "\n\n") # 키워드 명을 testing_txt에 작성
    
    tag_name = "a" # a태그에 href가 담겨 있어 검색 대상으로 지정
    bs_obj = BeautifulSoup(response, 'html.parser') # 현재 url 파싱
    urltag = bs_obj.findAll(tag_name) # 파싱한 것들 중 a태그 찾기
    
    print(urltag)  
    # urltag가 실질적으로 분할이 안되서 그런것 (2021.07.17)
    # 형변화 작업을 해주어야함 list_to_string이라는 함수로 형변환 해주어 주겠음
    
    for z in range(i, len(urltag)):
        list_to_string(urltag, i, match_list)
        i += 1
        #print(str(i)+"번째 시도 중.. \n\n")
    
    # 핵심 문제 해결 후 건들여볼 라인들
    """
	word1 = "href"
	word = "http"
	for word1 in match_list: #2021.05.11 여기가 안돌아감. 수정 할 방안 찾아서 코드 수정해야함 ㅇㅋ?? 여기부터 해결해라!!! 2021.05.22 가능성 1 :  match_list 속에 아무것도 없어서 그런듯 (정답) 방법 : 파일 불러와서 다시 분할 아니면 분할 조건을 더 세밀하게 설정
		if word1 in urltag: #조건 통과 X (if 문 이상 : 아마 배열이 제대로 안넘어가서 그런 듯(이따 서칭 필요))2021.07.03
			if word in urltag:
				match_list.append(word)
				print("current value :",match_list)
				list_to_string(match_list, word) #word1 이나 word 여도 스플릿 되는 건 똑같아서 추가적으로 스플릿이 더 필요하다는 추측 (방법 urltag 갱신 필요성 있음) 2021-07-31
				find_word_in_list(match_list, word) #통과 X // 원인:
				f.write()
	#테스팅
	f.close()
	"""
    '''
	text = response.decode('utf-8')
	f = open('C:/Users/Kor_SW_Developer/Desktop/꿀팁/개인 프로젝트 관련 텍스트/url_code.txt', 'a', -1, 'utf-8', 'w' )
	f.write(text)
	f.close()
	'''
    #  ===================================

'''
def counting_num(i):
    num = i + 1S
    return num
'''


def textsplit(file_location):  # out of range 에러 방지용으로 배열 크기 계산하는 시스템도 만들어야함
    i = 0
    re = 1
    f = open(file_location, 'r', -1, 'utf-8')
    list_file = f.read().split(' ')
    print('텍스트 분할 중..\n\n')
    while(re):
        if list_file[i].find('http') == -1 or list_file[i].find('href') == -1:
            i += 1
        else:
            print(list_file[i])  # 여기서 "인것을 삭제 해주어야함
            i += 1
    f.close()


def spacemode():
    for i in range(0, 2):
        print()
    for j in range(0, 2):
        print('=================================================================================================================')
    for i in range(0, 2):
        print()


def list_to_string(list_data, i, match_list): # 텍스트 작성 시 리스트 형태는 입력이 되지 않아 str로 변환 해주는 작업을 수행
    
    text = str(list_data)
    #print(str(i)+"번째 \n"+ text + "\n\n")
    # 수정 해야함 : 배열을 추가하는 방식을 채택할 예정!! => index out of range 해결을 위한 것 => append 사용 2021.05.22//20.03
    match_list.append(text)
    
    f = open('C:/Users/Kor_SW_Developer/Desktop/꿀팁/개인 프로젝트 관련 텍스트/testing_txt.txt',
             'a', -1, 'utf-8', 'w')
    f.write(text+"\n\n")
    # 최신 업데이트 2021-04-29 => (29 line solution) 여기에 match_list의 값을 맞추어줌. ? 근데 어떻게 match list 포함 시킴??? 전역 변수 써야하나????
    f.write("\n\n")
    
    #테스트
    #===================================================
    word1 = "href"
    word = "http"
    print("\n\n",str(i)+"번째 match list의 값 :",match_list[i-1],"\n\n")
    
    if word1 in match_list[i-1] and word in list_data[i-1]: #2021.05.11 여기가 안돌아감. 수정 할 방안 찾아서 코드 수정해야함 ㅇㅋ?? 여기부터 해결해라!!! 2021.05.22 가능성 1 :  match_list 속에 아무것도 없어서 그런듯 (정답) 방법 : 파일 불러와서 다시 분할 아니면 분할 조건을 더 세밀하게 설정
	    url_list.append(match_list[i-1]);print("\n\n current value :", url_list)
        
           
    #====================================================

'''
array_size = len(urltag)
print("현재 배열의 길이는 : ",array_size,"\n")
string_data = str(' '.join(urltag[i]))
return string_data
'''


def find_word_in_list(list_data, i):
    result_list = list()
    for_split = "\""  # "로 분리 할 것
    print(for_split)
    result_list = list_data.split(for_split)
    text = str(result_list)
    f = open('C:/Users/Kor_SW_Developer/Desktop/꿀팁/개인 프로젝트 관련 텍스트/url_code.txt',
             'a', -1, 'utf-8', 'w')
    f.write(text)


"""
def urltag_update(urltag,keywords):
	urltag = urltag.split(keywords)
"""



"""
문제점 : 텍스트 저장용 메모장 중 url_code에는 저장 되지 않음 => 아직 미구현임.
        testing~~~에는 같은 것만 저장되는 현상이 생김 => 아마 배열로 하는 것이 잘 진행이 되지 않아서 발생하는 문제라고 생각이 됨.


"""