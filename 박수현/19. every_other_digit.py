"""
모든 짝수번째 숫자를 * 로 치환하시오.(홀수번째 숫자,또는 짝수번째 문자를 치환하면 안됩니다.) 로직을 이용하면 쉬운데 정규식으로는 어려울거 같아요.
Example: a1b2cde3~g45hi6 → a*b*cde*~g4*hi6
"""


"""
=============================================================================
과제 1. 짝수번째 자리에 숫자가 나올경우 *로 치환하는 프로그램을 작성하시오.(정규식 사용 금지)
       input = a1b2cde3~g45hi6
       출력 : a*b*cde*~g4*hi6
=============================================================================
"""

# input_txt = 문자열을 입력받을 때, 문자를 하나씩 분해해서 리스트로 저장 
input_txt = list(input('문자열을 입력하세요 : '))

## 짝수번째 자리에 숫자가 나올 경우 '*'로 치환하는 프로그램
for i in range(1, len(input_txt), 2):                   # 짝수번째 자리에서 다음 행위 반복
       if '0' <= input_txt[i] <= '9':                   # 만약 해당 자리에 숫자가 있다면, '*'로 치환
              input_txt[i] = '*'

print(''.join(input_txt))                               # input_txt 출력
print()

"""
=============================================================================
과제 2. 짝수번째 자리에 숫자가 나올경우 *로 치환하는 프로그램을 작성하시오.(정규식 사용)
       input = a1b2cde3~g45hi6
       출력 : a*b*cde*~g4*hi6
=============================================================================
"""

import re                                               # 정규 표현식 모듈 가져오기

# input_txt = 문자열을 입력받을 때, 문자를 하나씩 분해해서 리스트로 저장 
input_txt = list(input('문자열을 입력하세요 : '))

## 짝수번째 자리에 숫자가 나올 경우 '*'로 치환하는 프로그램
for i in range(1, len(input_txt), 2):                   # 짝수번째 자리에서 다음 행위 반복
       input_txt[i] = re.sub('\d', '*', input_txt[i])   # re.sub('숫자'를, '*'로 치환, input_txt[i] 중)

print(''.join(input_txt))                               # input_txt 출력