
from dataclasses import is_dataclass
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import requests
import json
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import re

# chromedriver의 위치 저장하고 구글을 연다.
driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
driver.get('https://google.com')
time.sleep(1.0)

# 검색창 html의 이름이 q(검색창을 찾아서 '교보문고' 검색하고 엔터)
element = driver.find_element(By.NAME,'q')
element.send_keys("교보문고")
element.submit()

# 교보문고 홈페이지의 xpath를 복사해서 클릭하도록 함
driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a/h3').click()
time.sleep(3.0)
# '국내도서' 의 xpath 복사 후 클릭
driver.find_element(By.XPATH, '//*[@id="header"]/div[3]/ul[1]/li[1]/a').click()
time.sleep(1.0)
# '유아' 의 xpath 복사 후 클릭
driver.find_element(By.XPATH, '//*[@id="main_snb"]/div[1]/ul[3]/li[1]/a').click()
# '베스트셀러' 의 xpath 복사 후 클릭
driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div/div[3]/ul/li[2]/a/span').click()
# 해당 url 저장
url = 'http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?perPage=20&mallGb=KOR&linkClass=41&menuCode=002'
# 해당 페이지의 html 저장
response = requests.get(url)
# 파싱한 html을 변수로 정의
html_data = bs(response.text, 'html.parser')
# url을 얻기 위해 isbn을 저장
isbn_lst = []
for isbn in html_data.find_all('input',{'name':'barcode'}):
    isbn_lst.append(isbn.get('value'))
isbn_lst = list(filter(None, isbn_lst))

# url 뒤에 각 책의 isbn을 붙여 url반복
for page_isbn in isbn_lst:
    page_url = 'http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&linkClass=41&barcode=' + page_isbn
    # 해당 페이지의 html 저장, 변수로 정의
    response1 = requests.get(page_url)
    html_data1 = bs(response1.text, 'html.parser')
    # div태그의 class가 box_detail_point인 html을 찾아 저장
    book_data = html_data1.find('div', class_= 'box_detail_point')
    # 찾은 것에서 다시 태그가 strong인 요소를 책 제목으로 저장
    book_ti = book_data.find('strong')
    book_title = book_ti.text
    # div태그의 class가 author인 html을 찾아 저장
    author_data = html_data1.find('div', class_= 'author')
    # 그 중 태그가 a인 요소를 작가로 저장
    book_wri = author_data.find('a')
    book_writer = book_wri.text
    # 출판사는 title 요소가 출판사, 출간일은 title요소가 출간일
    book_pub = author_data.find(title = '출판사')
    book_publisher = book_pub.text
    book_d = author_data.find(title = '출간일')
    book_date = book_d.text
     # isbn, 쪽수, 크기를 불러오기 위해 해당 html에 접근하여 tr인 요소를 모두 찾고, 그 중에 td인 요소를 각각 저장
    detail = html_data1.find('table', {'class':'table_simple2 table_opened margin_top10'})
    tr = detail.find_all('tr')
    td_lst = []
    for i in tr:
        td_lst.append(i.find('td').text)
    book_isbn = td_lst[0]
    book_page = td_lst[1]
    book_size = td_lst[2]
    
    # 출판사 서평 저장
    publisher_review = html_data1.find('div', class_= 'content')
    #box_review = driver.find_elements(By.CSS_SELECTOR, 'box_detail_review')

    # 북로그 전체보기 클릭
    #driver.find_element(By.XPATH, '//*[@id="container"]/div[5]/div[1]/div[4]/h2[2]/small/a[1]').click()
    #time(300)
    
    # 리뷰 댓글 불러오기
    driver.get(page_url)
    klover_review = []
    
    # 스크롤 이동
    driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    # 회원리뷰 칸 선택
    driver.find_element(By.XPATH, '//*[@id="detailFixedTab"]/div/div[1]/ul/li[3]/a').click()
    driver.execute_script("window.scrollTo(0, 5000)")
    time.sleep(5)
    # 전체버튼 클릭
    driver.find_element(By.XPATH, '//*[@id="sorting_list1"]/li[2]/a').send_keys(Keys.ENTER)
    time.sleep(10)
    # 클로버 리뷰 개수 파악
    review_cnt = driver.find_element(By.XPATH, '//*[@id="kloverTotal"]').text
    rev_page = int(re.sub(r'[^0-9]', '', review_cnt)) // 5 + 1   
    pagenum = driver.find_element(By.XPATH, '//*[@id="reviewFrm"]/input[12]')
    
    try:
        for pg in range(1, rev_page + 1):
        # 리뷰 댓글을 리스트에 저장하는 반복문
            text = driver.find_elements(By.CLASS_NAME, 'txt')
            for txt in text:
                klover_review.append(txt.text)
                try:
                    driver.execute_script("_go_targetPage('2')")
                    time.sleep(3)
                except:
                    continue
        print(klover_review)
    except:
        continue
   
    
   
    