"""
위 그림은 {5,2,4,6,1,3} 이라는 배열을 소트하는 방법을 보여준다.
배열의 두번째 인덱스부터 시작하여 시작한 인덱스(검정색 블록) 좌측의 항목 중 자신이 들어가야 할 위치를 판단(소트되도록)하여 이동 한다.
좌측의 배열 요소들은 본인보다 좌측에 값이 삽입되어 들어올 경우 한칸씩 우측으로 이동한다. 단, 삽입되어 들어오는 요소(그림에서 검정색 블록)가 있던 인덱스(원래의 위치)까지만 이동한다.
마지막 인덱스까지 위 과정을 반복한다.
이와 같은 기능을 하는 소트 프로그램을 작성하시오.

그림 설명 : http://codingdojang.com/scode/443?answer_mode=hide
"""
"""
=============================================================================
과제 1. 위 문제의 알고리즘으로 배열을 정렬하시오. 
       - 조건 : 결과값을 저장하기 위해 새로운 리스트를 생성할 수 없다.
       - input = [5,2,6]
       - 출력 : [2,5,6]
=============================================================================
"""

def insertion_sort(sort):                                   # list.sort : 오름차 순으로 정렬 
    for x in range(1,len(sort)):                            # 1부터 sort 길이만큼 반복
        for a in range(len(sort)):                          # sort 길이만큼 반복
            if int(sort[a]) > int(sort[x]):                 # sort리스트의 a번째 값이 sort x번째 값보다 클 경우,
                sort[a],sort[a+1:x+1] = sort[x],sort[a:x]   # sort a번째 값, sort a+1번째 값부터 x번째값까지 = sort x번째값, sort a부터 x-1번째 값까지
                break                                       # 반복문 멈춤
    return ",".join(sort)                                   # sort를 ', '구분자로 합친 후 반환
   
num = input('input = ').split(',')                          # input 값을 ','구분자로 나누기
print('출력 : ', insertion_sort(num))                       # a를 insertion_sort 함수에 대입 후 출력

'''
input = 5,2,6

sort = ['5', '2', '6']

x = 1
a = 0
sort[a] = sort[0] = 5
sort[x] = sort[1] = 2

sort[a],sort[a+1:x+1] = sort[x],sort[a:x]
sort[0],sort[1:2] = sort[1], sort[0:1]
sort[0],sort[1] = sort[1], sort[0]
sort = ['2', '5', '6']

x = 2
a = 0
a = 1
a = 2
'''

"""
=============================================================================
과제 2. 위 문제의 알고리즘으로 배열을 정렬하시오
       - 조건 : 결과값을 저장하기 위해 새로운 리스트를 생성할 수 없다.
       - input = [5,2,4,6,1,3]
       - 출력 : [1,2,3,4,5,6]
=============================================================================
"""
def insertion_sort(sort):                                   # list.sort : 오름차 순으로 정렬 
    for x in range(1,len(sort)):                            # 1부터 sort 길이만큼 반복
        for a in range(len(sort)):                          # sort 길이만큼 반복
            if int(sort[a]) > int(sort[x]):                 # sort리스트의 a번째 값이 sort x번째 값보다 클 경우,
                sort[a],sort[a+1:x+1] = sort[x],sort[a:x]   # sort a번째 값, sort a+1번째 값부터 x번째값까지 = sort x번째값, sort a부터 x-1번째 값까지
                break                                       # 반복문 멈춤
    return ",".join(sort)                                   # sort를 ', '구분자로 합친 후 반환
   
num = input('input = ').split(',')                          # input 값을 ','구분자로 나누기
print('출력 : ', insertion_sort(num))                       # a를 insertion_sort 함수에 대입 후 출력
'''
input = 5,2,4,6,1,3
sort = ['5', '2', '4', '6', '1', '3']
x = 1
a = 0
sort[a] =  5 > sort[x] =  2
sort[a],sort[a+1:x+1] =  sort[x],sort[a:x] =  2, 5
sort = ['2', '5', '4', '6', '1', '3']

x = 2
a = 0
a = 1
sort[a] =  5 > sort[x] =  4
sort[a],sort[a+1:x+1] =  sort[x],sort[a:x] =  4, 5
sort = ['2', '4', '5', '6', '1', '3']

x = 3
a = 0
a = 1
a = 2
a = 3
a = 4
a = 5

x = 4
a = 0
sort[a] =  2 > sort[x] =  1
sort[a],sort[a+1:x+1] =  sort[x],sort[a:x] =  1 ['2', '4', '5', '6'] 
sort = ['1', '2', '4', '5', '6', '3']

x = 5
a = 0
a = 1
a = 2
sort[a] =  4 > sort[x] =  3
sort[a],sort[a+1:x+1] = sort[x],sort[a:x] =  3 ['4', '5', '6']
sort = ['1', '2', '3', '4', '5', '6']

출력 :  1,2,3,4,5,6
'''