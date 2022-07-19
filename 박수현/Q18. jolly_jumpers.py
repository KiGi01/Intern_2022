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
       출력 : Jolly
             Not Jolly
=============================================================================
"""

# input_seq_zip = 정수로 이루어진 수열을 입력받을 때, 이를 ', '을 기준으로 분해
input_seq_zip = input('정수로 이루어진 수열을 입력하세요 : ').split(', ')

## 수열이 유쾌한 점퍼인지 판단하는 프로그램
for input_seq in input_seq_zip:                                         # 수열의 리스트를 하나씩 분해
      input_seq = input_seq.split()                                     # input_seq = 하나의 수열을 공백을 기준으로 분해
      seq_n = int(input_seq[0])                                         # seq_n = 맨 앞의 숫자는 수열의 개수
      seq_dif_zip = []                                                  # seq_dif_zip = 인접한 두 수의 차이들의 리스트가 될 빈 리스트 

      for i in range(1, len(input_seq) - 1):                            # input_seq[1]부터 끝까지 다음 행위 반복 
            seq_dif = abs(int(input_seq[i]) - int(input_seq[i + 1]))    # seq_dif = 인접한 두 수의 차이의 절대값
            seq_dif_zip.append(seq_dif)                                 # 차이의 절대값을 seq_dif_zip에 추가

      if sorted(seq_dif_zip) == list(range(1, seq_n)):                  # 만약 차이들과 1부터 seq_n - 1까지가 같다면, 'Jolly' 출력
            print('Jolly')
      else:                                                             # 아니라면(유쾌한 점퍼가 아니라면), 'Not Jolly' 출력
            print('Not Jolly')
      
print()

"""
=============================================================================
과제 2. 수열이 jolly jumper인지 판단할 수 있는 프로그램을 작성하시오.
       input = ["4 1 4 2 3", "5 1 3 2 -1 6", "0"]
       출력 : Jolly
             Not Jolly
             0
=============================================================================
"""

# input_seq_zip = 정수로 이루어진 수열을 입력받을 때, 이를 ', '을 기준으로 분해
input_seq_zip = input('정수로 이루어진 수열을 입력하세요 : ').split(', ')

## 수열이 유쾌한 점퍼인지 판단하는 프로그램 (아래는 동일)
for input_seq in input_seq_zip:
      input_seq = input_seq.split()
      seq_n = int(input_seq[0])
      
      if seq_n == 0:                                                    # 만약 맨 앞 숫자가 0이라면, 0을 출력한 후 종료
            print(seq_n)
            break

      seq_dif_zip = []
      for i in range(1, len(input_seq) - 1):
            seq_dif = abs(int(input_seq[i]) - int(input_seq[i + 1]))
            seq_dif_zip.append(seq_dif)

      if sorted(seq_dif_zip) == list(range(1, seq_n)):
            print('Jolly')
      else:
            print('Not Jolly')