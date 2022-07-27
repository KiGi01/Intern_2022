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

def checkRemoval(a1, a2):           # 제거 확인 함수
    for i in range(len(a1)):        # a1의 길이만큼 반복
        t = a1[:i]+a1[i+1:]         # t는 (a1의 처음부터 i-1까지) + (a1의 i+1부터 끝까지)
        if a2==t: return True       # 만약 a2가 t와 같다면 true 반환
    return False

def checkadd(b1, b2):               # 삽입 확인 함수
    for i in range(len(b2)):        # b2의 길이만큼 반복
        t = b2[:i]+b2[i+1:]         # t는 (b2의 처음부터 i-1까지) + (b2의 i+1부터 끝까지)
        if b1==t: return True       # 만약 b2가 t와 같다면 true 반환
    return False

def checkReplace(c1, c2):           # 변환 확인 함수
    for i in range(len(c1)):        # c1의 길이만큼 반복
        t1 = c1[:i]+c1[i+1:]        # t1 = c1의 '처음부터i-1오프셋까지' + c1의 'i+1오프셋부터 끝까지'
        t2 = c2[:i]+c2[i+1:]        # t2 = c2의 '처음부터i-1오프셋까지' + c2의 'i+1오프셋부터 끝까지'
        if t1==t2: return True      # t1과 t2의 값이 같을 경우 True 반환
    return False

def decide_check(n1, n2):           # n1을 기준으로 삽입,제거,변환 판단하는 함수
    if len(n1) > len(n2):           # n1의 길이가 n2보다 클 경우,
        return checkRemoval(n1, n2) # checkRemovla(n1, n2) 값 반환
    elif len(n1) < len(n2):         # n1의 길이가 n2보다 작을 경우,
        return checkadd(n1, n2)     # checkadd(n1, n2) 값 반환
    else:                           # 두 조건에 해당하지 않을 경우,
        return checkReplace(n1, n2) # checkReplace(n1, n2) 값 반환

s1 = input('s1 = ')
s2 = input('s2 = ')
print(decide_check(s1, s2))         # decide_check(s1, s2) 출력

"""
=============================================================================
과제2. s1을 기준으로 한개의 문자를 삽입, 제거, 변환하였을 경우 s2가 나올 수 있는지 판별하시오.
       - 조건 : 문자열에서 문자 1개를 삽입, 제거, 변환할 수 있는 횟수는 총 1회이다. (예 : 삽입과 제거 동시 사용 불가능)
       - s1 = ‘cat’
       - s2 =‘acts’
       - 출력 = false
=============================================================================
"""
def checkRemoval(a1, a2):           # 제거 확인 함수
    for i in range(len(a1)):        # a1의 길이만큼 반복
        t = a1[:i]+a1[i+1:]         # t는 (a1의 처음부터 i-1까지) + (a1의 i+1부터 끝까지)
        if a2==t: return True       # 만약 a2가 t와 같다면 true 반환
    return False
    
def checkReplace(c1, c2):           # 변환 확인 함수
    for i in range(len(c1)):        # c1의 길이만큼 반복
        t1 = c1[:i]+c1[i+1:]        # t1 = c1의 '처음부터i-1오프셋까지' + c1의 'i+1오프셋부터 끝까지'
        t2 = c2[:i]+c2[i+1:]        # t2 = c2의 '처음부터i-1오프셋까지' + c2의 'i+1오프셋부터 끝까지'
        if t1==t2: return True      # t1과 t2의 값이 같을 경우 True 반환
    return False

def decide_check(n1, n2):           # n1을 기준으로 삽입,제거,변환 판단하는 함수
    if len(n1) > len(n2):           # n1의 길이가 n2보다 클 경우,
        return checkRemoval(n1, n2) # checkRemovla(n1, n2) 값 반환
    elif len(n1) < len(n2):         # n1의 길이가 n2보다 작을 경우,
        return checkRemoval(n2, n1) # checkRemoval(n2, n1) 값 반환
    else:                           # 두 조건에 해당하지 않을 경우,
        return checkReplace(n1, n2) # checkReplace(n1, n2) 값 반환

s1 = input('s1 = ')
s2 = input('s2 = ')
print(decide_check(s1, s2))         # decide_check(s1, s2) 출력