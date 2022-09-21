# 0. 필요한 모듈 가져오기
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time, math, json

# 0. 바코드 텍스트파일 리스트로 변환하는 프로그램 정의하기
# 이후에 추가된 바코드만 크롤링하고자 한다면, f"book_barcode_append_{category_name[i]}.txt" 로 변경
# 오류로 인해 재시도하고자 한다면, f"book_barcode_{category_name[i]}_2.txt" 로 변경
def is_book_barcode(i):
    category_name = ["유아(0~7세)", "어린이(초등)"]
    with open(f"book_barcode_{category_name[i]}.txt", "r") as f:
        book_barcode_list = f.read().splitlines()
    
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

    book = {"제목":book_title, "저자":book_writer, "출판사":book_publisher, "출간일":book_date, "ISBN-13":book_isbn, "키워드":book_keyword, "소개":book_detail, "출판사 서평":book_review_pub, "Klover 평점":book_level, "Klover 리뷰":book_klover_list, "북로그 리뷰":book_blog_list}
    return book

# 0. 목록:[category_book] 딕셔너리 저장 프로그램 정의하기
def is_list_to_dic(i, category_book):
    category_name = ["유아(0~7세)", "어린이(초등)"]
    dic_key = category_name[i]
    book_dic = {dic_key:category_book}
    return book_dic

if __name__ == '__main__':
    # 1. 크롬 드라이버 설정 및 웹 페이지 열기
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get("https://google.com")
    driver.maximize_window()

    book_info = []
    book_count = 0
    for i in range(2):
        try:
            category_book = []
            # 2. 바코드 텍스트파일 리스트로 변환하는 프로그램 실행하기
            book_barcode = is_book_barcode(i)
            for x in book_barcode:
                # (만약 과도한 크롤링으로 차단 당한다면, 몇 권 수집했는지 확인하기 위함)
                book_count += 1
                print(f"===== {book_count} 번째 책 =====")

                # 3. 목록에 있는 도서 페이지 진입하기
                book_link = f"https://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&barcode={x}"
                driver.get(book_link)
                time.sleep(3)
            
                # 4. 데이터 크롤링 프로그램 실행하기
                category_book.append(is_book_info())

        # 5. 다양한 이유로 오류가 떴다면, 해당 바코드부터 새로운 파일에 저장한 후 그전까지의 데이터 저장        
        except:
            book_barcode = book_barcode[book_barcode.index(x):]
            category_name = ["유아(0~7세)", "어린이(초등)"]
            with open(f"book_barcode_{category_name[i]}_2.txt", "w", encoding="UTF-8") as f:
                for barcode in book_barcode:
                    f.write(barcode + "\n")
            
            # 6. 목록:[category_book] 딕셔너리 저장 프로그램 실행하기
            book_info.append(is_list_to_dic(i, category_book))
            break
        
        book_info.append(is_list_to_dic(i, category_book))
    
    print("done")
    driver.quit()

    book_info_dic = {"book_info":book_info}
    # 6. book_info 리스트에 저장한 딕셔너리를 json에 저장하기
    with open("./book_all_info_박수현.json", "a", -1, "utf-8") as file:
        json.dump(book_info_dic, file, indent=4, ensure_ascii=False)