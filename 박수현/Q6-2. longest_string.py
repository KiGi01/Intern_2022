'''
여기서의 “부분”은 LCS문제에서의 “부분”과는 다른 의미임을 명심하라.
nice라는 문자열이 있다면 이 문제에서의 부분문자열의 집합은 {‘’, n, i, c, e, ni, ic, ce, nic, nice}이다.
LCS문제에서의 “부분”에서는 nce도 하나의 부분문자열로 볼 수 있지만 이 문제에서는 부분문자열이 아니다.
(즉, 이 문제에서의 “부분”은 원래 문자열에서 일정 부분을 잘라낸 것이다.)
photography와 autograph 두 문자열이 있다고 할 때,
ph, grap, to 등의 부분문자열이 있으며, 이 중 최대의 길이를 갖는 부분문자열은 tograph이다.

입력
두 줄에 각각의 스트링이 주어진다. 각 스트링의 길이는 4000이하이다.
photography
autograph

출력
첫줄에 찾은 부분문자열의 길이, 둘째 줄에 가장 긴 공통의 부분문자열을 출력한다.
7
tograph
'''
"""
========================================================================
과제1. 입력된 문자열의 부분문자열을 구하시오. 
        - 조건1. 부분문자열은 입력된 문자열 안에 연속된 문자열을 의미한다.
        - 조건2. 부분문자열에는 공집합도 포함
        - input_string = 'nice'
        - 출력값 = ['','n','i','c','e','ni','ic','ce','nic','ice','nice']
========================================================================
"""

print_list = ['']                                       # print_list = 최종 출력값이 될 리스트
input_string = input('문자를 입력하세요 : ')             # input_string = 문자를 입력받기

for i in input_string:                                  # input_string을 한 글자씩 분해하여 최종 리스트에 추가
    print_list.append(i)
for j in range(len(input_string) - 1):                  # input_string을 두 글자씩 분해하여 최종 리스트에 추가
    print_list.append(input_string[j] + input_string[j + 1])
for x in range(len(input_string) - 2):                  # input_string을 세 글자씩 분해하여 최종 리스트에 추가
    print_list.append(input_string[x] + input_string[x + 1] + input_string[x + 2])
print_list.append(input_string)                         # input_string을 최종 리스트에 추가

print(print_list)                                       # 최종 리스트 출력
print()

"""
========================================================================
과제2. 아래와 같이 두 문자열이 입력되었을 때, 두 문자열의 공통된 부분문자열 중 가장 긴 부분문자열의 길이와 실제값을 출력하시오.
        - 조건1. 부분문자열은 입력된 문자열 안에 연속된 문자열을 의미한다.
        - 조건2. 부분문자열에는 공집합도 포함
        - input_string1 = 'photography'
        - input_string2 = 'autograph'
        - 출력값 = 7 tograph
========================================================================
"""

# 부분 문자열을 구하는 프로그램 정의
def is_string_list(input_string):
    input_list = []                                     # input_list = 부분 문자열의 리스트가 될 빈 리스트
    for i in range(len(input_string)):                  # input_string 길이만큼 다음 행위 반복
        for j in range(i, len(input_string) + 1):       # i부터 input_string 길이만큼 다음 행위 반복
            input_list.append(input_string[i:j])        # input_string[i:j] 해당 값을 부분 문자열의 리스트에 추가

    return list(set(input_list))                        # 중복되는 값을 제외한 부분 문자열의 리스트를 반환

# 공통된 부분 문자열 중 가장 긴 부분 문자열과 그 길이를 구하는 프로그램 정의
def is_string_same(input_list_a, input_list_b):
    same_list = []                                      # same_list = 공통된 부분 문자열의 리스트가 될 빈 리스트
    for i in input_list_a:                              # input_list_a와 input_list_b를 하나씩 비교
        for j in input_list_b:
            if i == j:                                  # 만약 i와 j가 같다면, same_list에 추가
                same_list.append(i)
    
    max_string = max(same_list, key = len)              # max_string = same_list 중 가장 긴 문자열
    print(len(max_string), max_string)                  # 부분 문자열의 길이와 부분 문자열 출력

if __name__ == '__main__':
    # input_string a, input_string_b = 문자 각각 입력받기
    input_string_a = input('첫 번째 문자를 입력하세요 : ')
    input_string_b = input('두 번째 문자를 입력하세요 : ')

    # 만약 범위에 벗어난다면, 예외 발생시키기
    if 4000 < len(input_string_a) or 4000 < len(input_string_b):
        raise Exception('잘못 입력했습니다. (문자의 길이는 4,000 이하)')

    # 부분 문자열을 구한 후, 가장 긴 공통된 부분 문자열을 구하는 프로그램 실행
    is_string_same(is_string_list(input_string_a), is_string_list(input_string_b))