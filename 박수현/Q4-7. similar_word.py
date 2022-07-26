"""
아래와 같은 결과를 출력하는 function을 구현하라

bool OneEditApart(string s1, string s2)

OneEditApart("cat", "dog") = false
OneEditApart("cat", "cats") = true
OneEditApart("cat", "cut") = true
OneEditApart("cat", "cast") = true
OneEditApart("cat", "at") = true
OneEditApart("cat", "acts") = false
한개의 문자를 삽입, 제거, 변환을 했을때 s1, s2가 동일한지를 판별하는 OneEditApart 함수를 작성하시오.


"""
"""
=============================================================================
과제1. s1을 기준으로 한개의 문자를 삽입, 제거, 변환하였을 경우 s2가 나올 수 있는지 판별하시오.
        - 조건 : 문자열에서 문자 1개를 삽입, 제거, 변환할 수 있는 횟수는 총 1회이다. (예 : 삽입과 제거 동시 사용 불가능)
        - s1 = ‘cat’
        - s2 =‘cats’
        - 출력 = true
=============================================================================
"""

# OneEditApart 함수 정의 (변수는 s1, s2)
def OneEditApart(s1, s2):
    count_num = 0                                       # count_num = 횟수 카운트 (시작은 0)

    if len(s1) == len(s2):                              # 만약 s1과 s2의 길이가 같다면, 다음 행위 반복
        for i, j in zip(s1, s2):
            if not i == j:                              # 동일한 위치에 다른 문자가 있다면, 카운트
                count_num += 1
        if 1 < count_num:                               # 만약 횟수가 1보다 크다면, flag = 1
            flag = 1
        else:                                           # 만약 횟수가 0 혹은 1이라면, flag = 2
            flag = 2

    elif len(s1) < len(s2):                             # 만약 s2의 길이가 더 길다면, 다음 행위 반복
        for i in range(len(s2)):
            change_s2 = s2[:i] + s2[i + 1:]             # change_s2 = 특정 위치를 기준으로 슬라이스한 후 하나 빼고 붙이기
            if change_s2 == s1:                         # 만약 change_s2와 s1이 같다면, 카운드
                count_num += 1
        if count_num == 0:                              # 만약 카운트한 횟수가 없다면, flag = 1
            flag = 1
        else:                                           # 만약 카운트한 횟수가 있다면, flag = 2
            flag = 2

    elif len(s2) < len(s1):                             # 만약 s1의 길이가 더 길다면, 다음 행위 반복
        for i in range(len(s1)):
            change_s1 = s1[:1] + s1[i + 1:]             # change_s1 = 특정 위치를 기준으로 슬라이스한 후 하나 빼고 붙이기
            if change_s1 == s2:                         # 만약 change_s1과 s2가 같다면, 카운트
                count_num += 1
        if count_num == 0:                              # 만약 카운트한 횟수가 없다면, flag = 1
            flag = 1
        else:                                           # 만약 카운트한 횟수가 있다면, flag = 2
            flag = 2

    if flag == 1:                                       # 최종적으로 flag = 1이라면, false 출력
        print('false')
    if flag == 2:                                       # 최종적으로 flag = 2라면, true 출력
        print('true')

if __name__ == '__main__':
    # s1, s2 = 각각의 문자
    s1 = input('첫번째 문자를 입력하세요 : ')
    s2 = input('두번째 문자를 입력하세요 : ')

    OneEditApart(s1, s2)                                # OneEditApart 실행
    print()

"""
=============================================================================
과제2. s1을 기준으로 한개의 문자를 삽입, 제거, 변환하였을 경우 s2가 나올 수 있는지 판별하시오.
        - 조건 : 문자열에서 문자 1개를 삽입, 제거, 변환할 수 있는 횟수는 총 1회이다. (예 : 삽입과 제거 동시 사용 불가능)
        - s1 = ‘cat’
        - s2 =‘acts’
        - 출력 = false
=============================================================================
"""

if __name__ == '__main__':
    # s1, s2 = 각각의 문자
    s1 = input('첫번째 문자를 입력하세요 : ')
    s2 = input('두번째 문자를 입력하세요 : ')

    OneEditApart(s1, s2)                                # OneEditApart 실행