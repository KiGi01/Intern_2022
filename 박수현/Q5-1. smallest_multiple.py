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

# [Done] exited with code=0 in 27.285 seconds

# 최소공배수를 구하는 프로그램 정의
def is_smallest_multiple(start_num, end_num):
    ex_num = end_num                                    # ex_num = end_num의 배수 (시작은 곱하기 1)

    while True:                                         # 다음 행위 무한 반복
        for i in range(start_num, end_num + 1):         # start_num부터 end_num까지 다음 행위 반복
            if ex_num % i != 0:                         # 만약 나누어 떨어지지 않는다면, 중단
                break
        if i == end_num:                                # 만약 범위의 모든 값에 나누어 떨어졌다면, 해당 값 출력
            print('{:,}'.format(ex_num))
            break

        ex_num += end_num                               # ex_num에 end_num 더하기 (end_num의 배수가 되기 위해)

if __name__ == '__main__':
    # start_num, end_num = 구하고자 하는 범위의 시작, 끝 (','을 기준으로 분해한 후 숫자(정수)로 변환)
    start_num, end_num = map(int, input('구하고자 하는 범위의 시작과 끝을 입력하세요 : ').split(','))

    is_smallest_multiple(start_num, end_num)            # 최소공배수를 구하는 프로그램 실행