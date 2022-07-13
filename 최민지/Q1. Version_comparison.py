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

a = input('version1: ')
b = input('version2: ')

if a > b:
    print (a ,'>', b)
else:
    print (a ,'<', b)

# 과제 2
## input_1 = "1.0"
## input_2 = "1.0.4"
## 출력 : 1.0 < 1.0.4

a = input('version1: ')
b = input('version2: ')

if a > b:
    print (a ,'>', b)
else:
    print (a ,'<', b)

# 과제3
## input_1 = ["0.1.0", "1.0.4.9"]
## input_2 = ["0.0.1", "1.04.9"]
## 결과 : 0.1.0 > 0.0.1, 1.0.4.9 < 1.04.9

a = input('version1: ')
b = input('version2: ')
c = input('version3: ')
d = input('version4: ')


if a > b:
    print (a ,'>', b, end=', ')
else:
    print (a ,'<', b, end=', ')

if c > d:
    print (c ,'>', d)
else:
    print (c ,'<', d)

