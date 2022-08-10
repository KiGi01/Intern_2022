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
def all_substring(input_string):
    str_length = len(input_string) #4
    result = ['']
    num=0
    
    while num != str_length:
        for i,j in zip(range(0, str_length-num), range(1+num, str_length+1)):
            result.append(input_string[i:j])
#        print(result)
        num +=1
    
    return result
    

input_string = 'nice'
result  =all_substring(input_string)
"""
0:1    #1개씩
1:2
2:3
3:4

0:2    #2개씩
1:3
2:4

0:3    #3개씩
1:4

0:4    #4개씩
"""


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
def longest_string(input_string1, input_string2):
    sub1 = all_substring(input_string1) 
    sub2 = all_substring(input_string2) 
    sub_intersection  =set(sub1).intersection(sub2)
    result = {}
    for i in sub_intersection:
        result[i]=len(i)
        print(result)
    
    return print( result[max(result.keys())], max(result.keys()) )


input_string1 = 'photography'
input_string2 = 'autograph'
longest_string(input_string1, input_string2)
