'''
아시다시피, 데이터는 컴퓨터에 이진수 형태로 저장됩니다. 우리가 토론할 문제는 양의 정수와 이 수의 이진 형태입니다.
양의 정수 I가 주어지면, 당신이 할 일은 I보다 큰 수 중 가장 작은 수 J를 찾습니다.
I의 이진수 형태에서의 1의 개수와 J의 이진수 형태에서의 1의 개수는 일치합니다.
예를들어, "78"이 주어지면, 여러분은 "1001110"과 같은 이진수 형태로 쓸 수 있습니다.
이 이진수는 4개의 1을 가지고 있습니다. "1001110" 보다 크고 4개의 1을 포함하는 가장 작은 정수는 "1010011"입니다.
출력값은 "83"이 되어야 합니다.

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

# '{0:b}'.format(n) : 정수를 이진수로 바꾸는 코드
# 정수를 이진수로 바꾸는 프로그램 정의
def is_ten_to_two(input_num):
    start_num = input_num                                               # start_num = input_num 복사
    two_num = ''                                                        # two_num = 이진수가 될 빈 문자열

    while start_num:                                                    # start_num이 참이라면 다음 행위 반복
        two_num += str(start_num % 2)                                   # start_num 나누기 2의 나머지를 문자로 변환하여 문자열에 추가
        start_num = start_num // 2                                      # start_num 나누기 2의 정수인 몫으로 start_num 업데이트
    
    return two_num[::-1]                                                # two_num을 뒤집어서 반환

# 이진수가 포함하고 있는 1의 개수를 구하는 프로그램 정의
def is_one_count(input_num):
    return is_ten_to_two(input_num).count('1')                          # 정수를 이진수로 바꾸는 프로그램을 실행한 후 '1'의 개수 세어 반환

# 이진수로 변환했을 때 1의 개수가 같은 수 중 가장 작은 정수를 구하는 프로그램 정의
def is_the_smallest(input_num):
    print_num = input_num                                               # print_num = input_num 복사
    for i in range(1000):                                               # (임의로 지정한) 1000번 다음 행위 반복
        print_num += 1                                                  # print_num에 1 더하기

        if is_one_count(input_num) == is_one_count(print_num):          # 1의 개수를 구하는 프로그램을 실행하여 만약 input_num과 print_num의 1의 개수가 같다면,
            print(f'2진수 : {is_ten_to_two(print_num)}')                # 이진수로 바꾸는 프로그램을 실행하여 print_num의 2진수 출력
            print(f'10진수 : {print_num}')                              # print_num 출력
            break

if __name__ == '__main__':
    # input_num = 숫자를 입력받을 때, 숫자(정수)로 변환
    input_num = int(input('숫자를 입력하세요 : '))

    # 만약 범위를 벗어났다면, 예외 발생시키기
    if not 1 <= input_num <= 1000000:
        raise Exception('잘못 입력했습니다. (1 <= input_num <= 1,000,000)')

    # 이진수로 변환했을 때 1의 개수가 같은 수 중 가장 작은 정수를 구하는 프로그램 실행
    is_the_smallest(input_num)