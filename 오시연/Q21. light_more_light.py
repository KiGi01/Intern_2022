"""
우리 학교에는 복도 불을 켜고 끄는 마부(Mabu)라는 사람이 있다.
전구마다 불을 켜고 끄는 스위치가 있다.
불이 꺼져 있을 때 스위치를 누르면 불이 켜지고 다시 스위치를 누르면 불이 꺼진다.
처음에는 모든 전구가 꺼져 있다.
마부라는 사람은 특이한 행동을 한다.
복도에 n개의 전구가 있으면, 복도를 n번 왕복한다.
i번째 갈 때 그는 i로 나누어 떨어지는 위치에 있는 스위치만 누른다.
처음 위치로 돌아올 때는 아무 스위치도 건드리지 않는다.
i번째 왕복은 (이런 이상한 행동을 하면서) 복도를 한 번 갔다가 오는 것으로 정의된다.
마지막 전구의 최종 상태를 알아내자.
과연 그 전구는 켜져 있을까 아니면 꺼져 있을까?

Input : 복도에 있는 n번째 전구를 나타내는 숫자가 입력된다. (2^32-1 이하의 정수가 입력된다.) 0은 입력의 끝을 의미하며 그 값은 처리하지 않는다.
Output : 그 전구가 켜져 있으면 "yes"를, 꺼져 있으면 "no"를 출력한다. 테스트 케이스마다 한 줄에 하나씩 출력한다.

"""


"""
=============================================================================
과제 1 : 복도에 있는 n번째 전구의 최종 상태를 출력하시오.
        - 조건 : 0은 입력의 끝을 의미하며 그 값은 처리하지 않는다.
        input = [3, 6241, 8191, 0] (만약 전구번호가 3이면, 3번 왕복한 후의 전구상태를 출력하는 코드를 짜면 된다.)
        출력 : (테스트 케이스마다 한 줄에 하나씩 출력해야함.)
              no
              yes
              no
=============================================================================
"""

while 1:
      input_ = map(int,input('입력: ').split(', '))   #콤마 기준 분리
      for n in input_:       #숫자 하나씩 꺼냄
            if n == 0:  #0일 경우 종료
                  break
            print('yes' if n**0.5 % 1 == 0 else 'no')  #n의 제곱근이 정수인지 계산
      
#n번째(마지막) 전구는 i가 n의 약수일 때 켜지고 꺼짐
#마지막 전구는 처음에 꺼져있으므로 n의 약수 개수가 홀수일 때 최종 상태가 켜져있게 됨
#어떤 수의 완전제곱수(1, 4, 9, 16...)만이 홀수개의 약수를 가짐
#따라서 n이 어떤 수의 완전제곱수인지 확인



