"""
숫자 형태의 문자열을 콤마가 포함된 금액 표기식 문자열로 바꾸어주는 프로그램을 작성하시오.

※ 단, 프로그래밍 언어에서 지원하는 금액변환 라이브러리는 사용하지 말것

예)

숫자	금액
1000	1,000
20000000	20,000,000
-3245.24	-3,245.24
"""
"""
========================================================================
과제1. 아래와 같은 숫자 형태의 문자열을 콤마가 포함된 금액 표기식 문자열로 바꾸어주는 프로그램을 작성하시오.
      - 조건 : 파이썬의 금액변환 라이브러리 사용금지
      - money = 1000
      - 출력값 = 1,000
========================================================================
"""
money = input('금액 입력: ')
print(money[:-3] + ',' + money[-3:]) #뒤에서 세번째 숫자 앞에 콤마 추가

"""
========================================================================
과제2. 아래와 같은 숫자 형태의 문자열을 콤마가 포함된 금액 표기식 문자열로 바꾸어주는 프로그램을 작성하시오.
      - 조건 : 파이썬의 금액변환 라이브러리 사용금지
      - money = -3245.24
      - 출력값 = -3,245.24
========================================================================
"""

def comma(n):
      if len(n) < 4:  #3자리 이하 금액일 경우 그대로 결과로 반환
            return n
      if n[0] == "-":    
            return "-" + comma(n[1:])  #재귀호출한 결과값에 '-' 추가하여 반환
      if "." in n:    
            return comma(n[:n.find(".")]) + n[n.find("."):] #처음부터 소수점 전까지의 수+소수점부터 끝까지
      if len(n) >= 4:
            return comma(n[:-3]) + ',' + n[-3:] #뒤에서 세번째 숫자 앞에 콤마 추가

n = input("금액 입력: ")
print(comma(n))