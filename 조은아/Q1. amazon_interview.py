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
      - input_list = ['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6']
      - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']
========================================================================
"""
import numpy as np

input_list = ['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6']
input_list = np.sort(input_list)
f1 = 'a'
list_a, list_b, result = [],[],[]
for i in input_list:    #a1
    if f1==i[0]:        #a
      list_a.append(i)
    else:
      list_b.append(i)

for i in range(len(list_a)):    #range(6)
    result.append(list_a[i])    #a1
    result.append(list_b[i])    #b1

print(result)

"""
========================================================================
과제2. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
      - 조건1. 람다식 필수적 사용
      - input_list = ['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6']
      - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']
========================================================================
"""
input_list = ['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6']
input_list = np.sort(input_list)
f1 = 'a'
list_a, list_b, result = [],[],[]
make_list = lambda x: list_a.append(x) if x[0] == f1 else list_b.append(x)
for i in input_list:
    make_list(i)


for i in range(len(list_a)):
    result.append(list_a[i])
    result.append(list_b[i])

print(result)

"""
========================================================================
과제3. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
      - 조건1. 람다식 사용 X
      - input_list = ['b1','a2','b3','a4','b5','a6','a1','b2','b4','a3','a5','b6']
      - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']
========================================================================
"""
import numpy as np

input_list = ['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6']
input_list = np.sort(input_list)
f1 = 'a'
list_a, list_b, result = [],[],[]
for i in input_list:    #a1
    if f1==i[0]:        #a
      list_a.append(i)
    else:
      list_b.append(i)

for i in range(len(list_a)):    #range(6)
    result.append(list_a[i])    #a1
    result.append(list_b[i])    #b1

print(result)

"""
========================================================================
과제4. 아래와 같은 입력값을 넣을 경우 출력값을 도출하는 알고리즘을 구성하시오.  
      - 조건1. 람다식 필수적 사용
      - input_list = ['b1','a2','b3','a4','b5','a6','a1','b2','b4','a3','a5','b6']
      - 출력값 = ['a1','b1','a2','b2','a3','b3','a4','b4','a5','b5','a6','b6']
========================================================================
"""
input_list = ['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6']
input_list = np.sort(input_list)
f1 = 'a'
list_a, list_b, result = [],[],[]
make_list = lambda x: list_a.append(x) if x[0] == f1 else list_b.append(x)
for i in input_list:
    make_list(i)


for i in range(len(list_a)):
    result.append(list_a[i])
    result.append(list_b[i])

print(result)