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


def EvenNumber2Star(input_str):
    replace_str  = ""
    for i, j in zip(input_str, range(1, len(input_str)+1)): 
        if j%2 == 1 :
            replace_str+= i
        else:
#            print(i, j)
            if i.isdigit():
                replace_str+= "*"
            else:
                replace_str+= i
    
    return replace_str

input_str = "a1b2cde3~g45hi6"
print(EvenNumber2Star(input_str))



"""
=============================================================================
과제 2. 짝수번째 자리에 숫자가 나올경우 *로 치환하는 프로그램을 작성하시오.(정규식 사용)
       input = a1b2cde3~g45hi6
       출력 : a*b*cde*~g4*hi6
=============================================================================
"""


import re   #정규표현식 지원모듈

input_str = list(input())
for i in range(1, len(input_str), 2): 
    input_str[i] = re.sub(r'\d', '*', input_str[i])  #re.sub('패턴', 교체함수, '문자열')


