# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requester as req

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
urladd = 'http://www.google.com/'

driver.get(urladd)
requested_SC = req.request_url(urladd)
print(requested_SC)
elem = driver.find_element(By.NAME, 'q') # 이런 식으로 서칭 해야 적용됨 (버전 : 셀레니움 4)
searching = input("검색 할 키워드 입력 : ")
elem.send_keys(searching + Keys.ENTER)
time.sleep(2)