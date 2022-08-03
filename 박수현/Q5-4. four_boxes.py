"""
4개의 직사각형이 평면에 있는데 밑변이 모두 가로축에 평행하다. 이 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오. 이 네 개의 직사각형들은 서로 떨어져 있을 수도 있고 겹쳐 있을 수도 있다.
또한 하나가 다른 하나를 포함할 수도 있으며, 변이나 꼭지점이 겹쳐질 수도 있다.

입력형식)
하나의 직사각형은 왼쪽 아래의 꼭지점과 오른쪽 위의 꼭지점의 좌표로 주어진다. 입력은 네 줄이며, 각 줄은 네 개의 정수로 하나의 직사각형을 나타낸다.
첫 번째와 두 번째의 정수는 사각형의 왼쪽 아래 꼭지점의 x좌표, y좌표이고, 세 번째와 네 번째의 정수는 사각형의 오른쪽 위 꼭지점의 x좌표, y좌표이다.
단, x좌표와 y좌표는 1 이상이고 1000 이하인 정수이다.

출력형식)
화면에 4개의 직사각형이 차지하는 면적을 출력한다.

입력예제)
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6

출력예제)
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

# 직사각형의 왼쪽 아래 꼭지점과 오른쪽 위 꼭지점에 대한 각각의 좌표
alx, aly, arx, ary = map(int, input('첫 번째 직사각형의 좌표를 입력하세요 : ').split())
blx, bly, brx, bry = map(int, input('두 번째 직사각형의 좌표를 입력하세요 : ').split())

same_x = 0                                      # same_x = 직사각형이 겹치는 x좌표 (시작은 0)
for i in range(alx, arx + 1):                   # 두 직사각형의 x좌표 확인
   for j in range(blx, brx + 1):
        if i == j:                              # 만약 겹친다면, 1 더하기
            same_x += 1
if 0 < same_x:                                  # 길이를 계산하기 위해 겹친 좌표 - 1
    same_x -= 1

same_y = 0                                      # same_y = 직사각형이 겹치는 y좌표 (시작은 0)
for i in range(aly, ary + 1):                   # 두 직사각형의 y좌표 확인
   for j in range(bly, bry + 1):
        if i == j:                              # 만약 겹친다면, 1 더하기
            same_y += 1
if 0 < same_y:                                  # 길이를 계산하기 위해 겹친 좌표 - 1
    same_y -= 1

rectangle_s = same_x * same_y                   # rectangle_s = 겹치는 사각형의 넓이
rectangle_a = (arx - alx) * (ary - aly)         # rectangle_a = 첫 번째 사각형의 넓이
rectangle_b = (brx - blx) * (bry - bly)         # rectangle_b = 두 번째 사각형의 넓이

print(rectangle_a + rectangle_b - rectangle_s)  # 두 사각형의 넓이에서 겹치는 부분을 중복하지 않은 넓이 출력
print()

"""
========================================================================
과제2. 아래의 입력인 4개의 직사각형이 차지하는 넓이를 구하시오.(직사각형이 겹치거나 또 다른 하나가 다른 하나를 포함할 수 있음)
        - 조건 1 : 첫 번째와 두 번째 정수는 사각형 왼쪽 아래 꼭지점의 x좌표, y좌표이고, 세 번째와 네 번째의 정수는 오른쪽 위 꼭지점의 x좌표, y좌표이다.
        - 조건 2 : 직사각형의 면적이 겹칠 경우, 중복하여 계산하지 않는다.      
        - rectangle_list = [1 2 4 4, 2 3 5 7, 3 1 6 5, 7 3 8 6]
        - 출력값 : 26
