"""

1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.

그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?
"""
"""
========================================================================
과제1. 아래 입력 값의 범위의 어떤 수로도 나누어 떨어지는 수 중 가장 작은 수를 구하시오.
      - num_range = [1,20]
      - 출력값 : 232,792,560
========================================================================
"""

import functools                    # functools 모듈 가져오기

def gcd(x, y):                      # 최대공약수 구하는 함수(유클리드 호제법 사용)
    if y == 0: return x             # y가 0일 경우, x값 반환 
    else: return gcd(y, x%y)        # 아닐경우, gcd(y, x%y)

def lcm(x, y):                      # 최소공배수 구하는 함수
    return int(x * y / gcd(x, y)) 

a, b = map(int, input('num_range : ').split(','))
output = functools.reduce(lambda x, y: lcm(x, y), [a for a in range(a, b)])
print(format(output, ','))

# reduce(함수, 시퀀스): 인수를 두개 받는 함수와 시퀀스 자료형을 인수로 받아, 시퀀스 요소의 왼쪽부터 차례대로 처음부터 긑까지 입력받은 함수를 실행시키는 함수
# lambda: 함수를 일시적으로 만들어서 사용
# 예) reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])는 ((((1+2)+3)+4)+5)
'''
최대공약수를 구하는 유클리드 호제법

a를 b로 나눈 나머지를 r이라고 했을 때, gcd(a,b)=gcd(b,r)과 같다.
r이 0이면, 그때 b가 최대공약수이다.

'''
'''
a: 1
b: 20

x:1, y:2
lambda: 2

x:2, y:3
lambda:6

x:6, y;4
lambda:12

x:12, y:5
lambda:60

x:60, y:6
lambda:60

x:60, y:7
lambda:420

x:420, y:8
lambda:820

x:820, y:9
lambda:2520

x:2520, y:10
lambda:2520

x:2520, y:11
lambda:27720

x:27720, y:12
lambda:27720

x:27720, y:13
lambda:360360

x:360360, y:14
lambda:360360
x:360360, y:15
lambda:360360

x:360360, y:16
lambda:720720

x:720720, y:17
lambda:12252240

x:12252240, y:18
lambda:12252240

x:12252240, y:19
lambda: 232792560
'''
