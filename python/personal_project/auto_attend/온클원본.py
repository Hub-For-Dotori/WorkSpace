import requests, time, datetime
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from fake_useragent import UserAgent

def spacemode():
	for i in range (0,2):
		print()
	for j in range (0,2):	
		print('=================================================================================================================')
	for i in range (0,2):
		print()	
	return
#================================현 날짜=============================
dt_now = datetime.datetime.now() 
month0 = str(dt_now.month)
today0 = str(dt_now.day)
todate = ((month0+'월 ')+(today0+'일'))
#================================개인정보============================
usr = "rnjsxodnd10"
pwd = "dnd1357911"

path = "C:\chromedriver.exe"
driver = webdriver.Chrome(path)
print(todate,'출석 프로그램 시작.. 홈페이지 접속 중..')
spacemode()
driver.get("https://hoc5.ebssw.kr/soraehigh303/hmpg/hmpgAlctcrListView.do?menuSn=310091")
print('홈페이지 접속!')
spacemode()
driver.get("https://hoc5.ebssw.kr/sso/loginView.do?loginType=onlineClass&hmpgId=soraehigh303")
print('로그인 중....')
spacemode()
assert "EBS 온라인 클래스" in driver.title
elem = driver.find_element_by_id("j_username") # input  type name j_username
elem.send_keys(usr)
elem = driver.find_element_by_id("j_password") # input  type name j_password
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
time.sleep(1)
#=======================중복 로그인 체크===============================
# popup = driver.switch_to.alert
try:
	popup = driver.switch_to.alert
	print(popup)
	popup.accept()
except:
	pass
#=======================로그인 완료!!!!================================
print('로그인 완료!')
spacemode()
time.sleep(2)
print("출석중...")
spacemode()
print(todate,'출석 게시물 찾는 중..')
#=======================403 error 방지================================
fullUrl = 'https://hoc5.ebssw.kr/soraehigh303/hmpg/hmpgBbsListView.do?menuSn=326023&bbsId=BBSID_000367906'
req = urllib.request.Request(fullUrl, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'})
response = urllib.request.urlopen(req).read()
text = response.decode('utf-8')
spacemode()
#=======================출석창 접근====================================
driver.get("https://hoc5.ebssw.kr/soraehigh303/hmpg/hmpgBbsListView.do?menuSn=326023&bbsId=BBSID_000367906")
time.sleep(2)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
#=======================최신글 접근======================================
titlelist = soup.select('#swedu_listL > div.table_wrap.line1 > table > tbody > tr:nth-child(1) > td.tit.tl > a[href]')
advalue = str(titlelist)
advalue = advalue[64:70]
print(advalue)
print('working...')
driver.get("https://hoc5.ebssw.kr/soraehigh303/hmpg/hmpgBbsDetailView.do?menuSn=326023&bbsId=BBSID_000367906&bbscttSn={0}".format(advalue))
#=======================날짜 체크중======================================
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
checking = soup.select('#searchVO > div > div > div > div > ul > li > div.open_comment > div.comment_head.clearfix > div.left.fl > p')
print('working..')
chetext = str(checking)
if todate in chetext: #출석 성공
	print('날짜 맞음')
	elem = driver.find_element_by_name("cmmntsCn")
	elem.send_keys('출석 했습니다.')
	elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/form/div/div/div/div/ul/li/div[1]/div[2]/div[4]/a').click()
	try:
		popup = driver.switch_to.alert
		print(popup)
		popup.accept()
	except:
		pass
	time.sleep(2)
	print('출석 완료!')
	spacemode()
	#========================로그 아웃====================================
	print('로그아웃중...')
	spacemode()
	driver.get("https://hoc5.ebssw.kr/sso?c=LO&amp;returnUrl=https://hoc5.ebssw.kr:443/soraehigh303")
	print('출석 프로그램 종료')
	driver.quit()
else : #출석 실패
	print('날짜 틀림')
	driver.quit()		
'''
결론은 주소값 마지막 6자리의 숫자만 바뀌는 것을 볼 수 있음 => 주소를 현재 날짜 맞는 걸 크롤링해서 뒤 6자리 수 찾아 주소 값에 대입
https://hoc5.ebssw.kr/soraehigh303/hmpg/hmpgBbsDetailView.do?menuSn=326023&bbsId=BBSID_000367906&bbscttSn=506080
https://hoc5.ebssw.kr/soraehigh303/hmpg/hmpgBbsDetailView.do?menuSn=326023&bbsId=BBSID_000367906&bbscttSn=505496
#searchVO > div > div > div > div > ul > li > div.open_comment > div.comment_head.clearfix > div.left.fl > p
rnjsxodnd10
dnd1357911
'''