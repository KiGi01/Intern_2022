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

def days_month(month):                          # 월(날짜수) 구하는 함수
    return  [0,31,28,31,30,31,30,31,31,30,31,30,31][month]

def days_year(year):                            # 연도(날짜수) 구하는 함수
    if year%400==0:return 366                   # year을 400으로 나눴을 때 나머지가 0이면(윤년일 경우), 366 반환
    elif year%100==0:return 365                 # year을 100으로 나눴을 때 나머지가 0이면(평년일 경우), 365 반환
    elif year%4==0:return 366                   # year을 4로 나눴을 때 나머지가 0이면(윤년일 경우), 366 반환
    return 365                                  # 이외 365 반환

def convert(yyyymmdd):
    res = 0
    ymd = str(yyyymmdd)
    y = int(ymd[:-4])                           # 'yyyy'mmdd
    m = int(ymd[-4:-2])                         # yyyy'mm'dd
    d = int(ymd[-2:])                           # yyyymm'dd'
    for i in range(1900,y):
        res += days_year(i)                     # 1900부터 y-1까지 i값 반복, res에 days_year(i)값 추가
    for i in range(1,m):
        res += days_month(i)                    # 1부터 m까지 i값 반복, res에 days_month(i)값 추가
    res += d                                    # res에 d값 추가
    return res                                  # res값 반환
    
def subdate(a,b):
    return abs(convert(a)-convert(b))           # abs: 절대값 구하는 함수


first = input('first = ')
second = input('second = ')

print(subdate(first, second))

"""
========================================================================
과제2. 아래에 입력된 두 날짜 간의 차이를 구하는 프로그램을 작성하시오. 
      - 조건 : 날짜 차이를 계산하는 라이브러리 사용 금지
      - first = 20070301
      - second = 20070515
      - 출력값 : 75
========================================================================
"""

def days_month(month):                          # 월(날짜수) 구하는 함수
    return  [0,31,28,31,30,31,30,31,31,30,31,30,31][month]

def days_year(year):                            # 연도(날짜수) 구하는 함수
    if year%400==0:return 366                   # year을 400으로 나눴을 때 나머지가 0이면(평년일 경우), 366 반환
    elif year%100==0:return 365                 # year을 100으로 나눴을 때 나머지가 0이면(윤년일 경우), 365 반환
    elif year%4==0:return 366                   # year을 4로 나눴을 때 나머지가 0이면(평년일 경우), 366 반환
    return 365                                  # 이외 365 반환

def convert(yyyymmdd):
    res = 0
    ymd = str(yyyymmdd)
    y = int(ymd[:-4])                           # 'yyyy'mmdd
    m = int(ymd[-4:-2])                         # yyyy'mm'dd
    d = int(ymd[-2:])                           # yyyymm'dd'
    for i in range(1900,y):
        res += days_year(i)                     # 1900부터 y-1까지 i값 반복, res에 days_year(i)값 추가
    for i in range(1,m):
        res += days_month(i)                    # 1부터 m까지 i값 반복, res에 days_month(i)값 추가
    res += d                                    # res에 d값 추가
    return res                                  # res값 반환
    
def subdate(a,b):
    return abs(convert(a)-convert(b))           # abs: 절대값 구하는 함수


first = input('first = ')
second = input('second = ')

print(subdate(first, second))