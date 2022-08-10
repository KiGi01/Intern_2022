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

input_String = 'nice' #입력할 문자열
lst = [] #빈리스트 생성

for i in range(0, len(input_String)): #첫번째 문자도 포함하기 위해 0부터 시작하는 반복문
    if i == 0: #만약 0이라면
        blank_input_string1 = '' #부분문자열인 빈칸을 넣는다.
        first_input_String1 = input_String[i] #알파벳이 하나가 필요한 부분문자열을 넣는다.
        first_input_String2 = input_String[i] + input_String[i+1] #알파벳이 두개가 필요한 부분문자열을 넣는다.
        first_input_String3 = input_String[i] + input_String[i+1] +input_String[i+2] #알파벳이 세개가 필요한 부분문자열을 넣는다.
        first_input_String4 = input_String[i] + input_String[i+1] +input_String[i+2] + input_String[i+3] #단어 자체가 부분문자열을 넣는다.
        lst.append(blank_input_string1) #리스트에 넣는다.
        lst.append(first_input_String1)
        lst.append(first_input_String2)
        lst.append(first_input_String3)
        lst.append(first_input_String4)
    if i == 1:
        second_input_String1 = input_String[i]
        second_input_String2 = input_String[i] + input_String[i+1]
        second_input_String3 = input_String[i] + input_String[i+1] +input_String[i+2]
        lst.append(second_input_String1)
        lst.append(second_input_String2)
        lst.append(second_input_String3)
    if i == 2:
        third_input_String1 = input_String[i]
        third_input_String2 = input_String[i] + input_String[i+1]
        lst.append(third_input_String1)
        lst.append(third_input_String2)
    if i == 3:
        fourth_input_String1 = input_String[i]
        lst.append(fourth_input_String1)

lst.sort(key= len) #문자길이를 순서로 재정렬한다.
print(lst)
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

input_string1 = "photography"
input_string2 = "autograph"

a_list = [] # a 문자열 리스트
b_list = [] # b 문자열 리스트
c_list = [] # a,b 문자열 비교하여 동일 부분문자열 리스트
d_list =[] # 가장 큰 문자 개수
temp_list = []
for i in range (0, len(input_string1)): #숫자가 하나씩 늘면서 input_string1 첫번째 문자의 문자열을 만든다. (0~1번째, 0~2번쨰, 0~3번째..., 공집합까지)
    for k in range (1,len(input_string1)):
        a_list.append(input_string1[i:k])

for i in range (0, len(input_string1)): #숫자가 하나씩 늘면서 input_string2 두번째 문자의 문자열을 만든다. (0~1번째, 0~2번쨰, 0~3번째..., 공집합까지)
    for k in range (1,len(input_string1)):
        b_list.append(input_string2[i:k])

for i in range (0, len(a_list)):
    for k in range (1,len(b_list)):
        if(a_list[i] == b_list[k] and b_list[k] != ""): #공집합이 아니면서 부분문자열이 동일한 것을 리스트에 넣는다.
            c_list.append(b_list[k])

for i in range (0, len(c_list)):
    d_list.append(int(len(c_list[i]))) #문자열 크기 구하기
    temp_list.append(int(len(c_list[i]))) #정렬하기전 문자 구하기

d_list.sort() #문자열크기로 정렬
c_index=temp_list.index(d_list[-1]) #가장 큰 문자의 index 확인
print(d_list[-1], c_list[c_index]) # 가장 큰 문자의 개수와 가장 큰 문자열 출력