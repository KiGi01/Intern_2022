"""
전화번호의 표준형은 세 번째 번호와 네 번째 번호 사이에 하이픈(-)을 삽입한 7개의 숫자로 구성되어 있다. (예: 888-1200).
전화기의 키패드는 다음과 같은 글자 대 숫자의 대응을 지닌다.

A, B, C -> 2
D, E, F -> 3
G, H, I -> 4
J, K, L -> 5
M, N, O -> 6
P, R, S -> 7
T, U, V -> 8
W, X, Y -> 9
Q와 Z에 대한 대응관계는 존재하지 않는다. 하이픈은 전화기에 입력되지 않으며 필요에 따라 추가되거나 빠질 수 있다.
TUT-GLOP의 표준형은 888-4567이고, 310-GINO의 표준형은 310-4466, 3-10-10-10의 표준형은 310-1010이다.
만약 어떤 두 전화번호가 같은 표준형을 지니면 그들은 같은 번호이다.

여러분의 회사는 지역 회사원들의 전화번호를 정리하고 있다.
품질 관리 과정의 일환으로, 여러분은 정리된 전화번호부의 번호 중에 같은 것이 둘 이상 있지 않은지 확인하고 싶다.

Input
입력은 하나의 테스트 케이스로 구성된다. 입력의 첫 줄은 전화번호의 갯수(<=100,000)로 이뤄져 있다.
남은 줄들은 전화번호부 내의 전화번호들이 한 줄에 하나씩 들어 있다.
각 전화번호는 십진 숫자들과 대문자(Q,Z 제외), 하이픈으로 구성된 문자열로 이뤄져 있다.
문자열 내에서 정확히 7개의 문자들이 숫자 또는 알파벳 문자이다.

Output
한 번 이상 등장한 전화번호들이 출력을 구성한다. 각 줄은 표준형으로 표현된 전화번호와 출현 횟수가 하나의 공백 문자로 구분되어 있다.
출력되는 전화 번호들은 증가하는 사전식 순서로 되어 있어야 한다. 만약 입력으로 들어온 전화번호 중에 중복이 없다면 "No duplicates."를 출력한다.

Sample Input
12
4873279
ITS-EASY
888-4567
3-10-10-10
888-GLOP
TUT-GLOP
967-11-11
310-GINO
F101010
888-1200
-4-8-7-3-2-7-9-
487-3279

Sample Output
310-1010 2
487-3279 4
888-4567 3
"""
"""
=============================================================================
과제 1. 다음 전화번호를 표준형으로 변경하시오.
       - input : 310-GINO
       - 출력 : 310-4466
=============================================================================
"""

def standard_number(before_n):   #함수 정의
    after_num = ''         #표준형을 저장할 변수
    for num in before_n:        #요소 하나씩 꺼내 반복
        if num in '0123456789':   #만약 숫자이면
            after_num += num      #그대로 변수에 저장
        elif num in 'ABC':        #각 알파벳에 대응하는 숫자를 추가
            after_num += '2'
        elif num in 'DEF':
            after_num += '3'
        elif num in 'GHI':
            after_num += '4'
        elif num in 'JKL':
            after_num += '5'
        elif num in 'MNO':
            after_num += '6'
        elif num in 'PRS':
            after_num += '7'
        elif num in 'TUV':
            after_num += '8'
        elif num in 'WXY':
            after_num += '9'
    after_num =  after_num[:3] + '-' + after_num[3:]   #하이픈을 추가한 표준형으로 저장
    return  after_num              #완성된 표준형 번호를 결과로 반환


input_num = input('번호 입력: ')    
print(standard_number(input_num))    #함수 호출


"""
=============================================================================
과제 2. input의 전화번호를 표준형으로 바꾸었을 때 표준형 전화번호의 등장횟수를 출력하시오. 
       - input = ['4873279','888-4567','487-3279','4-8-7-32-79-','8884567','8-8-845-67']
       - 출력 : 
        888-4567 3 
        487-3279 3
=============================================================================
"""

input_2 = list(input('번호 입력: ').split(','))   #콤마 기준 분리, 리스트로 입력받음
st_numlst = list(map(standard_number, input_2))        #map으로 리스트의 모든 요소를 함수에 적용, 리스트로 반환
num_set = set(st_numlst)     #등장횟수 계산을 위해 중복을 제거한 set
for dup in num_set:          #번호 하나씩 꺼내 반복
    print(dup, st_numlst.count(dup))   #등장횟수 계산하여 출력

"""
=============================================================================
과제 3. input의 전화번호와 표준형으로 바꾸었을 때, 표준형 전화번호의 등장횟수를 출력하시오. 
       - 출력형식 : 표준형전화번호(공백)중복횟수를 한줄에 하나씩 출력하시오
       - 조건1 : 출력되는 표준형 전화번호는 오름차순으로 정렬하시오.
       - 조건2 : 중복 횟수가 1인 표준형 전화번호는 출력에서 제외하시오.
       - 조건3 : input()을 사용하여 처음에는 입력받을 전화번호의 수를 입력하고 그에 따라 전화번호를 입력받을 수 있도록 하시오.
       - input : 
         12 
         4873279
         ITS-EASY
         888-4567
         3-10-10-10
         888-GLOP
         TUT-GLOP
         967-11-11
         310-GINO
         F101010
         888-1200
         -4-8-7-3-2-7-9-
         487-3279
        
        출력 :
        310-1010 2
        487-3279 4
        888-4567 3
=============================================================================
"""

times = int(input('전화번호의 수: '))
befornumlst = []
for i in range(times):   #처음에 입력받은 수만큼 반복
    befornumlst.append(input())    #리스트에 추가
standard_lst = list(map(standard_number, befornumlst))   #map으로 리스트의 모든 요소를 함수에 적용, 리스트로 반환
standard_lst.sort()                 #오름차순 정렬
lst_set = list(set(standard_lst))       #중복 제거하여 리스트로 변환
lst_set.sort()               #오름차순 정렬
if standard_lst == lst_set:   #비교하여 중복이 없는지 확인
    print("No duplicates.")   #중복되는 번호가 한개도 없을시 출력
else:
    for dup_ in lst_set:      #번호 하나씩 꺼내 반복
        if standard_lst.count(dup_) == 1:  #등장횟수가 1일 경우는 생략
            pass
        else:      
            print(dup_, standard_lst.count(dup_))   #등장횟수 2 이상인 번호, 등장횟수를 출력