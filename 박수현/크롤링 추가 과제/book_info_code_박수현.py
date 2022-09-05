"""
코드 실행 중 발견한 오류

1. driver.back()의 과부하 : 164번째 줄에서 driver.back()을 연속으로 사용했는데, 문제 없이 코드를 돌리던 중 어느 순간 갑자기 그 부분에서 오류 발생
> time.sleep(1)을 사이에 넣으며 해결

2. 베스트셀러 목록 중 유아 > 유아교양의 151위부터 이탤릭체가 사용되며 XPath가 변함 (751번째 책에서 오류...)
150위 : //*[@id="prd_list_type1"]/li[99]/div/div/div[2]/div[1]/a
151위 : //*[@id="prd_list_type1"]/i/li[2]/div/div[1]/div[2]/div[1]/a
> try-except를 활용하며 해결
except_count = 2
try:
    driver.find_element(By.XPATH, f"//*[@id='prd_list_type1']/li[{x}]/div/div[1]/div[2]/div[1]/a").click()
except:
    driver.find_element(By.XPATH, f"//*[@id='prd_list_type1']/i/li[{except_count}]/div/div[1]/div[2]/div[1]/a").click()
    except_count += 2

3. 2번의 코드를 실행할 때, 150위 > 151위로 넘어가는 부분만 실행할 땐 문제 없이 실행됐는데 처음부터 실행하자 해당 위치에서 동일 오류 발생
> 결국 바코드 추출해서 해당 페이지 진입하는 방식으로 변경

4. 어린이 > 초등학교 입학준비의 경우 베스트셀러 진입을 위한 페이지가 다르게 제공 됨
> if문을 설정해 다른 페이지로 진입하며 해결
"""

# 0. 필요한 모듈 가져오기
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time, math, json

# 0. 목록 진입 및 바코드 추출 프로그램 정의하기
def is_book_barcode(i):
    # link_class = 목록별로 링크에서 변경되는 'linkClass=' 부분에 대한 리스트
    link_class = [4107, 4109, 4111, 4115, 4117, 4119, 4121, 4123, 4202, 4204, 4206, 4208, 4210, 4212, 4214, 4216, 4220]
    if i == 12:
        book_link = "https://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?pageNumber=1&perPage=50&mallGb=KOR&linkClass=4210&ejkGb=&sortColumn=&menuCode=002"
    else:
        book_link = f"https://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?pageNumber=1&perPage=300&mallGb=KOR&linkClass={link_class[i]}&ejkGb=&sortColumn=near_date"
    driver.get(book_link)
    driver.maximize_window()
    time.sleep(5)

    # lank_page = 목록 데이터
    lank_page = BeautifulSoup(driver.page_source, "html.parser")

    # book_barcode_list = 베스트셀러 내의 바코드에 대한 빈 리스트
    book_barcode_list = []
    for book_barcode in lank_page.find_all("input", {"name":"barcode"}):
        book_barcode_list.append(book_barcode.get("value"))
    book_barcode_list = list(filter(None, book_barcode_list))
    
    return book_barcode_list

