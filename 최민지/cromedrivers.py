from ast import keyword
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from selenium.webdriver.chrome.options import Options

#chromedriver 경로 위치
browser = webdriver.Chrome("/Users/choiminji/Desktop/chromedriver")

#구글 홈페이지 실행
browser.get('https://www.google.com/search?q=')

#구글 검색창에서 '교보문고' 검색어 입력 후 검색
element = browser.find_element(By.NAME, "q")
element.send_keys("교보문고")
element.send_keys("\n")

#교보문고 홈페이지 클릭
browser.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a/div/cite').click()

#국내도서 클릭
browser.find_element(By.XPATH, '//*[@id="header"]/div[3]/ul[1]/li[1]/a').click()

#유아(0~7) 클릭
browser.find_element(By.XPATH, '//*[@id="main_snb"]/div[1]/ul[3]/li[1]/a').click()

#유아(0~7) 베스트셀러 클릭
browser.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div/div[3]/ul/li[2]/a/span').click()

#각 페이지 안에서 반복
#1페이지 당  20개
#각각의 책을 눌러 원하는 정보인 저자, 책 이름, ISBN-13, 키워드, 출판사 서평을 찾는다.
#json파일에 저장

pageNum = 1
lastpage = 8
while pageNum < lastpage + 1:
    href = "javascript:_go_targetPage('{pageNum}')"

    html = urllib.request.urlopen(browser).read()
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find_all(class_ = 'title')

    for i in title:
        print(i.attrs['title'])
        print(i.attrs['author'])
        print()
        pageNum += 1

#왜 브라우저가 마지막에 꺼지는지
#하나하나 책 페이지에 들어가서 데이터를 추출해야 하는 지