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
# 과제2와 코드 동일

"""
=============================================================================
과제2. s1을 기준으로 한개의 문자를 삽입, 제거, 변환하였을 경우 s2가 나올 수 있는지 판별하시오.
       - 조건 : 문자열에서 문자 1개를 삽입, 제거, 변환할 수 있는 횟수는 총 1회이다. (예 : 삽입과 제거 동시 사용 불가능)
       - s1 = ‘cat’
       - s2 =‘acts’
       - 출력 = false
=============================================================================
"""
def checkRemoval(s1, s2):           # (제거) 한 글자씩 제거해보며 두 단어가 일치하는지 확인하는 함수
    for i in range(len(s1)):        # s1이라는 단어에서 한 글자씩 꺼내는 반복문
        t = s1[:i]+s1[i+1:]         # 변수 t는 s1의 해당 글자를 제외한 나머지를 하나로 합친 것
        if s2==t: return True       # t와 s2가 같은 경우가 있다면 s2는 s1에서 한 단어를 제거한 것과 같으므로 True 반환
    return False                    # for문을 범위만큼 반복해도 True가 나오지 않으면 False

def checkReplace(s1, s2):           # (변환) 다른 글자 한 개만 다른지 확인하는 함수
    for i in range(len(s1)):        # s1이라는 단어에서 한 글자씩 꺼내는 반복문
        t1 = s1[:i]+s1[i+1:]        # 변수 t1은 s1의 해당 글자를 제외한 나머지를 하나로 합친 것
        t2 = s2[:i]+s2[i+1:]        # 변수 t2는 s2의 (동일)
        if t1==t2: return True      # t1과 t2가 같다면 두 단어는 한 글자만 다른 것
    return False                    # for문을 범위만큼 반복해고 True가 나오지 않으면 False

def OneEditApart(s1, s2):           # OneEditApart 함수
    if len(s1) > len(s2):           # s1이 더 긴 경우 s2가 s1에서 한 글자를 제거한 것과 같은지 확인
        return checkRemoval(s1, s2)
    elif len(s1) < len(s2):         # s2가 더 긴 경우 s2가 s1에서 한 글자를 추가한 것과 같은지 확인
        return checkRemoval(s2, s1)
    else:                           # 길이가 같은 경우 한 글자만 다른지 확인
        return checkReplace(s1, s2)

s1 = input()
s2 = input()

print(OneEditApart(s1, s2))