"""
-----------------  Question  -----------------
지뢰찾기 게임은 M x N 매트릭스에 위치해 있는 지뢰를 찾는 게임이다.
M x N 매트릭스 상의 격자(square)는 지뢰이거나 지뢰가 아니다.
지뢰 격자는 *로 표시한다. 지뢰가 아닌 격자(square)는 숫자로 표시하며 그 숫자는 인접해 있는 지뢰의 수를 의미한다.
(격자(sqaure)는 최대 8개의 인접한 지뢰를 가질 수 있다.)
다음은 4x4 매트릭스에서 2개의 지뢰(*)를 표시하는 방법이다.
 *...
 ....
 .*..
 ....

이 게임의 목표는 지뢰의 위치(*)를 제외한 나머지 격자들의 숫자를 맞추는 것이다.
위 경우의 답은 아래와 같다.
 *100
 2210
 1*10
 1110

입력 : 첫번째 줄은 M x N 의 M(행)과 N(열)에 해당되는 숫자이다.
       N과 M은 0보다 크고 100 이하이다(0< N, M <=100).
       그 다음 M개의 줄이 차례로 입력되고 각 줄은 정확하게 N개의 문자가 입력된다.
       지뢰 격자는 *로 표시하며 지뢰가 아닌 격자는 .(dot)로 표시한다.
출력 : 지뢰(*)를 제외한 나머지 격자의 숫자값을 찾아서 M x N 매트릭스를 출력한다.
----------------------------------------------
"""

"""
==========================================================================
과제 1. input의 숫자만큼 '*'과 '.'으로 구성된 문자열을 출력하시오. 
      - 조건1 : random 모듈을 활용하시오.
      - input = '4'
      - 출력 : *.** 또는 ...* 등등
==========================================================================
"""

import random                                                        # 랜덤 모듈 가져오기

# input_n = 정수를 입력받을 때, 숫자(정수)로 변환
input_n = int(input('정수를 입력하세요 : '))

## 문자열을 랜덤으로 생성하는 프로그램
random_box = ['*', '.'] * input_n                                    # random_box = 랜덤으로 뽑기 위한 리스트
random_list = random.sample(random_box, input_n)                     # random_list = 랜덤 박스에서 input_n만큼 뽑기

print(''.join(random_list))                                          # random_list 출력
print()

"""
==========================================================================
과제 2. 행과 열을 입력하면 '*'과 '.'으로 구성된 행렬을 출력하시오.
      - 조건1 : random 모듈을 활용하시오.
      - 조건2 : 행과 열은 1보다 크고 100 이하인 정수이다.
      - row = 3
      - column = 6
      - 출력 (예시이며 random 모듈을 사용하였으므로 결과는 다를 수 있음.)
        [['*', '.', '.', '.', '*', '.'], 
        ['.', '.', '*', '.', '.', '.'],
        ['.', '.', '.', '*', '.', '*']]
==========================================================================
"""

import random                                                        # 랜덤 모듈 가져오기

# input_row = 행이 될 정수를 입력받을 때, 숫자(정수)로 변환
input_row = int(input('행이 될 정수를 입력하세요 : '))
# input_column = 열이 될 정수를 입력받을 때, 숫자(정수)로 변환
input_column = int(input('열이 될 정수를 입력하세요 : '))
# mineticon_list = '*', '.'로 구성된 문자열들의 리스트가 될 빈 리스트
mineticon_list = []

## 조건2를 충족하기 위한 조건문 (조건을 벗어났다면, '잘못 입력했습니다'만 출력)
if input_row < 1 or 100 < input_row or input_column < 1 or 100 < input_column:
      print('잘못 입력했습니다')

## '*', '.'로 구성된 문자열을 생성하는 리스트
else:                                                             # 만약 조건2를 충족했다면,
      for i in range(input_row):                                  # input_row만큼 다음 행위 반복
            random_box = ['*', '.'] * input_column                # random_box = 랜덤으로 뽑기 위한 리스트
            random_list = random.sample(random_box, input_column) # random_list = 랜덤 박스에서 input_column만큼 뽑기
            mineticon_list.append(random_list)                    # 생성한 문자열을 mineticon_list에 추가

for mineline in mineticon_list:                                   # mineticon_list 출력
      print(mineline)
print()

"""
==========================================================================
#과제 3. 과제2에서 생성한 행렬을 이용하여 지뢰(*)를 제외한 나머지 격자의 숫자값을 찾고 행렬을 출력하시오.
      - 조건1 : random 모듈을 활용하시오.
      - 조건2 : 행과 열은 1보다 크고 100 이하인 정수이다.
      - row = 3
      - column = 6
      - 출력 (예시이며 random 모듈을 사용하였으므로 결과는 다를 수 있음.)
        *212*1
        12*332
        012*2*
==========================================================================
"""

# minenumlist = mineticon_list 중 '.'을 숫자로 변환한 리스트가 될 리스트
minenum_list = mineticon_list

## 과제2에서 생성한 행렬을 지뢰찾기 게임을 위한 행렬로 변환하는 프로그램
for i in range(input_row):                                           # input_row만큼 다음 행위 반복
      for j in range(input_column):                                  # input_column만큼 다음 행위 반복
            if minenum_list[i][j] == '*':                            # 만약 해당 자리에 지뢰가 있다면, 그대로 유지
                  continue
            
            else:                                                    # 지뢰가 없다면('.'이라면),
                  mine_count = 0                                     # mine_count = 근처에 있는 지뢰의 수 (시작은 0)
                  for x in range(-1, 2):                             # x는 -1, 0, 1로  다음 행위 반복
                        for y in range(-1, 2):                       # y는 -1, 0, 1로 다음 행위 반복
                              # 만약 근처에 지뢰가 있다면, 카운트 (근처 = 자신의 위치를 기준으로 상하좌우 및 대각선)
                              if 0 <= i + x < input_row and 0 <= j + y < input_column and minenum_list[i + x][j + y] == '*':
                                    mine_count += 1
                              minenum_list[i][j] = mine_count        # 해당 자리의 '.'을 mine_count로 변환

for mineline in minenum_list:                                        # minenum_list 출력
      print(''.join(map(str, mineline)))