# 0. 데이터 크롤링 프로그램 정의하기
def is_book_info():
    # book_page = 책 데이터
    book_page = BeautifulSoup(driver.page_source, "html.parser")

    # book_title = 책 제목
    book_title = book_page.select_one("h1.title > strong").text.strip()
    # book_writer = 책 저자
    book_writer = book_page.select_one("a.detail_author").text.strip()
    # book_info = 책 정보 (저자 | 출판사 | 출간일)
    book_info = book_page.select_one("div.author").text.split("|")
    # book_publisher = 책 출판사
    book_publisher = book_info[-2].strip()
    # book_date = 책 출간일
    book_date = book_info[-1].strip().replace(" 출간", "").replace("\t", "").replace("\n", "")
    # book_isbn = 책 ISBN-13
    book_isbn = book_page.select_one("tbody > tr > td > span").text.strip()
    # book_keyword = 책 키워드
    book_keyword_list = []
    for book_keyword in book_page.select("div.tag_list > a > span > em"):
        book_keyword_list.append(book_keyword.text.strip().replace("#", ""))
    if book_keyword_list == []:
        book_keyword = "등록된 키워드가 없습니다."
    else:
        book_keyword = ', '.join(book_keyword_list)
    print(book_title, book_writer, book_publisher, book_date, book_isbn, book_keyword)

    # book_detail = 책 소개
    try:
        book_detail_1 = book_page.select_one("div.title_detail_basic2").text.strip().replace("\n", "")
    except:
        book_detail_1 = ""
    book_detail_2 = book_page.select_one("div.box_detail_article").text.strip().replace("\n", "")
    try:
        book_detail_3 = book_page.select_one("div.box_detail_comment > div.box_detail_article").text.strip().replace("\n", "")
        book_detail = book_detail_1 + book_detail_2 + book_detail_3
    except:
        book_detail = book_detail_1 + book_detail_2
    # book_review_pub = 책 출판사 서평
    try:
        book_review_pub = book_page.select("div.box_detail_article > div.content")[-1].text.strip().replace("\n", "").replace("\t\t\t\t닫기", "")
    except:
        book_review_pub = "등록된 출판사 서평이 없습니다."
    print(book_detail)
    print(book_review_pub)

    # book_level = Klover 평점
    # book_klover = Klover 리뷰
    try:
        book_level = book_page.select_one("div.popup_load > em").text.strip()
        driver.get(driver.current_url + "#review")
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, "전체").click()
        time.sleep(5)
        book_klover_list = []
        x = 1
        while True:
            try:
                book_page = BeautifulSoup(driver.page_source, "html.parser")
                len_book_klover = book_page.select_one("span.kloverTotal").text.strip()
                for book_klover in book_page.select("div#box_detail_review.box_detail_review dd.comment"):
                    book_klover_list.append(book_klover.text.strip().replace("\n", "").replace("크게보기", ""))
                if x == math.ceil(int(len_book_klover[1:-1]) / 5):
                    break
                driver.find_elements(By.CSS_SELECTOR, "div#box_detail_review.box_detail_review a.pad")[-2].click()
                x += 1
                time.sleep(5)
            except:
                break
    except:
        book_level = "-"
        book_klover_list = "등록된 리뷰가 없습니다."
        driver.get(driver.current_url + "#review")
        time.sleep(5)
    print(book_level)
    print(book_klover_list)

    # book_blog = 북로그 리뷰
    try:
        driver.find_element(By.LINK_TEXT, "전체보기").click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        book_blog_list = []
        x = 1
        while True:
            try:
                book_page = BeautifulSoup(driver.page_source, "html.parser")
                for book_blog in book_page.select("div.content"):
                    book_blog_list.append(book_blog.text.strip().replace("\n", "").replace("\xa0", "").replace("\u200b", ""))
                x += 1
                driver.find_element(By.XPATH, f"/html/body/div/div[2]/ul/li[{x}]/a").click()
                time.sleep(5)
            except:
                driver.close()
                break
        driver.switch_to.window(driver.window_handles[0])
        driver.back()
    except:
        book_blog_list = "등록된 리뷰가 없습니다."
    print(book_blog_list)

    book = {"제목":book_title, "저자":book_writer, "출판사":book_publisher, "출간일":book_date, "ISBN-13":book_isbn, "키워드":book_keyword, "소개":book_detail, "출판사 서평":book_review_pub, "Klover 평점":book_level, "Klover 리뷰":book_klover_list, "북로그 리뷰":book_blog_list}
    return book

# 0. 목록:[category_book] 딕셔너리 저장 프로그램 정의하기
def is_list_to_dic(i, category_book):
    # category_name = 목록의 이름에 대한 리스트
    category_name = ["유아놀이", "유아그림책", "유아교양", "유아학습", "유아캐릭터", "0세부터100세그림책", "0-3세", "4-7세", "교과서수록/연계도서", "어린이문학", "어린이교양", "어린이만화", "초등학교 입학준비", "초등1-2힉년", "초등3-4힉년", "초등5-6힉년", "초등1-6힉년"]
    dic_key = category_name[i]
    book_dic = {dic_key:category_book}
    return book_dic

if __name__ == '__main__':
    # 1. 크롬 드라이버 설정 및 웹 페이지 열기
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get("https://google.com")

    book_info = []
    book_count = 0
    for i in range(17):
        category_book = []
        # 2. 목록 진입 및 바코드 추출 프로그램 실행하기
        for x in is_book_barcode(i):
            # (만약 과도한 크롤링으로 차단 당한다면, 최대 몇 개까지 수집이 가능한지 확인하기 위함)
            book_count += 1
            print(f"===== {book_count} 번째 책 =====")

            # 3. 목록에 있는 도서 페이지 진입하기
            book_link = f"https://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&barcode={x}"
            driver.get(book_link)
            time.sleep(3)
            # 4. 데이터 크롤링 프로그램 실행하기
            category_book.append(is_book_info())
        
        # 5. 목록:[category_book] 딕셔너리 저장 프로그램 실행하기
        book_info.append(is_list_to_dic(i, category_book))
    
    print("done")
    driver.quit()

    # 6. book_info 리스트에 저장한 딕셔너리를 json에 저장하기
    with open("./book_info_박수현.json", "a", -1, "utf-8") as file:
        json.dump(book_info, file, indent=4, ensure_ascii=False)