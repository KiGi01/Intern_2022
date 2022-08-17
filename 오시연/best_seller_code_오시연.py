from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
#불필요한 에러 메시지 없애기
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

#셀레니움을 이용하여 구글 홈페이지를 연다.
driver.get('https://google.com')

#검색창에 접근한다.
element = driver.find_element(By.NAME, "q")
#검색어를 '교보문고'로 입력한다.
element.send_keys('교보문고')
#검색을 실행한다.
element.submit()
#교보문고를 클릭한다.
driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a/h3').click()
time.sleep(3)
#국내도서 메뉴를 클릭한다. 
driver.find_element(By.XPATH, '//*[@id="header"]/div[3]/ul[1]/li[1]/a').click()
#유아(0~7)세를 클릭한다.
driver.find_element(By.XPATH, '//*[@id="main_snb"]/div[1]/ul[3]/li[1]/a/em').click()
#베스트셀러를 클릭한다.
driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div/div[3]/ul/li[2]/a/span').click()
#첫번째 책을 클릭한다.
book1 = driver.find_element(By.XPATH, '//*[@id="prd_list_type1"]/li[1]/div/div[1]/div[2]/div[1]/a')
book1.click()
#현재 실행중인 웹 사이트의 소스를 가져온다.
html = driver.page_source
#html parser를 사용해야 한다고 선언한다.
soup = BeautifulSoup(html, "html.parser")

title = soup.select("#container > div:nth-child(4) > form > div.box_detail_point > h1 > strong")
print(title[0].text)

