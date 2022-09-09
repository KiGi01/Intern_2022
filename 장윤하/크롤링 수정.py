
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

# 공백을 없애는  함수 
def no_space(text):
    text1 = re.sub('&nbsp;|&nbsp;|\n|\t|\r', '', text)
    text2 = re.sub('\n\n','', text1)
    return text2

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

for totalpage in range(1, 9):
    # 해당 url 저장
    # url을 얻기 위해 isbn을 저장
    isbn_lst = []
    barcode = driver.find_elements(By.NAME, 'barcode')
    for bar in barcode:
        isbn_lst.append(bar.get_attribute('value'))
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
        book_title = no_space(book_ti.text)
        # div태그의 class가 author인 html을 찾아 저장
        author_data = html_data1.find('div', class_= 'author')
        # 그 중 태그가 a인 요소를 작가로 저장
        book_wri = author_data.find('a')
        book_writer = no_space(book_wri.text)
        # 출판사는 title 요소가 출판사, 출간일은 title요소가 출간일
        book_pub = author_data.find(title = '출판사')
        book_publisher = no_space(book_pub.text)
        book_d = author_data.find(title = '출간일')
        book_date = no_space(book_d.text)
        # isbn, 쪽수, 크기를 불러오기 위해 해당 html에 접근하여 tr인 요소를 모두 찾고, 그 중에 td인 요소를 각각 저장
        detail = html_data1.find('table', {'class':'table_simple2 table_opened margin_top10'})
        tr = detail.find_all('tr')
        td_lst = []
        for i in tr:
            td_lst.append(i.find('td').text)
        book_isbn = td_lst[0]
        book_page = no_space(td_lst[1])
        book_size = td_lst[2]
        
        # 출판사 서평 저장
        driver.get(page_url)
        
        try:
            try:
                # '책 속으로' 부분이 존재하는 경우
                driver.find_element(By.XPATH,'//*[@id="container"]/div[5]/div[1]/div[3]/div[10]/div[1]/a').click()
                publisher_review = no_space(driver.find_element(By.XPATH, '//*[@id="container"]/div[5]/div[1]/div[3]/div[10]/div[2]').text)
            # 없는 경우
            except:
                driver.find_element(By.XPATH, '//*[@id="container"]/div[5]/div[1]/div[3]/div[9]/div[1]/a').click()
                publisher_review =  no_space(driver.find_element(By.XPATH, '//*[@id="container"]/div[5]/div[1]/div[3]/div[9]/div[2]').text)
            
            # 닫기 버튼이 포함되기 때문에 제거
            publisher_review = publisher_review[:-2]
        # 출판사 서평이 없는 경우 "없음 저장"
        except:
            publisher_review = "없음"
        
        # 리뷰 댓글 불러오기
        klover_review = []
        
        # 스크롤 이동
        driver.execute_script("window.scrollTo(0, 3000)")
        time.sleep(3)
        # 회원리뷰 칸 선택
        driver.find_element(By.XPATH, "//*[contains(text(), '회원리뷰')]").click()
        driver.execute_script("window.scrollTo(0, 5000)")
        time.sleep(5)
        # 전체버튼 클릭
        try:
            driver.find_element(By.XPATH, '//*[@id="sorting_list1"]/li[2]/a').click()
            time.sleep(10)
        except:
            continue
        # 클로버 리뷰 개수 파악
        review_cnt = driver.find_element(By.XPATH, '//*[@id="kloverTotal"]').text
        # 숫자만 가져오기
        rev_page = int(re.sub(r'[^0-9]', '', review_cnt)) // 5 + 1   
        pagenum = driver.find_element(By.XPATH, '//*[@id="reviewFrm"]/input[12]')
        
        try:
            for pg in range(1, rev_page + 1):
            # 리뷰 댓글을 리스트에 저장하는 반복문
                text = driver.find_elements(By.CLASS_NAME, 'txt')
                for txt in text:
                    klover_review.append((txt.text).strip('\n'))
                try:
                    driver.execute_script("_go_targetPage('" + str(pg + 1) + "')")
                    time.sleep(2)
                except:
                    continue
        except:
            klover_review = "없음"
            
        # 북로그 리뷰 
        
        # 리뷰 개수 파악
        log_cnt = driver.find_element(By.CSS_SELECTOR, 'h2:nth-child(5) > span').text
        log_page = int(re.sub(r'[^0-9]', '', review_cnt)) // 10 + 1
        
        # 북로그가 0개일 때 '없음' 저장
        if log_cnt == '(0)':
            booklog = '없음'
        else:
            booklog = []
            # 북로그 전체보기 버튼 클릭 
            total_log = driver.find_element(By.XPATH, "//*[contains(text(), '전체보기')]").click()
            # 팝업창으로 전환
            driver.switch_to.window(driver.window_handles[1])
            # 페이지를 넘기면서 리스트에 북로그 저장
            for pg in range(1, log_page + 1):
                # 북로그를 리스트에 저장하는 반복문
                text = driver.find_elements(By.CLASS_NAME, 'content')
                for txt in text:
                    new_text = (txt.text).replace('\n', ' ')
                    booklog.append((new_text).strip())
                try:
                    # 다음 페이지로 넘길 때 javascript 이용
                    driver.execute_script("_go_targetPage('" + str(pg + 1) + "')")
                    time.sleep(2)
                except:
                    driver.close()
                    
            driver.switch_to.window(driver.window_handles[0])
  
        # 문장수집 
        time.sleep(1)
        # 문장수집 위치를 찾음
        some_tag = driver.find_element(By.XPATH, '//*[@id="box_detail_killingPart"]')
        # 해당 위치까지 스크롤
        action = ActionChains(driver)
        action.move_to_element(some_tag).perform()
        
        # 문장수집 개수 파악
        sentence_cnt = driver.find_element(By.XPATH, '//*[@id="killingTotal"]').text
        # 문장수집 개수가 0인 경우에 없음을 저장
        if sentence_cnt == "(0)":
            sent_lst = "없음"
        else:
            # 한 페이지 당 5개의 문장이 나타남
            sent_page = int(re.sub(r'[^0-9]', '', sentence_cnt)) // 5 + 1   
            pagenum = driver.find_element(By.XPATH, '//*[@id="reviewFrm"]/input[12]')
            sent_lst = []
            
            for pg in range(1, sent_page + 1):
            # 리뷰 댓글을 리스트에 저장하는 반복문
                text = driver.find_elements(By.CLASS_NAME, 'txt')
                for txt in text:
                    sent_lst.append(no_space((txt.text)))
                try:
                    driver.execute_script("_go_targetPage2('" + str(pg + 1) + "')")
                    time.sleep(2)
                except:
                    break
    
            
        # json 저장
        book = {"책제목":book_title, "저자":book_writer, "출판사":book_publisher, "출간일":book_date,"isbn_13":book_isbn, 
                "쪽수":book_page, "크기":book_size, "출판사 서평":publisher_review, 
                "클로버 리뷰":klover_review, "북로그 리뷰":booklog, "문장수집":sent_lst}
        with open('C:\세미나\크롤링\크롤링 인턴과제_2022\크롤링 인턴과제/best_seller_장윤하.json', 'a', -1, 'utf-8') as f : 
            json.dump(book, f, indent=4, ensure_ascii=False)
            
        time.sleep(2)
    
    # 다시 베스트 셀러로 돌아가서 페이지를 하나씩 넘김        
    driver.get('http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?perPage=20&mallGb=KOR&linkClass=41&menuCode=002')
    try:
        driver.execute_script("_go_targetPage('" + str(totalpage + 1) + "')")
        time.sleep(2)
    except:
        driver.close()
        break
        
    
