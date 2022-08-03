"""
4개의 직사각형이 평면에 있는데 밑변이 모두 가로축에 평행하다. 이 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오. 이 네 개의 직사각형들은 서로 떨어져 있을 수도 있고 겹쳐 있을 수도 있다.
또한 하나가 다른 하나를 포함할 수도 있으며, 변이나 꼭지점이 겹쳐질 수도 있다.

입력형식

하나의 직사각형은 왼쪽 아래의 꼭지점과 오른쪽 위의 꼭지점의 좌표로 주어진다. 입력은 네 줄이며, 각 줄은 네 개의 정수로 하나의 직사각형을 나타낸다.
첫 번째와 두 번째의 정수는 사각형의 왼쪽 아래 꼭지점의 x좌표, y좌표이고, 세 번째와 네 번째의 정수는 사각형의 오른쪽 위 꼭지점의 x좌표, y좌표이다.
단, x좌표와 y좌표는 1 이상이고 1000 이하인 정수이다.

출력형식

화면에 4개의 직사각형이 차지하는 면적을 출력한다.

입력예제

1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6

출력예제

26
"""
"""
========================================================================
과제1. input1과 input2로 구성되는 두 직사각형이 차지하는 넓이를 구하시오.
      - 조건 1 : 첫 번째와 두 번째 정수는 사각형 왼쪽 아래 꼭지점의 x좌표, y좌표이고, 세 번째와 네 번째의 정수는 오른쪽 위 꼭지점의 x좌표, y좌표이다.
      - 조건 2 : 직사각형의 면적이 겹칠 경우, 중복하여 계산하지 않는다.
      - rectangle1 = '1 2 4 4'
      - rectangle2 = '2 3 5 7'
      - 출력값 : 16
========================================================================
"""

def fill_plane(plane, coordinate):                              # 사각형 채우는 함수
    for x in range(coordinate[0],coordinate[2]):                # x축
        for y in range(coordinate[1],coordinate[3]):            # y축
            plane[y][x] = 1                                     # 사각형을 1로 칠하기

Plane = [[0]*1000 for x in range(1000)]                         # 평면 만들기
rectangle1 = input('rectangle1 = ')
rectangle2 = input('rectangle2 = ')
rectangle_list = []
rectangle_list.append(rectangle1)
rectangle_list.append(rectangle2)
print(rectangle_list)

for x in rectangle_list:
    coordinate = [int(c) for c in x.split()]
    fill_plane(Plane,coordinate)                                # 사각형 채우기

Area = sum([sum(x) for x in Plane])                             # Plane만큼 반복할 때, x의 합의 합
print('출력값 : ', Area)   
                                   
"""
========================================================================
과제2. 아래의 입력인 4개의 직사각형이 차지하는 넓이를 구하시오.(직사각형이 겹치거나 또 다른 하나가 다른 하나를 포함할 수 있음)
      - 조건 1 : 첫 번째와 두 번째 정수는 사각형 왼쪽 아래 꼭지점의 x좌표, y좌표이고, 세 번째와 네 번째의 정수는 오른쪽 위 꼭지점의 x좌표, y좌표이다.
      - 조건 2 : 직사각형의 면적이 겹칠 경우, 중복하여 계산하지 않는다.      
      - rectangle_list = ['1 2 4 4','2 3 5 7','3 1 6 5','7 3 8 6']
      - 출력값 : 26
========================================================================
"""

def fill_plane(plane, coordinate):                              # 사각형 채우는 함수
    for x in range(coordinate[0],coordinate[2]):                # x축
        for y in range(coordinate[1],coordinate[3]):            # y축
            plane[y][x] = 1                                     # 사각형을 1로 칠하기

Plane = [[0]*1000 for x in range(1000)]                         # 평면 만들기
a,b,c,d = input('rectangle_list= ').split(',')
rectangle_list = []
rectangle_list.append(a)
rectangle_list.append(b)
rectangle_list.append(c)
rectangle_list.append(d)

for x in rectangle_list:
    coordinate = [int(c) for c in x.split()]
    fill_plane(Plane,coordinate)                                # 사각형 채우기

Area = sum([sum(x) for x in Plane])                             # Plane만큼 반복할 때, x의 합의 합
print('출력값 : ', Area)    