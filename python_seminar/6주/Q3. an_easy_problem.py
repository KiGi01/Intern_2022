'''
아시다시피, 데이터는 컴퓨터에 이진수 형태로 저장됩니다. 우리가 토론할 문제는 양의 정수와 이 수의 이진 형태입니다.

양의 정수 I가 주어지면, 당신이 할 일은 I보다 큰 수 중 가장 작은 수 J를 찾습니다. I의 이진수 형태에서의 1의 개수와 J의 이진수 형태에서의 1의 개수는 일치합니다.

예를들어, "78"이 주어지면, 여러분은 "1001110"과 같은 이진수 형태로 쓸 수 있습니다. 이 이진수는 4개의 1을 가지고 있습니다. "1001110" 보다 크고 4개의 1을 포함하는 가장 작은 정수는 "1010011"입니다. 출력값은 "83"이 되어야 합니다.

Input

각 줄에 한개의 정수를 입력할 수 있습니다. (1 <= I <= 1000000)
0이 나오면 입력을 종료합니다. 이 줄은 작업할 필요 없습니다.

Output

각 줄에 한개의 정수를 출력하면 됩니다.

Sample Input

1
2
3
4
78
0
Sample Output

2
4
5
8
83
'''

"""
========================================================================
과제1. 주어진 입력 수의 이진수와 동일하게 1을 가진 가장 작은 수 j와 j의 이진수 값을 출력하시오. 
      - 조건1. j는 주어진 입력 수보단 커야한다. 
      - input_num = 78
      - 출력값(2진수) : 1010011
      - 출력값(10진수) : 83
========================================================================
"""