"""
week 7. 유아 베스트셀러 목록에 있는 각각의 도서 페이지 진입하기까지 완료
week 8. 도서 페이지 진입하기 수정 + 데이터 크롤링 최종 코드 완성 (json 수정 필요)
"""

# 0. 필요한 모듈 가져오기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from bs4 import BeautifulSoup
import time, math, json

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
                time.sleep(7)
            except:
                driver.close()
                break
        driver.switch_to.window(driver.window_handles[0])
        driver.back()
    except:
        book_blog_list = "등록된 리뷰가 없습니다."
    print(book_blog_list)

    book = {"제목":book_title, "저자":book_writer, "출판사":book_publisher, "출간일":book_date, "ISBN-13":book_isbn, "키워드":book_keyword, "소개":book_detail, "출판사 서평":book_review_pub, "Klover 평점":book_level, "Klover 리뷰":book_klover_list, "북로그 리뷰":book_blog_list}
    with open("./best_seller_박수현.json", "a", -1, "utf-8") as file:
        json.dump(book, file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    # 1. 크롬 드라이버 설정 및 웹 페이지 열기
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get("https://google.com")
    driver.maximize_window()

    # 2. 교보문고 검색 및 홈페이지 클릭하기
    driver.find_element(By.NAME, "q").send_keys("교보문고\n")
    driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/a").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='welcomeAdLayer']/div/button").click()
    pop_up = Alert(driver)
    pop_up.accept()

    # 3. 유아 베스트셀러 페이지 진입하기
    driver.find_element(By.LINK_TEXT, "국내도서").click()
    driver.find_element(By.LINK_TEXT, "유아(0~7세)").click()
    driver.find_element(By.LINK_TEXT, "베스트셀러").click()
    time.sleep(5)

    # 4. 베스트셀러 목록에 있는 도서 페이지 진입하기
    for i in range(1, 9):
        for j in range(1, 40, 2):
            if i == 8 and j == 21:
                print('done')
                driver.quit()
                break
            
            driver.find_element(By.XPATH, f"//*[@id='prd_list_type1']/li[{j}]/div/div[1]/div[2]/div[1]/a").click()
            time.sleep(5)
            # 5. 데이터 크롤링 프로그램 실행하기
            is_book_info()
            driver.back()
            driver.back()
            time.sleep(5)

        if i == 8:
            break
        driver.execute_script("window.scrollTo(0, 0)")
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "div.list_paging > a.btn_next").click()
        time.sleep(5)