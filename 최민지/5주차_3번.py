"""
두 날짜(YYYYMMDD)의 차이 일수를 구하는 프로그램을 작성하시오.
※ 단, 프로그래밍 언어에서 지원하는 날짜차이를 계산하는 라이브러리는 사용하지 말것
예)
20070515 sub 20070501 = 14
20070501 sub 20070515 = 14
20070301 sub 20070515 = 75
"""
"""
========================================================================
과제1. 아래에 입력된 두 날짜 간의 차이를 구하는 프로그램을 작성하시오. 
      - 조건 : 날짜 차이를 계산하는 라이브러리 사용 금지
      - first = 20070501
      - second = 20070515
      - 출력값 : 14
========================================================================
"""

def date_count(date):
    year = int(date[0:4]) #date의 0번째부터 3번째까지
    month = int(date[4:6]) #date의 4번째부터 5번째까지
    day =  int(date[6:8]) #date의 6번째부터 7번째까지
    year_number = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400 #년을 일수로 치환
    month_number = 0
    for mon in range(1,month): #월을 일수로 계산
        if mon == 2: #2월이라면 '그레고리력의 윤일'로 인하여 4의 배수인 해이지만 윤일을 넣지 않는 경우는 100으로 나눠떨어지되 400으로는 떨어지지 않는 해
            if year // 400 == 0:
                month_number += 29
            elif year // 100 == 0:
                month_number += 28
            elif year // 4 == 0: 
                month_number += 29
            else:
                month_number += 28
        elif mon in [1, 3, 5, 7, 8, 10, 12]: #1, 3, 5, 7, 8, 10, 12월이라면
            month_number += 31 #31일이라고 계산한다.
        else: #나머지 4, 6, 9, 11월이라면
            month_number += 30 #30일이라고 계산한다.
    return year_number + month_number + day #날짜를 일수로 바꾼 걸 더한다.

def main():
    date1 = input('비교할 첫번째 날짜(YYYYMMDD)를 입력하세요: ')
    date2 = input('비교할 두번째 날짜(YYYYMMDD)를 입력하세요: ')
    print(abs(date_count(date1) - date_count(date2)))

main()

"""
========================================================================
과제2. 아래에 입력된 두 날짜 간의 차이를 구하는 프로그램을 작성하시오. 
      - 조건 : 날짜 차이를 계산하는 라이브러리 사용 금지
      - first = 20070301
      - second = 20070515
      - 출력값 : 75
========================================================================
"""

def date_count(date):
    year = int(date[0:4]) #date의 0번째부터 3번째까지
    month = int(date[4:6]) #date의 4번째부터 5번째까지
    day =  int(date[6:8]) #date의 6번째부터 7번째까지
    year_number = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400 #년을 일수로 치환
    month_number = 0
    for mon in range(1,month): #월을 일수로 계산
        if mon == 2: #2월이라면 '그레고리력의 윤일'로 인하여 4의 배수인 해이지만 윤일을 넣지 않는 경우는 100으로 나눠떨어지되 400으로는 떨어지지 않는 해
            if year // 400 == 0:
                month_number += 29
            elif year // 100 == 0:
                month_number += 28
            elif year // 4 == 0: 
                month_number += 29
            else:
                month_number += 28
        elif mon in [1, 3, 5, 7, 8, 10, 12]: #1, 3, 5, 7, 8, 10, 12월이라면
            month_number += 31 #31일이라고 계산한다.
        else: #나머지 4, 6, 9, 11월이라면
            month_number += 30 #30일이라고 계산한다.
    return year_number + month_number + day #날짜를 일수로 바꾼 걸 더한다.

def main():
    date1 = input('비교할 첫번째 날짜(YYYYMMDD)를 입력하세요: ')
    date2 = input('비교할 두번째 날짜(YYYYMMDD)를 입력하세요: ')
    print(abs(date_count(date1)-date_count(date2)))

main()