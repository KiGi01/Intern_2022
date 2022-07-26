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

# count_num = 개수 세기 (시작은 0)
count_num = 0

for i in range(1, 10001):                          # 1부터 10,000까지 다음 행위 반복
    if i % 2 != 0 and i % 5 != 0:                  # 만약 2와 5로 나누어 떨어지지 않는다면, 카운트
        count_num += 1

print(count_num)                                   # 2나 5로 나누어 떨어지지 않는 정수의 개수 출력
print()

"""
=============================================================================
과제 2. input의 배수 중에서 모든 자리 숫자가 1로 이루어진 가장 작은 수와 그 수의 자리수를 구하시오
        - input =  7
        - output = 111111 6
=============================================================================
"""

# 모든 자리 숫자가 1로 이루어진 최소 배수와 자리수를 구하는 프로그램 정의 (변수는 input_num)
def is_ones_count(input_num):
    ones_num = '1'                                 # ones_num = 1로만 이루어진 수 (시작은 1)

    for i in range(10000):                         # (임의로 지정한) 10,000번 동안 다음 행위 반복
        if int(ones_num) % input_num == 0:         # 만약 ones_num이 input_num의 배수라면, 그 수와 자리수 출력 후 종료
            print(ones_num, len(ones_num))
            break
        else:                                      # 배수가 아니라면(나누어 떨어지지 않는다면), ones_num + '1'
            ones_num += '1'                        # 1 -> 11 -> 111 -> 1111 -> 11111 -> 111111 등으로 변화

if __name__ == '__main__':
    input_num = int(input('정수를 입력하세요 : '))  # input_num 입력받을 때, 이를 숫자(정수)로 변환
    # 만약 잘못 입력했다면, 예외 발생시키기
    if input_num % 2 == 0 or input_num % 5 == 0:
        raise Exception('잘못 입력했습니다. (2나 5로 떨어지지 않는 정수)')
    if not 1 <= input_num <= 10000:
        raise Exception('잘못 입력했습니다. (1 이상 10,000 이하의 정수)')
    
    is_ones_count(input_num)                        # is_ones_count 실행
    print()

"""
=============================================================================
과제 3. input의 배수 중에서 모든 자리 숫자가 1로 이루어진 가장 작은 수의 자리수를 구하시오
        - input =  3, 7, 9901
        - output = 3, 6, 12
=============================================================================
"""

# 모든 자리 숫자가 1로 이루어진 최소 배수의 자리수를 구하는 프로그램 정의 (변수는 input_num_zip)
def is_ones(input_num_zip):
    # is_ones_zip = 1로만 이루어진 최소 배수의 자리수들의 리스트가 될 빈 리스트
    is_ones_zip = []
    
    for input_num in input_num_zip:                # input_num_zip을 하나씩 분해
    # 만약 잘못 입력했다면, 예외 발생시키기
        if input_num % 2 == 0 or input_num % 5 == 0:
            raise Exception('잘못 입력했습니다. (2나 5로 떨어지지 않는 정수)')
        if not 1 <= input_num <= 10000:
            raise Exception('잘못 입력했습니다. (1 이상 10,000 이하의 정수)')
    
        ones_num = '1'                             # ones_num = 1로만 이루어진 수 (시작은 1)

        for i in range(10000):                     # (임의로 지정한) 10,000번 동안 다음 행위 반복
            if int(ones_num) % input_num == 0:     # 만약 ones_num이 input_num의 배수라면, 그 수의 자리수를 리스트에 추가 후 종료
                is_ones_zip.append(len(ones_num))
                break
            else:                                  # 배수가 아니라면(나누어 떨어지지 않는다면), ones_num + '1'
                ones_num += '1'
    
    print(', '.join(map(str, is_ones_zip)))        # 1로만 이루어진 최소 배수의 자리수들의 리스트 출력

if __name__ == '__main__':
    # input_num_zip 입력받을 때, 이를 ', ' 기준으로 분해 후 숫자(정수)로 변환
    input_num_zip = list(map(int, input('정수를 입력하세요 : ').split(', ')))
       
    is_ones(input_num_zip)                         # is_ones 실행