"""
당신은 어떤 그래픽 처리 라이브러리를 제작하고 있다. 라이브러리의 사용자는 다양한 단위를 이용해 데이터를 입출력하기 때문에 이 라이브러리에는 단위 변환기가 포함되어야 한다.
아래 조건에 따라 단위 변환 함수를 제작하라.
단위 변환기는 다음 단위들을 입력받아 다른 단위로 변환할 수 있어야 한다.

inch(인치)
cm(센티미터)
mm(밀리미터)
px(픽셀)
pt(포인트)
dxa(20분 포인트)
emu(EMU)

당신은 변환율 상수를 꼭 필요한 만큼만 정의할 생각이다. 라이브러리의 메모리 사용량을 최소화하는 목적도 있고, 여러 개의 상수를 손으로 입력하다 보면 실수로 버그를 만들 위험도 있기 때문이다.
당신은 백과사전을 뒤져서 믿을 수 있는 변환율 여섯 개를 찾아냈다. 당신은 아래에 있는 변환율만을 정의하여야 하며, 각 단위에서 다른 단위로 모든 경우의 변환을 지원해야 한다.

1 inch  =  2.54 cm
1 cm    =    10 mm
1 inch  =    72 pt
1 inch  =    96 px
1 pt    =    20 dxa
1 dxa   =   635 emu

입력: 단위 변환기는 두 개의 인수를 입력받는다. 첫 번째 인수는 한 단위의 수를 표현한 문자열이고 두 번째 인수는 변환하고자 하는 단위를 표현한 문자열이다.
출력: 변환된 수와 단위를 문자열로 출력한다.

입출력예:

param1         param2     result
===================================
"10 cm"        "cm"       "10 cm"
"10 inch"      "mm"       "254 mm"
"1024 px"      "pt"       "768 pt"
"768 px"       "inch"     "8 inch"
"9144000 emu"  "inch"     "10 inch"
"12000 dxa"    "px"       "800 px"
"""

"""
========================================================================
과제1. 아래의 입력에 대한 mm, pt, px, dxa, emu로 변환한 값을 출력하여라. 
        - input_unit = 10 inch
        - 출력값 : 254 mm, 720 pt, 960 px, 14400 dxa, 9144000 emu
========================================================================
"""

# unit_dic = 1 inch를 변환한 값에 대한 딕셔너리
unit_dic = {'mm' : 25.4, 'pt' : 72, 'px' : 96, 'dxa' : 1440, 'emu' : 914400}
trans_list = []                                                  # trans_list = 변환한 값에 대한 빈 리스트

input_unit = input('변환할 값을 입력하세요 : ').split()           # input_unit = 입력받은 값을 공백을 기준으로 분해
input_num = int(input_unit[0])                                   # input_num = input_unit 중 숫자를 숫자(정수)로 변환

for i in unit_dic:                                               # unit_dic의 하나씩 다음 행위 반복
    trans_list.append(f'{int(input_num * unit_dic[i])} {i}')     # input_num에 1 inch를 변환한 값을 곱한 후 리스트에 추가 

print(', '.join(trans_list))                                     # 변환한 값에 대한 리스트 출력
print()

"""
========================================================================
과제2. input_unit을 trans_unit의 단위로 변환한 값을 출력하여라. 
        - input_unit = '768 px'
        - trans_unit =  'inch'
        - 출력값 : 8 inch
========================================================================
"""

# unit_dic = 1 inch를 변환한 값에 대한 딕셔너리
unit_dic = {'cm' : 2.54, 'mm' : 25.4, 'pt' : 72, 'px' : 96, 'dxa' : 1440, 'emu' : 914400}

# input_num = 입력받은 값 중 숫자에 해당하는 것, input_unit = 입력받은 값 중 단위에 해당하는 것
input_num, input_unit = input('변환할 값을 입력하세요 : ').split()
# trans_unit = 변환하고 싶은 단위
trans_unit = input('변환하고 싶은 단위를 입력하세요 : ')

# input_num에 input_unit에 대한 값을 나눈 후 출력
print(f'{int(input_num) // unit_dic[input_unit]} {trans_unit}')

""""
========================================================================
과제3. 아래의 입력에 대한 변환한 값을 출력하여라.
        - 조건 1 : input_unit과 trans_unit을 input() 함수를 사용하여 입력받는다.
        - 조건 2 : 입력 - 출력 - 입력 - 출력을 반복하는 코드를 작성하고, 반복 횟수는 4번이다.
     
        input_unit   trans_unit     출력값  
        "10 cm"        "cm"       "10 cm"
        "10 inch"      "mm"       "254 mm"
        "1024 px"      "pt"       "768 pt"
        "768 px"       "inch"     "8 inch"
========================================================================
"""

# 단위를 변환하는 프로그램 정의
def is_unit_convert(input_num, input_unit, trans_unit):
    # 만약 input_unit과 trans_unit이 같다면, 그대로 출력
    if input_unit == trans_unit:
        print(f'{input_num} {input_unit}')
    # 만약 input_unit이 'inch'라면, input_num에 1 inch를 변환한 값을 곱한 후 출력
    elif input_unit == 'inch':
        print(f'{int(int(input_num) * unit_dic[trans_unit])} {trans_unit}')
    # 만약 trans_unit이 'inch'라면, input_num에 input_unit에 대한 값을 나눈 후 출력
    elif trans_unit == 'inch':
        print(f'{int(input_num) // unit_dic[input_unit]} {trans_unit}')
    # 그 외라면, input_num에 input_unit에 대한 값을 나누고, 1 inch를 변환한 값을 곱한 후 출력
    else:
        print(f'{int(int(input_num) / unit_dic[input_unit] * unit_dic[trans_unit])} {trans_unit}')

if __name__ == '__main__':
    # 다음 행위 4번 반복
    for i in range(4):
        print()
        # input_num = 입력받은 값 중 숫자에 해당하는 것, input_unit = 입력받은 값 중 단위에 해당하는 것
        input_num, input_unit = input('변환할 값을 입력하세요 : ').split()
        # trans_unit = 변환하고 싶은 단위
        trans_unit = input('변환하고 싶은 단위를 입력하세요 : ')

        # 단위를 변환하는 프로그램 실행
        is_unit_convert(input_num, input_unit, trans_unit)