"""
음수가 아닌 수들이 주어졌을 때 그 수들을 이어서 만들 수 있는 가장 큰 수를 구하시오.

예를 들어 [1,2,3]이 주어졌을 때 만들 수 있는 가장 큰 수는 321이고, [3, 30, 34, 5, 9] 가 주어지면 만들 수 있는 가장 큰 수는 9534330이다.
"""
"""
========================================================================
과제1. 아래에 입력이 num_list로 주어졌을 때, 그 수들을 이어서 만들 수 있는 가장 큰 수인 출력값을 구하시오. 
      - 조건 1. 입력된 숫자들은 음수가 아닌 자연수
      - num_list = [1, 2, 3] 
      - 출력값 : 321
========================================================================
"""

def make_largest_number(n):                 # 만들 수 있는 가장 큰수를 구하는 함수
    digit_list = n                          # digit list 생성
    result = ''                             # result 값 생성
    digit_list.sort()                       # digit_list 요소를 정렬
    digit_list.reverse()                    # digit_list 요소를 역순으로 배열
    for digit in digit_list:                # for 반복문
        result += str(digit)                # result에 문자열 digit 값을 추가
    return int(result)

num_list = list(map(int, input('num_list : ').split(',')))
print(make_largest_number(num_list))

"""
========================================================================
과제2. 아래에 입력이 num_list로 주어졌을 때, 그 수들을 이어서 만들 수 있는 가장 큰 수인 출력값을 구하시오. 
      - 조건 1. 입력된 숫자들은 음수가 아닌 자연수
      - 조건 2. 아래와 같은 입력값을 도출하시오. 
      - num_list = [3, 30, 34, 5, 9] 
      - 출력값 : 9,534,330
========================================================================
"""

from random import shuffle

def largest(L):
    i = 0
    ass = 0
    while i != 10000:
        temporary_value = "".join(str(x) for x in L)
        if int(temporary_value) >= int(ass):
            ass = int(temporary_value)
        shuffle(L)
        i += 1
    return ass

print(largest([3, 30, 34, 5, 9]))