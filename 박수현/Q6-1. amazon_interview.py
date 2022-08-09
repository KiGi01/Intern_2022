'''
다음과 같은 형태의 배열을
[a1,a2,a3...,an,b1,b2...bn]

다음과 같은 형태로 바꾸시오
[a1,b1,a2,b2.....an,bn]
'''
"""
========================================================================
과제1. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
        - 조건1. 람다식 사용 X
        - input_list = [a1, a2, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6]
        - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']
========================================================================
"""

final_list = []                                                 # final_list = 최종 출력값이 될 빈 리스트
input_list = input('리스트를 입력하세요 : ').split(', ')         # input_list = 리스트를 입력받을 때, ', '을 기준으로 분해 

a_list = input_list[:input_list.index('b1')]                    # a_list = input_list 중 an에 해당하는 값에 대한 리스트
b_list = input_list[input_list.index('b1'):]                    # b_list = input_list 중 bn에 해당하는 값에 대한 리스트

for i in range(len(a_list)):                                    # a_list만큼 다음 행위 반복
    final_list.append(a_list[i])                                # 최종 리스트에 a_list[i] 해당 값 추기
    final_list.append(b_list[i])                                # 최종 리스트에 b_list[i] 해당 값 추가

print(final_list)                                               # 최종 리스트 출력
print()

"""
========================================================================
과제2. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
        - 조건1. 람다식 필수적 사용
        - input_list = [a1, a2, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6]
        - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']
========================================================================
"""

input_list = input('리스트를 입력하세요 : ').split(', ')         # input_list = 리스트를 입력받을 때, ', '을 기준으로 분해 

final_list = sorted(input_list, key = lambda x: x[1])           # final_list = input_list를 오름차순으로 정렬할 떄, 각 값의 1번째 자리를 기준으로 정렬

print(final_list)                                               # 최종 리스트 출력
print()

"""
========================================================================
과제3. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
        - 조건1. 람다식 사용 X
        - input_list = [b1, a2, b3, a4, b5, a6, a1, b2, b4, a3, a5, b6]
        - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']
========================================================================
"""

final_list = []                                                 # final_list = 최종 출력값이 될 빈 리스트
input_list = input('리스트를 입력하세요 : ').split(', ')         # input_list = 리스트를 입력받을 때, ', '을 기준으로 분해 

input_list.sort()                                               # input_list 오름차순으로 정렬
a_list = input_list[:input_list.index('b1')]                    # a_list = input_list 중 an에 해당하는 값에 대한 리스트
b_list = input_list[input_list.index('b1'):]                    # b_list = input_list 중 bn에 해당하는 값에 대한 리스트

for i in range(len(a_list)):                                    # a_list만큼 다음 행위 반복
    final_list.append(a_list[i])                                # 최종 리스트에 a_list[i] 해당 값 추기
    final_list.append(b_list[i])                                # 최종 리스트에 b_list[i] 해당 값 추가

print(final_list)                                               # 최종 리스트 출력
print()

"""
========================================================================
과제4. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
        - 조건1. 람다식 필수적 사용
        - input_list = [b1, a2, b3, a4, b5, a6, a1, b2, b4, a3, a5, b6]
        - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']
========================================================================
"""

input_list = input('리스트를 입력하세요 : ').split(', ')         # input_list = 리스트를 입력받을 때, ', '을 기준으로 분해 

input_list.sort()                                               # input_list 오름차순으로 정렬
final_list = sorted(input_list, key = lambda x: x[1])           # final_list = input_list를 오름차순으로 정렬할 떄, 각 값의 1번째 자리를 기준으로 정렬

print(final_list)                                               # 최종 리스트 출력