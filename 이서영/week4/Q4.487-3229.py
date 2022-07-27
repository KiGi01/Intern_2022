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

def change_alphabet(n):                         # n을 표준형 전화번호로 바꾸는 함수
    result=""                                   # 표준형 전화번호
    for i in n:                                 # n리스트 요소들을 차례대로 변수 i에 대입
        if i == '-' : pass                      # i가 '-'일 경우 통과
        elif i in ['A','B','C'] : result += '2' # i가 'A','B','C'일 경우, result에 2추가
        elif i in ['D','E','F'] : result += '3' # i가 'D','E','F'일 경우, result에 3추가
        elif i in ['G','H','I'] : result += '4' # i가 'G','H','I'일 경우, result에 4추가
        elif i in ['J','K','L'] : result += '5' # i가 'J','K','L'일 경우, result에 5추가
        elif i in ['M','N','O'] : result += '6' # i가 'M','N','O'일 경우, result에 6추가
        elif i in ['P','R','S'] : result += '7' # i가 'P','R','S'일 경우, result에 7추가
        elif i in ['T','U','V'] : result += '8' # i가 'T','U','V'일 경우, result에 8추가
        elif i in ['W','X','Y'] : result += '9' # i가 'W','X','Y'일 경우, result에 9추가
        else :result += i                       # i가 '-'나 알파벳이 아닐 경우, result에 i추가

        if len(result) == 3 : result += '-'     # result의 길이가 3일 경우, result에 '-'추가
    return result                               # result 값 반환

num = input('input : ')
print(change_alphabet(num))

"""
=============================================================================
과제 2. input의 전화번호를 표준형으로 바꾸었을 때 표준형 전화번호의 등장횟수를 출력하시오. 
       - input = [‘4873279’,’888-4567’,’487-3279’,’4-8-7-32-79-’,’8884567’,’8-8-845-67’]
       - 출력 : 
        888-4567 3 
        487-3279 3
=============================================================================
"""

def change_num(n):                                      # n을 표준형으로 바꾸는 함수
    result=""                                           # 표준형 전화번호
    for i in n:                                         # n리스트 요소들을 차례대로 변수 i에 대입
       if i == '-' : pass                               # i가 '-'일 경우 통과
       else : result += i                               # 아닐경우, result에 i추가
       if len(result) == 3 : result += '-'              # result의 길이가 3일 경우, result에 '-'추가
    return result                                       # result 값 반환

num = input('input = ').split(',')

num_list = list(map(change_num,num))            
num_list_clear = list(set(num_list))                    # num_list의 중복 요소 제거


for i in num_list_clear :                               # num_list_clear리스트 요소들을 차례대로 i 변수에 대입
    print(i,end = " ")                                  # i와 i값의 개수를 한줄에 출력할 수 있도록 end=' '를 사용
    if num_list.count(i) == 1 : print("No duplicates")  # num_list의 i값 개수가 1일 경우 No duplicates 출력
    else :print(num_list.count(i))                      # 아닐경우, num_list의 i값 개수 출력

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

def change_alphabet(n):                         # n을 표준형 전화번호로 바꾸는 함수
    result=""                                   # 표준형 전화번호
    for i in n:                                 # n리스트 요소들을 차례대로 변수 i에 대입
        if i == '-' : pass                      # i가 '-'일 경우 통과
        elif i in ['A','B','C'] : result += '2' # i가 'A','B','C'일 경우, result에 2추가
        elif i in ['D','E','F'] : result += '3' # i가 'D','E','F'일 경우, result에 3추가
        elif i in ['G','H','I'] : result += '4' # i가 'G','H','I'일 경우, result에 4추가
        elif i in ['J','K','L'] : result += '5' # i가 'J','K','L'일 경우, result에 5추가
        elif i in ['M','N','O'] : result += '6' # i가 'M','N','O'일 경우, result에 6추가
        elif i in ['P','R','S'] : result += '7' # i가 'P','R','S'일 경우, result에 7추가
        elif i in ['T','U','V'] : result += '8' # i가 'T','U','V'일 경우, result에 8추가
        elif i in ['W','X','Y'] : result += '9' # i가 'W','X','Y'일 경우, result에 9추가
        else :result += i                       # i가 '-'나 알파벳이 아닐 경우, result에 i추가

        if len(result) == 3 : result += '-'     # result의 길이가 3일 경우, result에 '-'추가
    return result                               # result 값 반환

count = int(input('입력받을 전화번호 수 = '))    # 입력받을 전화번호 수 
num = []                # 전화번호 리스트

for i in range(0,count) :                       # count수만큼 반복
    num.append(input('전화번호 = '))            # input을 num리스트에 추가


num_list = list(map(change_alphabet,num))
num_list_clear = list(set(num_list))            # num_list의 중복 요소 제거


for i in num_list_clear:                        # num_list_clear리스트 요소들을 차례대로 i 변수에 대입
    print(i,end = " ")                          # i와 i값의 개수를 한줄에 출력할 수 있도록 end=' '를 사용
    if num_list.count(i) != 1 :
        print(num_list.count(i))                # num_list의 i값 개수가 1일 경우, num_list의 i값 개수 출력