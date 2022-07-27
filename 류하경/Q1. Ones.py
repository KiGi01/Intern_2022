"""
2나 5로 나누어 떨어지지 않는 1 이상 10,000 이하의 정수 n이 주어졌는데, n의 배수 중에는 10진수로 표기했을 때 모든 자리 숫자가 1인 것이 있다.
그러한 n의 배수 중에서 가장 작은 것은 몇 자리 수일까?

Sample Input
3
7
9901

Sample Output
3
6
12
"""

"""
=============================================================================
과제 1. 2나 5로 나누어 떨어지지 않는 1 이상 10,000 이하의 정수는 모두 몇 개인지 구하시오
       - output : 4000
=============================================================================

"""
# n = int(input())
# if 1 <= n <= 10000 and n % 2 != 0 and n % 5 != 0:

i_list = []
for i in range(1, 10001):
       if i % 2 != 0 and i % 5 != 0:
              i_list.append(i)
len(i_list)


"""
=============================================================================
과제 2. input의 배수 중에서 모든 자리 숫자가 1로 이루어진 가장 작은 수와 그 수의 자리수를 구하시오
       - input =  7
       - output = 111111 6
=============================================================================
"""

# 예시
# n = 3
# r = 1
## '1'*1 % 3은 1 % 3
## '1'*2 % 3은 11 % 3
## '1'*3 % 3은 111 % 3, 111 % 3 == 0

def ones(n):
       r = 1
       while True:
              number_w_one = int('1' * r)
              if number_w_one % n == 0:
                     return number_w_one, r
              elif number_w_one % n != 0:
                     r += 1
n = int(input())
print(ones(n))

"""
=============================================================================
과제 3. input의 배수 중에서 모든 자리 숫자가 1로 이루어진 가장 작은 수의 자리수를 구하시오
       - input =  3, 7, 9901
       - output = 3, 6, 12
=============================================================================
"""
def ones(n):
       r = 1
       while True:
              number_w_one = int('1' * r)
              if number_w_one % n == 0:
                     return r
              elif number_w_one % n != 0:
                     r += 1
n = int(input())
print(ones(n))