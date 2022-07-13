"""
- 첫 번째 계산
  아이들은 여러 자리 숫자들을 더하기 위해서
  우에서 좌로 숫자를 하나씩 차례대로 더 하라고 배웠다.
  1을 한 숫자 위치에서 다음 자리로 더하기위해 이동하는 "한자리올림"연산을
  많이 발견하는 것은 중요한 도전이 된다.
  당신의 일은 교육자가 그들의 어려움을 평가하기 위하여,
  덧셈 문제들의 각 집합에 대해서 한자리올림 연산들의 수를 계산하는 것이다.

- 입력
  입력의 각 라인은 10개의 숫자들보다 미만인 양의 정수들 두 개를 포함한다.
  입력의 마지막 라인은 0 0 을 포한한다.

- 출력
  마지막을 제외한 입력의 각 라인에 대해서 당신은 두 숫자들을 더한 결과에서
  한자리올림 연산들의 수를 아래 처럼 보여지는 형식으로 계산하여 출력해야 한다.

[입력 샘플]
123 456
555 555
123 594
0 0

[출력 샘플]
No carry operation
3 carry operation
1 carry operation
"""

"""
==========================================================================
# 과제 1. 입력 값의 자릿수가 같을 때 한자리 올림 계산 횟수를 출력하시오.
## Input :  123 456
            555 555
            123 594
            0 0
## 출력 :   No carry operation
           3 carry operation
           1 carry operation
## 조건 1> 입력이 총 4번 완료된 후에 계산이 수행되도록 하세요.
## 조건 2> 입력값은 '123 456'의 형태로 받습니다.
==========================================================================
==========================================================================
# 과제 2. 입력 값의 자릿수가 다를 때의 한자리 올림 계산 횟수를 출력하시오.
## Input : 13 452
           55 555
           1009 99
           0 0
## 출력 : No carry operation
         2 carry operation
         1 carry operation
## 조건 1> 입력이 총 4번 완료된 후에 계산이 수행되도록 하세요.
## 조건 2> 입력값은 '13 452'의 형태로 받습니다.
==========================================================================
"""
#1
b = []
while True:  # 무한루프
  cnt=0
  A, B = input("Input = ").split(' ')  # A와 B에 값을 각각 입력 받음
  if A=='0' and B=='0':  # A와 B 모두 0인 경우
    break   # 루프 중단
  else:                  # A와 B 둘 중 하나라도 0이 아닌 경우
    for i in range(len(A)):       # A의 자릿수만큼 반복
      if int(A[i])+int(B[i])>=10: # A와 B의 동일한 자릿수끼리 더했을 때 그 값이 10 이상인 경우
        cnt+=1   # 1씩 더함
    if cnt==0:   # 올림 계산 횟수가 0인 경우
      b.append('No carry operation') # b에 추가
    else:        # 올림 계산 횟수가 1이상인 경우
      b.append(str(cnt) +' carry operation') # 개수와 문자를 더해서 저장
print(*b, sep='\n') # 각 값을 한 줄에 하나씩 출력

 
#2
b = []
while True: # 무한루프
  cnt=0
  A, B = input("Input = ").split(' ') # A와 B에 값을 각각 입력 
  if A=='0' and B=='0':     # A와 B 모두 0인 경우
    break                   # 루프 중단
  
  else:                     # A와 B 둘 중 하나라도 0이 아닌 경우
    if len(A) > len(B):     # A 자릿수가 B의 자릿수보다 큰 경우
      A_B = len(A) - len(B)         # 자릿수의 차이를 계산
      for j in range(A_B):          # 자릿수의 차이만큼 B의 앞에 0을 추가
        B = '0' + B         
      for i in range(len(A)):       # 동일하게 계산 횟수 저장
        if int(A[i])+int(B[i])>=10:
          cnt+=1
      if cnt==0:
        b.append('No carry operation')
      else:
        b.append(str(cnt) +' carry operation')
    
    else:                   # B 자릿수가 A의 자릿수보다 큰 경우
      B_A = len(B) - len(A)         # 자릿수의 차이를 계산
      for h in range(B_A):          # 자릿수의 차이만큼 A의 앞에 0을 추가
        A = '0' + A
      for i in range(len(A)):       # 동일하게 계산 횟수 저장
        if int(A[i])+int(B[i])>=10:
          cnt+=1
      if cnt==0:
        b.append('No carry operation')
      else:
        b.append(str(cnt) +' carry operation')
              
print(*b, sep='\n')  # 각 값을 한 줄에 하나씩 출력