========================================================================
"""

# 사각형의 넓이를 구하는 프로그램 정의
def is_rectagle_size(rectangle_a):
    # 직사각형의 왼쪽 아래 꼭지점과 오른쪽 위 꼭지점에 대한 각각의 좌표
    alx, aly, arx, ary = map(int, rectangle_a.split())

    rectangle_a = (arx - alx) * (ary - aly)         # rectangle_a = 첫 번째 사각형의 넓이
    return rectangle_a                              # rectangle_a 반환

# 겹치는 사각형의 넓이를 구하는 프로그램 정의
def is_same_rectangle(rectangle_a, rectangle_b):
    # 직사각형의 왼쪽 아래 꼭지점과 오른쪽 위 꼭지점에 대한 각각의 좌표
    alx, aly, arx, ary = map(int, rectangle_a.split())
    blx, bly, brx, bry = map(int, rectangle_b.split())

    same_x = 0                                      # same_x = 직사각형이 겹치는 x좌표 (시작은 0)
    for i in range(alx, arx + 1):                   # 두 직사각형의 x좌표 확인
        for j in range(blx, brx + 1):
            if i == j:                              # 만약 겹친다면, 1 더하기
                same_x += 1
    if 0 < same_x:                                  # 길이를 계산하기 위해 겹친 좌표 - 1
        same_x -= 1

    same_y = 0                                      # same_y = 직사각형이 겹치는 y좌표 (시작은 0)
    for i in range(aly, ary + 1):                   # 두 직사각형의 y좌표 확인
        for j in range(bly, bry + 1):
            if i == j:                              # 만약 겹친다면, 1 더하기
                same_y += 1
    if 0 < same_y:                                  # 길이를 계산하기 위해 겹친 좌표 - 1
        same_y -= 1

    rectangle_s = same_x * same_y                   # rectangle_s = 겹치는 사각형의 넓이
    return rectangle_s                              # rectangle_s 반환

# 세 사각형이 겹치는 넓이를 구하는 프로그램 정의
def is_triple(rectangle_a, rectangle_b, rectangle_c):
    # 직사각형의 왼쪽 아래 꼭지점과 오른쪽 위 꼭지점에 대한 각각의 좌표
    alx, aly, arx, ary = map(int, rectangle_a.split())
    blx, bly, brx, bry = map(int, rectangle_b.split())
    clx, cly, crx, cry = map(int, rectangle_b.split())

    same_x = 0                                      # same_x = 직사각형이 겹치는 x좌표 (시작은 0)
    for i in range(alx, arx + 1):                   # 세 직사각형의 x좌표 확인
        for j in range(blx, brx + 1):
            for x in range(clx, cly + 1):
                if i == j == x:                     # 만약 겹친다면, 1 더하기
                    same_x += 1
    if 0 < same_x:                                  # 길이를 계산하기 위해 겹친 좌표 - 1
        same_x -= 1

    same_y = 0                                      # same_y = 직사각형이 겹치는 y좌표 (시작은 0)
    for i in range(aly, ary + 1):                   # 세 직사각형의 y좌표 확인
        for j in range(bly, bry + 1):
            for x in range(cly, crx + 1):
                if i == j == x:                     # 만약 겹친다면, 1 더하기
                    same_y += 1
    if 0 < same_y:                                  # 길이를 계산하기 위해 겹친 좌표 - 1
        same_y -= 1

    triple_s = same_x * same_y                      # triple_s = 겹치는 사각형의 넓이
    return triple_s                                 # rectangle_s 반환

# 사각형이 차지하는 넓이를 구하는 프로그램 정의
def is_four_rectangle(rectangle_list):
    rectangle_size = 0                              # rectangle_size = 사각형의 넓이 (시작은 0) 
    for i in rectangle_list:                        # rectangle_list의 하나씩 다음 행위 반복
        rectangle_size += is_rectagle_size(i)       # rectangle_size에 더하기

    rectangle_same = 0                              # rectangle_same = 겹치는 사각형의 넓이 (시작은 0)
    for i in range(1, len(rectangle_list)):         # 사각형 두 개씩 비교하여 겹치는 사각형의 넓이 구하기
        rectangle_same += is_same_rectangle(rectangle_list[0], rectangle_list[i])
    for i in range(2, len(rectangle_list)):
        rectangle_same += is_same_rectangle(rectangle_list[1], rectangle_list[i])
    rectangle_same += is_same_rectangle(rectangle_list[2], rectangle_list[3])

    triple_same = 0                                 # triple_same = 세 번 겹치는 사각형의 넓이 (시작은 0)
    # 사각형 세 개씩 비교하여 겹치는 사각형의 넓이 구하기
    triple_same += is_triple(rectangle_list[0], rectangle_list[1], rectangle_list[2])
    triple_same += is_triple(rectangle_list[0], rectangle_list[2], rectangle_list[3])
    triple_same += is_triple(rectangle_list[1], rectangle_list[2], rectangle_list[3])
    
    # 네 사각형의 넓이에서 겹치는 부분을 중복하지 않은 넓이 출력
    print(rectangle_size - rectangle_same + triple_same)

if __name__ == '__main__':
    # rectangle_list = 사각형의 좌표를 입력받을 때, ', '를 기준으로 분해
    rectangle_list = input('네 개의 직사각형의 각 좌표를 입력하세요 : ').split(', ')

    is_four_rectangle(rectangle_list)                # 사각형이 차지하는 넓이 구하는 프로그램 실행