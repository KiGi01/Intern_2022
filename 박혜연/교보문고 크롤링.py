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

import requests
import os
import json
from collections import OrderedDict
from bs4 import BeautifulSoup
import sys

#화면 초기화. 모든 문자 삭제 함수 정의.
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':

    #교보문고 사이트의 기본 구조.
    kyobo_URL = 'http://www.kyobobook.co.kr/categoryRenewal/categoryMain.laf?perPage=20&mallGb={0}' \
                '&linkClass={1}&menuCode={2}'

    #추후 사용할 리스트 미리 생성. 각각
    t = list()
    u = list()
    c = list()
    g = list()
    a = list()
    d = list()
    o = list()

    #검색 시, 제일 처음 값.
    start_num = 1

    #화면 초기화 실행.
    clear_screen()

    #교보문고 홈페이지 내의 카테고리 이용
    print("""
    =======================
    DB를 구축할 도서의 차트를 선택해주세요.
    
    1. 베스트 셀러
    2. 신상품
    3. 종료
    =======================
    """)

    #{2}에 들어갈 정보
    num2 = input("입력 : ")

    if num2 == '1':
        standard_2 = "002"

    if num2 == '2':
        standard_2 = "003"

    elif num2 == '3':
        print('서비스를 종료합니다.')
        #sys를 이용해서 강제로 코드 종료.
        sys.exit()

    #교보문고 홈페이지 내의 카테고리 이용
    print("""
    =======================
    DB를 구축할 도서의 카테고리를 선택해주세요.
    
    1. 국내 도서
    2. 국외 도서
    3. 종료
    =======================
    """)

    #{0}에 들어갈 정보
    num0 = input("입력 : ")

    #교보문고 홈페이지 내의 카테고리 이용
    if num0 == '1':
        standard_0 = "KOR"
        print("""
            =======================
            DB를 구축할 도서의 카테고리를 선택해주세요.

            1. 소설
            2. 시/에세이
            3. 경제/경영
            4. 자기계발
            5. 인문
            6. 역사/문화
            7. 정치/사회
            8. 예술/대중문화
            9. 과학
            10. 유아(0 ~ 7세)
            11. 어린이(초등)
            12. 청소년
            13. 그 외
            =======================
            """)

        #{1}에 들어갈 정보
        num1 = input("입력 : ")

        if num1 == '1':
            standard_1 = "01"

        if num1 == '2':
            standard_1 = "03"

        if num1 == '3':
            standard_1 = "13"

        if num1 == '4':
            standard_1 = "15"

        if num1 == '5':
            standard_1 = "05"

        if num1 == '6':
            standard_1 = "19"

        if num1 == '7':
            standard_1 = "17"

        if num1 == '8':
            standard_1 = "23"

        if num1 == '9':
            standard_1 = "29"

        if num1 == '10':
            standard_1 = "41"

        if num1 == '11':
            standard_1 = "42"

        if num1 == '12':
            standard_1 = "38"

        if num1 == '13':
            print('현재 서비스를 제공하지 않는 카테고리입니다. 서비스를 종료합니다.')
            sys.exit()

    if num0 == '2':
        standard_0 = "ENG"

    elif num0 == '3':
        print('서비스를 종료합니다.')
        sys.exit()

    #정보 추출할 도서 권 수 입력.
    book_Num = int(input("DB를 구축할 도서의 개수를 입력해주세요 : "))

    #교보문고 기본 구조 속 {1}, {2}, {3} 실제 값으로 변경 후 검색 시작.
    while True:
        kyobo_URL = kyobo_URL.format(standard_0, standard_1, standard_2)
        #해당 주소의 요소 추출.
        response = requests.get(kyobo_URL)

        # bs4를 이용하여 교보문고 검색 페이지에서 추출할 수 있는 요소 추출.
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # 해당 페이지의 책 상세 설명 주소 접속.
            kyobo_books = soup.select("")