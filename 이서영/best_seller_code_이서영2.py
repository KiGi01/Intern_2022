'''
<문제 및 제출 파일>
Q : 교보문고에서 국내도서 > 유아(0~7세) > 베스트셀러 목록에 있는 도서에 대한 정보를 자동으로 수집할 수 있는 프로그램을 작성하시오.

제출해야 할 파일 : 'best_seller_code_본인이름.py', 'best_seller_본인이름.json' (파일 2개)

<조건>
1. 셀레니움과 BeautifulSoup을 모두 활용할 것.
2. book_sample.json과 유사한 형태의 출력 결과물을 작성할 것.(반드시 동일할 필요는 없음)
3. "driver.get('https://google.com')"를 시작으로 크롤링을 수행할 것.(구글 -> 교보문고 검색 -> 교보문고 홈페이지 클릭 -> ...)
4. 한번의 프로그램 실행으로 베스트셀러에 대한 책정보 크롤링이 수행되어야 함.


<기타사항>
- 아래의 주어진 코드와 같이 추출된 서지정보는 최종적으로 주어진 딕셔너리에 담기는 형식.
- book_title, book_writer 등 미리 주어진 변수는 임의로 수정 가능함.
- 웹 크롤링의 경우(특히 셀레니움), 개인 상황에 따라 다양한 오류가 발생할 수 있음.

### 주석 작성은 아래와 같이 코드 옆이 아닌 위에 작성 부탁해요!

아래 코드는 하나의 예시이니 수정하여 작성하셔도 괜찮습니다.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

# 브라우저 생성
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

service_obj = Service(r'C:/chromedriver.exe')
browser = webdriver.Chrome(options=options, service=service_obj)

# 웹 사이트 열기
browser.get('http://www.kyobobook.co.kr/index.laf?NaPm=ct%3Dl6y1bfub%7Cci%3Dcheckout%7Ctr%3Dds%7Ctrx%3D%7Chk%3Dfe86f8e3aa56ed3958e08d10c943f6782ba91256&OV_REFFER=https://search.naver.com/search.naver%3Fwhere=nexearch%26sm=top_hty%26fbm=1%26ie=utf8%26query=%EA%B5%90%EB%B3%B4%EB%AC%B8%EA%B3%A0')

# 로딩이 끝날때까지 10초까지 기다려주기
browser.implicitly_wait(10)

CSS_SELECTOR = 'css selector'
browser.find_element(By.CSS_SELECTOR,'a.text').click()

# 유아(0~7세) 메뉴 클릭
browser.find_element(By.XPATH,'//*[@id="main_snb"]/div[1]/ul[3]/li[1]/a/em').click()

# 베스트셀러 메뉴 클릭
browser.find_element(By.XPATH,'//*[@id="container"]/div[2]/div/div/div[3]/ul/li[2]/a/span').click()

# 정렬 메뉴 클릭
browser.find_element(By.XPATH,'//*[@id="showcaseNew"]/div[1]/div').click()

# 50개씩 정렬 설정
browser.find_element(By.XPATH, '//*[@id="showcaseNew"]/div[1]/div/span[1]/ul/li[2]/a').click()

# 첫페이지에 있는 책 목록 클릭 후 제목 출력하기 (반복문 이용)
f = '//*[@id="prd_list_type1"]/li['
b = ']/div/div[1]/div[2]/div[1]/a/strong'

# 반복문으로 순서대로 도서 선택
for x in range(1, 100, 2):
    z = f+str(x)+b
    browser.find_element(By.XPATH, z).click()
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 각 도서의 제목 선택
    title = soup.select_one('.box_detail_point > h1 > strong')
    # 제목 출력
    print(title.text.strip())

    # 각 도서의 작가 선택
    author = soup.select_one('.box_detail_point >div > span > a.detail_author')
    # 작가 출력
    print(author.text.strip())
    
    # 각 도서의 출판사 선택
    publisher = soup.select_one('.box_detail_point >div > span:nth-child(3) > a')
    # 출판사 출력
    print(publisher.text.strip())
    
    # 각 도서의 출판일 선택
    book_date = soup.select_one('.box_detail_point >div > span.date')
    # 출판일 출력
    print(book_date.text.strip())

    # 서평 더보기란 클릭(XPATH가 다른 도서들이 있어서 수정 필요)
    try:
        add_ = browser.find_element(By.XPATH, '//*[@id="container"]/div[5]/div[1]/div[3]/div/div[1]/a')
        browser.find_element(By.XPATH, '//*[@id="container"]/div[5]/div[1]/div[3]/div/div[1]/a').click()
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        review = soup.select_one('.content_left > div:nth-child(5) > div > div.content:nth-child(2)')

    except: 
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        review = soup.select_one('.content_left > div:nth-child(5) > div > div.content')
    # 서평 출력
    print(review.text.strip())    

    # 이전 페이지로 되돌아가기
    browser.back()

'''
책 목록 xpath

1번째 //*[@id="prd_list_type1"]/li[1]/div/div[1]/div[2]/div[1]/a/strong
2번째 //*[@id="prd_list_type1"]/li[3]/div/div[1]/div[2]/div[1]/a/strong
.
.
50번째 //*[@id="prd_list_type1"]/li[99]/div/div[1]/div[2]/div[1]/a/strong

51번째 //*[@id="prd_list_type1"]/li[1]/div/div[1]/div[2]/div[1]/a/strong
'''
