"""
-----------------  Question  -----------------
A씨는 두 개의 버전을 비교하는 프로그램을 작성해야 한다.
버전은 다음처럼 "." 으로 구분된 문자열이다.
두 개의 버전을 비교하는 프로그램을 작성하시오.
ex) - 0.0.2 > 0.0.1
    - 1.0.10 > 1.0.3
    - 1.2.0 > 1.1.99
    - 1.1 > 1.0.1
----------------------------------------------
"""
# 과제 1
## input_1 = "1.0.2"
## input_2 = "0.9.1"
## 출력 : 1.0.2 > 0.9.1

a = input("input_1 = ")  # 변수 a에 입력값 저장
b = input("input_2 = ")  # 변수 b에 두 번째 입력값 저장

a_1 = a.split('.') # 변수 a_1에 a를 '.'으로 쪼개어 저장
b_1 = b.split('.') # 변수 b_1에 b를 '.'으로 쪼개어 저장

for i in range(len(a_1)): # a_1의 길이만큼 반복
    if a_1[i] == b_1[i]:  # 만약 a_1의 i번째 값과 과 b_1의 i번째 값이 같다면
        continue          # 건너뜀
    else:                 # a_1의 i번째 값과 과 b_1의 i번째 값이 다르다면
        if int(a_1[i]) > int(b_1[i]): # 두 값의 크기를 비교
            print(a, ">", b)          
            break   # 중단 (안 하면 반복 횟수만큼 출력)
        else:
            print(a, "<", b)
            break
        



# 과제 2
## input_1 = "1.0"
## input_2 = "1.0.4"
## 출력 : 1.0 < 1.0.4

a = input("input_1 = ")
b = input("input_2 = ")

a_1 = a.split('.')
b_1 = b.split('.')

for i in range(len(a_1)):
    if a_1[i] == b_1[i]:
        continue
    else:
        if int(a_1[i]) > int(b_1[i]):
            print(a, ">", b)
            break
        else:
            print(a, "<", b)
            break

    
    

# 과제3
## input_1 = ["0.1.0", "1.0.4.9"]
## input_2 = ["0.0.1", "1.04.9"]
## 결과 : 0.1.0 > 0.0.1, 1.0.4.9 < 1.04.9

a = input("input_1 = ").split(',') # a리스트에 값 입력받아 ','를 기준으로 쪼개기
b = input("input_2 = ").split(',') # b리스트에 값 입력받아 ','를 기준으로 쪼개기

for x in range(2): # 두 번 반복
    a_1 = a[x].split('.') # 리스트의 첫 번째와 두 번째 값을 쪼개어 저장
    b_1 = b[x].split('.')

    for i in range(len(a_1)): # a_1의 길이만큼 반복
        if a_1[i] == b_1[i]:  # 한자리씩 비교  
            continue          # 건너뛰기 
        else:
            if int(a_1[i]) > int(b_1[i]): 
                print(a[x], ">", b[x])
                break
            else:
                print(a[x], "<", b[x])
                break
       
    



