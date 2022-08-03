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
def inchchange(source):
    result, tmp = 0, 0
    result1 = 0

    source_list = source.split(' ')
# source를 'inch' 값으로 변환 한 후
    if source_list[1] == 'inch': #inch라면 그대로
        tmp = int(source_list[0])
        result = 2.54 * tmp * 10
        result1 = tmp * 72
        result2 = tmp * 96
        result3 = tmp * (72 * 20)
        result4 = tmp * (72 * 20) * 635

    print("출력값 : {} mm, {} pt, {} px, {} dxa, {} emu".format(result, result1, result2, result3, result4))

if __name__ == "__main__":
    source = input("입력하세요: ")
    inchchange(source)

"""
========================================================================
과제2. input_unit을 trans_unit의 단위로 변환한 값을 출력하여라. 
     - input_unit = '768 px'
     - trans_unit =  'inch'
     - 출력값 : 8 inch
========================================================================
"""

def inchchange(source, unit):
    result, tmp = 0, 0
    source_list = source.split(' ')
# source를 'inch' 값으로 변환 한 후
    if source_list[1] == 'inch': #inch라면 그대로
        tmp = int(source_list[0])
    elif source_list[1] == 'cm': #cm 
        tmp =  int(source_list[0]) / 2.54
    elif source_list[1] == 'pt':
        tmp =  int(source_list[0]) / 72
    elif source_list[1] == 'px':
        tmp = int(source_list[0]) / 96
    elif source_list[1] == 'dxa':
        tmp = int(source_list[0]) / (20 * 72)
    elif source_list[1] == 'emu':
        tmp = int(source_list[0])/(20 * 635 * 72)
# unit 값 단위로 변환
    if unit == 'inch':
        result = tmp
    elif unit == 'cm':
        result = tmp * 2.54
    elif unit == 'mm':
        result = 2.54 * tmp * 10
    elif unit == 'pt':
        result = tmp * 72
    elif unit == 'px':
        result = tmp * 96
    elif unit == 'dxa':
        result = tmp / (72 * 20)
    elif unit == 'emu':
        result = tmp / (72 * 20) * 635

    print("%-10s"%(str(int(result))+' '+unit))

if __name__ == "__main__":
    source = input("입력하세요: ")
    unit = input("단위를 입력하세요: ")
    inchchange(source, unit)

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

def inchchange(source, unit):
    result, tmp = 0, 0
    source_list = source.split(' ')
# source를 'inch' 값으로 변환 한 후
    if source_list[1] == 'inch': #inch이면 그대로 반환
        tmp = int(source_list[0])
    elif source_list[1] == 'cm': #cm이면 2.54 나누기
        tmp =  int(source_list[0]) / 2.54 
    elif source_list[1] == 'pt': #pt이면 72 나누기
        tmp =  int(source_list[0]) / 72 
    elif source_list[1] == 'px': #px이면 96 나누기
        tmp = int(source_list[0]) / 96
    elif source_list[1] == 'dxa': #dxa이면 (20 * 72) 나누기
        tmp = int(source_list[0]) / (20 * 72)
    elif source_list[1] == 'emu': #emu이면 (20 * 635 * 72) 나누기
        tmp = int(source_list[0])/(20 * 635 * 72)
# unit 값 단위로 변환
    if unit == 'inch': 
        result = tmp
    elif unit == 'cm':
        result = tmp * 2.54
    elif unit == 'mm':
        result = 2.54 * tmp * 10
    elif unit == 'pt':
        result = tmp * 72
    elif unit == 'px':
        result = tmp * 96
    elif unit == 'dxa':
        result = tmp / (72 * 20)
    elif unit == 'emu':
        result = tmp/(72 * 20) * 635

    print("%-10s   %-10s   %-10s"%(source,unit,str(int(result))+' '+unit))

if __name__ == "__main__":
    for i in range (4): #4번 반복
        print() 
        source = input("숫자와 단위를 입력하세요: ")
        unit = input("단위를 입력하세요: ")
        inchchange(source, unit)