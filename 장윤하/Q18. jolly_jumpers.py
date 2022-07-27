"""
n개의 정수(n>0)로 이루어진 수열에 대해 서로 인접해 있는 두 수의 차가
1에서 n-1까지의 값을 모두 가지면 그 수열을 유쾌한 점퍼(jolly jumper)라고 부른다.
예를 들어 다음과 같은 수열에서
1 4 2 3
앞 뒤에 있는 숫자 차의 절대 값이 각각 3,2,1이므로 이 수열은 유쾌한 점퍼가 된다. 어떤 수열이 유쾌한 점퍼인지 판단할 수 있는 프로그램을 작성하라.

Input : 각 줄 맨 앞에는 3000 이하의 정수가 있으며 그 뒤에는 수열을 나타내는 n개의 정수가 입력된다. 맨 앞 숫자가 0이면 출력하고 종료한다.
output : 입력된 각 줄에 대해 "Jolly" 또는 "Not Jolly"를 한 줄씩 출력한다

[Sample Input] ※ 주의: 각 줄의 맨 앞의 숫자는 수열의 갯수이다. 첫번째 입력인 4 1 4 2 3 의 맨 앞의 4는 뒤에 4개의 숫자가 온다는 것을 의미함
4 1 4 2 3
5 1 4 2 -1 6

[Sample Output]
Jolly
Not jolly
"""
"""
=============================================================================
과제 1. 수열이 유쾌한 점퍼인지 판단할 수 있는 프로그램을 작성하라.
       input = ["4 1 4 2 3", "5 1 3 2 -1 6"]
       4 1 4 2 3,5 1 3 2 -1 6
       출력 : Jolly
             Not Jolly
=============================================================================
"""

jumper_lst = input("수열을 입력하세요: ").split(',')        # 판달할 수열 입력



for i in range(len(jumper_lst)):                        # 해당 수열의 개수만큼 반복
    deleteone = jumper_lst[i][1:].split()               # 첫 번째 문자와 구분하기 위해 두 번쨰 글자부터 문자열을 나눠서 리스트에 저장
    minus_lst = []                                      # 두 수를 빼기 연산한 후 저장할 리스트 생성
    for j in range(len(deleteone)-1):                                   # 첫 번째 글자를 제외한 리스트에서
        minus_lst.append(abs(int(deleteone[j])-int(deleteone[j + 1])))  # 앞 뒤 두 자리를 뺀 후 abs함수로 절대값 반환을 하여 리스트에 저장

    if list(range(1, int(jumper_lst[i][0]))) == sorted(minus_lst):      # 1부터 첫 번째 수에서 -1한 값까지 범위가 절대값을 저장한 리스트를 정렬했을 때의 모습과 동일하다면
        print('Jolly')                                                  # Jolly를 프린트
    else:                                                               # 아닌 경우
        print('Not Jolly')                                              # Not jolly




"""
=============================================================================
과제 2. 수열이 jolly jumper인지 판단할 수 있는 프로그램을 작성하시오.
       input = ["4 1 4 2 3", "5 1 3 2 -1 6", "0"]
       4 1 4 2 3,5 1 3 2 -1 6,0
       출력 : Jolly
             Not Jolly
             0
=============================================================================
"""

jumper_lst = input("수열을 입력하세요: ").split(',')



for i in range(len(jumper_lst)):
    deleteone = jumper_lst[i][1:].split()
    minus_lst = []
    for j in range(len(deleteone)-1):
        minus_lst.append(abs(int(deleteone[j])-int(deleteone[j + 1])))

    if jumper_lst[i][0] == '0':                                       # 입력한 수열의 첫 글자가 0인 경우
        print('0')                                                    # 0을 프린트
    elif list(range(1, int(jumper_lst[i][0]))) == sorted(minus_lst):
        print('Jolly')
    else:
        print('Not Jolly')