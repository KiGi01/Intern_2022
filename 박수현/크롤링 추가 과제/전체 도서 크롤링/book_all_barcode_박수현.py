# 0. 필요한 모듈 가져오기
from selenium import webdriver
from bs4 import BeautifulSoup
from ast import literal_eval
import time, math

# 0. 목록 진입 및 바코드 추출 프로그램 정의하기
def is_book_barcode(i):
    # category_num = 목록별로 링크에서 변경되는 "목록 숫자" 부분에 대한 리스트
    category_num = [41, 42]
    book_link = f"http://mobile.kyobobook.co.kr/search/bycategory/KOR/{category_num[i]}"
    
    driver.get(book_link)
    time.sleep(3)

    # search_page = 목록 데이터
    search_page = BeautifulSoup(driver.page_source, "html.parser")
    # len_book = 해당 목록의 총 권수
    len_book = search_page.select_one("div.total").text.strip()

    for x in range(math.ceil(int(len_book[0:-2].replace(",", "")) / 8)):
        if x != 0 and x % 500 == 0:
            print(x)
            time.sleep(3)
        
        # 모바일 버전은 다음 페이지 버튼을 누르는 형식이 아닌 스크롤을 맨 아래로 내려야 다음 페이지가 로드되는 형식
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(0.5)

    time.sleep(5)
    search_page = BeautifulSoup(driver.page_source, "html.parser")

    # book_barcode_list = 목록 내의 바코드에 대한 빈 리스트
    book_barcode_list = []
    for book_barcode in search_page.find_all("span", {"class":"disabled"}):
        try:
            book_barcode_dic = literal_eval(book_barcode.get("data"))
            book_barcode_list.append(book_barcode_dic["barcode"])
        # 절판 혹은 품절된 경우 바코드 로드 불가 및 클로버, 북로그 리뷰가 없음
        except:
            pass
    print(len(book_barcode_list))
    
    return book_barcode_list

if __name__ == '__main__':
    # 1. 크롬 드라이버 설정 및 웹 페이지 열기
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get("https://google.com")
    driver.maximize_window()

    for i in range(2):
        # category_name = 목록 이름에 대한 리스트
        category_name = ["유아(0~7세)", "어린이(초등)"]

        with open(f"book_barcode_{category_name[i]}.txt", "w", encoding="UTF-8") as f:
            # 2. 목록 진입 및 바코드 추출 프로그램 실행하기
            for barcode in is_book_barcode(i):
                f.write(barcode + "\n")
    
    driver.quit()