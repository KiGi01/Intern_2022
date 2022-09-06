from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import codecs


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

url = ('http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&linkClass=41&barcode=002')

bsObject = BeautifulSoup(url, "html.parser")

book_rank = 0
isbn_list = []

for isbn in bsObject.find_all('input', {'name':'barcode'}):
    isbn_list.append(isbn.get('value'))

for isbn in isbn_list:
    url1 = ('http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&linkClass=41&barcode=' + isbn)
    
    #빈 리스트 생성
    title_list = []
    author_list = []
    writing_basic_list = []
    writing_basic_list2 = []

    source = browser.page_source

    parsed_source = BeautifulSoup(source, "html.parser")
    #클래스가 'title' 찾기
    ul_list = parsed_source.find_all("ul", class_ = "title")
    ul_list = ul_list[0]

    div_title_list = ul_list.find_all("div", class_ = "title")
    for item in div_title_list:
        title_list.append(item.text.strip())
    #div class인 'author' 찾기 = 저자 데이터 
    div_author_list = ul_list.find_all("div", class_ = "author")
    for item in div_author_list:
        author_list.append(item.text.strip().replace("\n","").replace("\t",""))
    #div class인 'title_datial_basic2' 찾기 = 책 소개 데이터
    div_writing_list = ul_list.find_all("div", class_ = "title_detail_basic2")
    for item in div_writing_list:
        writing_basic_list.append(item.text)
    #div class인 'box_detail_article' 찾기 = 두번째 책 소개 데이터
    div_writing_list2 = ul_list.find_all("div", class_ = "box_detail_article")
    for item in div_writing_list2:
        writing_basic_list2.append(item.text)

    for i in range(len(title_list)):
        book_rank += 1
        f.write("%s등" % book_rank + "\n")
        f.write(title_list[i] + "\n")
        f.write(author_list[i] + "\n")
        f.write(writing_basic_list[i] + "\n")
        f.write(writing_basic_list2[i] + "\n")
