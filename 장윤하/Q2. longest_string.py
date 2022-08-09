'''
여기서의 “부분”은 LCS문제에서의 “부분”과는 다른 의미임을 명심하라. nice라는 문자열이 있다면 이 문제에서의 부분문자열의 집합은 {‘’, n, i, c, e, ni, ic, ce, nic, nice}이다.

LCS문제에서의 “부분”에서는 nce도 하나의 부분문자열로 볼 수 있지만 이 문제에서는 부분문자열이 아니다. (즉, 이 문제에서의 “부분”은 원래 문자열에서 일정 부분을 잘라낸 것이다.)

photography와 autograph 두 문자열이 있다고 할 때, ph, grap, to 등의 부분문자열이 있으며, 이 중 최대의 길이를 갖는 부분문자열은 tograph이다.

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
def set_string(input_string):
    st = input_string
    output_string = ['']              # 공집합 추가
    length = len(st) + 1                          # 리스트 길이에 1을 더한 수를 저장 (리스트 길이만큼 반복하기 위해)
    # #(예: input_string [0:1] [1:2] [2:3] [3:4]/ [0:2] [1:3] [2:4]/ [0:3] [1:4]/ [0:4]) 추가 ##
    for i in range(1, length):                              # i는 1 ~ 4
        for j in range(0, length - i):                      # j는 위 문자열의 범위에서 시작 범위를 의미  --- 부분문자열 각 자리수마다 0부터 5 - i - 1까지
            output_string.append(st[j:(j + i)])             # input_string의 j번째 부터 j + i - 1번쨰 자리까지의 문자열을 리스트에 추가
    return output_string

if __name__ == '__main__':
    input_string = input("문자열을 입력하세요: ")
    print(set_string(input_string))

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
input_string = input("문자열1을 입력하세요: ")
string1_set = set_string(input_string)   # 문자열1의 부분문자열 집합

input_string = input("문자열2를 입력하세요: ")
string2_set = set_string(input_string)   # 문자열2의 부분문자열 집합

min_str = min([string1_set, string2_set], key=len)  # 길이가 더 짧은 집합 저장
max_str = max([string1_set, string2_set], key=len)  # 길이가 더 긴 집합 저장
multi_lst = []     # 공통된 부분문자열을 저장할 리스트 생성

for i in min_str:                   # 짧은 문자열 반복
    if i in max_str:                # 해당 문자열이 긴 집합에 포함되는 경우
        multi_lst.append(i)         # 해당 문자열을 리스트에 저장
print(len(max(multi_lst, key = len)), max(multi_lst, key = len))   # 공통 문자열 중 길이가 긴 문자열의 길이과 해당 문자열 출력

