from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 브라우저 생성
browser = webdriver.Chrome('/Users/user/chromedriver')

# 웹사이트 열기
browser.get('https://google.com')

# 로딩이 끝날 동안 2초 기다린다
browser.implicitly_wait(3)

# 화면 크기 최대화
browser.maximize_window()

# 검색창 클릭
search = browser.find_element(By.NAME, 'q')
search.click()

# 검색어 입력
search.send_keys('교보문고')
search.send_keys(Keys.ENTER)

# 교보문고 홈페이지 링크 클릭 및 이동
browser.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a/h3').click()

# 교보문고 홈페이지로 이동하는 동안 2초 기다린다
time.sleep(2)

# 국내도서
browser.find_element(By.XPATH, '//*[@id="header"]/div[3]/ul[1]/li[1]/a').click()

# 유아(0~7세)
browser.find_element(By.XPATH, '//*[@id="main_snb"]/div[1]/ul[3]/li[1]/a/em').click()

# 베스트셀러
browser.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div/div[3]/ul/li[2]/a').click()