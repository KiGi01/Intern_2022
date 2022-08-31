from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import json
import traceback

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

#1부터 8페이지까지 반복한다.
for page in range(1,9):
    #2일 때부터 해당 페이지로 가는 버튼을 클릭한다.
    if page >= 2:
        driver.find_element(By.XPATH, f'//*[@id="eventPaging"]/div/ul/li[{page}]/a').click()
        print(page, '페이지')         
    #현재 페이지의 html을 분석한다.
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser") 
    #목록에 있는 각 도서의 isbn을 추출한다.
    isbn_list = []
    for i in soup.find_all('input', {"name" : 'barcode'}):
        isbn_list.append(i.get('value'))
    isbn_list = list(filter(None, isbn_list))
    #isbn을 url에 추가하여 각 도서의 상세페이지로 진입한다.
    for isbn in isbn_list:
        bookpage = driver.get(f'http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&linkClass=41&barcode={isbn}')
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        #책 제목을 추출한다.
        book_title = soup.select_one('div.box_detail_point > h1 > strong').text.strip()
        #저자명을 추출한다.
        book_writer= soup.select_one('div.box_detail_point > div.author > span:nth-child(1) > a').text.strip()
        #출판사명을 추출한다.
        book_pub = soup.find(title = "출판사").text.replace('\n','')
        #출판 연도를 추출한다.
        book_pubdate = soup.find(title="출간일").text.strip()
        book_pubdate = book_pubdate[0:5]
        #isbn을 추출한다.
        book_isbn = isbn
        #책의 주제어를 추출한다.
        book_keyword = soup.select('div.content_left > div:nth-child(5) > div.tag_list > a')
        key = [i.text for i in book_keyword]
        book_keyword = ', '.join(key)
        if key == []:
            book_keyword = "키워드 없음"
        #출판사 서평을 추출한다.
        try:
            book_review_pub = soup.select("div.box_detail_article > div.content")[-1].text.strip().replace("\n", "").replace("닫기", "")
            #print('출판사 서평: ', book_review_pub)
        except:
            book_review_pub = '출판사 서평 없음'
        #북로그 전체보기 버튼을 클릭한다. 
        try: 
            driver.find_element(By.LINK_TEXT, "전체보기").click() 
            time.sleep(1)
            #새롭게 열린 탭으로 전환한다.
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(1)
            #북로그 페이지의 html을 분석한다.
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")     
            #북로그 총 개수를 추출한다.
            total = soup.find(class_ = 'total').text.strip().replace('(', '').replace(')', '')
            #북로그를 추출한다.       
            log = soup.select('div.content')
            book_loglist = []
            for i in log:
                book_loglist.append(i.text.strip().replace("\n", "").replace('\t\t\t\t', '').replace('\"', ''))
            time.sleep(1)
            
            try:
                logpage = 1
                #리스트에 담긴 북로그 개수가 총 개수와 같아질 때까지 다음 페이지 버튼을 누른다.
                while len(book_loglist) != int(total):  
                    logpage += 1
                    driver.find_element(By.XPATH, f"/html/body/div/div[2]/ul/li[{logpage}]/a").click()
                    html = driver.page_source
                    soup = BeautifulSoup(html, "html.parser")     
                    time.sleep(2)
                    log = soup.select('div.content')
                    for i in log:
                        book_loglist.append(i.text.strip().replace("\n", "").replace('\t\t\t\t', '').replace('\"', ''))    
                time.sleep(2) 
                #원래 탭으로 돌아간다.      
                driver.switch_to.window(driver.window_handles[0])        
            #에러 메세지 출력
            except Exception as e:
                print(traceback.format_exc())
            
            #원래 탭으로 돌아간다.    
            driver.switch_to.window(driver.window_handles[0]) 
            book_log = (f'{total}개의 북로그', book_loglist)     
        #북로그가 없는 경우
        except:
            book_log = '북로그 없음'
            
        #json 파일로 저장한다. 
        book = {"책제목":book_title, "저자":book_writer, "출판사":book_pub, "출판 연도":book_pubdate, "isbn_13":book_isbn, "키워드":book_keyword, "출판사 서평":book_review_pub, "북로그":book_log}
        with open('C:/Users/oso21/intern_2022/crawling_project/best_seller_오시연.json', 'a', -1, 'utf-8') as f :
            json.dump(book, f, indent=4, ensure_ascii=False)
    
    #베스트셀러 목록으로 돌아간다.
    driver.get('http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?perPage=20&mallGb=KOR&linkClass=41&menuCode=002')
    
    


