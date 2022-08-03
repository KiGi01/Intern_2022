"""
음수가 아닌 수들이 주어졌을 때 그 수들을 이어서 만들 수 있는 가장 큰 수를 구하시오.
예를 들어 [1,2,3]이 주어졌을 때 만들 수 있는 가장 큰 수는 321이고, [3, 30, 34, 5, 9] 가 주어지면 만들 수 있는 가장 큰 수는 9534330이다.
"""
"""
========================================================================
과제1. 아래에 입력이 num_list로 주어졌을 때, 그 수들을 이어서 만들 수 있는 가장 큰 수인 출력값을 구하시오. 
      - 조건 1. 입력된 숫자들은 음수가 아닌 자연수
      - num_list = [1, 2, 3] 
      - 출력값 : 321
========================================================================
"""

number_list = [1, 2, 3]
lst = []
for i in range(len(number_list)-1): #리스트 길이까지 돌린다.
    if i == 0: #i가 0이라면
        if int(str(number_list[i]) + str(number_list[i+1])) > int(str(number_list[i+1]) + str(number_list[i])): #각 조합한 글자를 비교, 첫번째가 더 숫자가 높다면
            lst.append(number_list[i]) #첫번째 숫자 중 첫번째를 먼저 넣고
            lst.append(number_list[i+1]) #그 다음의 숫자를 넣음
        else: #두번째 숫자가 더 높다면
            lst.append(number_list[i+1]) #두번째 숫자 중 두번째를 먼저 넣고
            lst.append(number_list[i]) #그 다음의 숫자를 넣음
    else: #i가 0이 아니라면
        for j in range(len(lst)): #리스트 길이까지 돌린다.
            if int(str(number_list[i+1]) + str(lst[j])) > int(str(lst[j]) + str(number_list[i+1])):
                lst.insert(j, number_list[i+1]) #리스트의 j번째 위치에 값 number_list[i+1]를 삽입
                break
            elif j == len(lst)-1:
                  lst.append(number_list[i+1]) #리스트에 넣음

print(''.join(str(i) for i in lst)) #빈칸없이 숫자 출력

"""
========================================================================
과제2. 아래에 입력이 num_list로 주어졌을 때, 그 수들을 이어서 만들 수 있는 가장 큰 수인 출력값을 구하시오. 
      - 조건 1. 입력된 숫자들은 음수가 아닌 자연수
      - 조건 2. 아래와 같은 입력값을 도출하시오. 
      - num_list = [3, 30, 34, 5, 9] 
      - 출력값 : 9,534,330
========================================================================
"""

number_list = [3, 30, 34, 5, 9]
lst = []
for i in range(len(number_list)-1): #리스트 길이까지 돌린다.
    if i == 0: #i가 0이라면
        if int(str(number_list[i]) + str(number_list[i+1])) > int(str(number_list[i+1]) + str(number_list[i])): #각 조합한 글자를 비교, 첫번째가 더 숫자가 높다면
            lst.append(number_list[i]) #첫번째 숫자 중 첫번째를 먼저 넣고
            lst.append(number_list[i+1]) #그 다음의 숫자를 넣음
        else: #두번째 숫자가 더 높다면
            lst.append(number_list[i+1]) #두번째 숫자 중 두번째를 먼저 넣고
            lst.append(number_list[i]) #그 다음의 숫자를 넣음
    else: #i가 0이 아니라면
        for j in range(len(lst)): #리스트 길이까지 돌린다.
            if int(str(number_list[i+1]) + str(lst[j])) > int(str(lst[j]) + str(number_list[i+1])):
                lst.insert(j, number_list[i+1]) #리스트의 j번째 위치에 값 number_list[i+1]를 삽입
                break
            elif j == len(lst)-1:
                  lst.append(number_list[i+1]) #리스트에 넣음

print(''.join(str(i) for i in lst)) #빈칸없이 숫자 출력