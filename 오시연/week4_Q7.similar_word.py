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

def OneEditApart(s1, s2):
    if len(s1) == len(s2):        #문자열 길이 같을 경우
        for i in range(len(s1)):  #문자열 길이만큼 반복
            s1_change = s1[:i] + s1[i+1:]   #i번째 인덱스를 제외한 문자열을 변수에 담았을 때 두 문자열이 같아지는지 확인
            s2_change = s2[:i] + s2[i+1:] 
            if s1_change == s2_change:
                return True
        return False
    elif len(s1) > len(s2):      #s1에서 문자 1개를 제거했을 때 s2와 같아지는지 확인
        for i in range(len(s1)): #s1 길이만큼 반복
            s1_change = s1[:i] + s1[i+1:]  #i번째 인덱스를 제외한 문자열을 변수에 담고 같아지는지 확인
            if s1_change == s2:
                return True
        return False
    elif len(s1) < len(s2):      #s2에서 문자 1개를 제거했을 때 s1과 같아지는지 확인
        for i in range(len(s2)): #s2 길이만큼 반복
            s2_change = s2[:i] + s2[i+1:] #첫글자 제외 담음(ats), 두번째글자 제외 담음(cts), 세번째글자 제외 담음(cas), 끝글자 제외 담음(cat)
            if s1 == s2_change:   #동일할 때 
                return True
        return False
    
print(OneEditApart('cat', 'cats'))


"""
=============================================================================
과제2. s1을 기준으로 한개의 문자를 삽입, 제거, 변환하였을 경우 s2가 나올 수 있는지 판별하시오.
       - 조건 : 문자열에서 문자 1개를 삽입, 제거, 변환할 수 있는 횟수는 총 1회이다. (예 : 삽입과 제거 동시 사용 불가능)
       - s1 = ‘cat’
       - s2 =‘acts’
       - 출력 = false
=============================================================================
"""
def OneEditApart(s1, s2):
    if len(s1) == len(s2):        #문자열 길이 같을 경우
        for i in range(len(s1)):  #문자열 길이만큼 반복
            s1_change = s1[:i]+s1[i+1:]   #i번째 인덱스를 제외한 문자열을 변수에 담았을 때 두 문자열이 같아지는지 확인
            s2_change = s2[:i]+s2[i+1:] 
            if s1_change == s2_change:
                return True
        return False
    elif len(s1) > len(s2):      #s1에서 문자 1개를 제거했을 때 s2와 같아지는지 확인
        for i in range(len(s1)): #s1 길이만큼 반복
            s1_change = s1[:i]+s1[i+1:]  #i번째 인덱스를 제외한 문자열을 변수에 담고 같아지는지 확인
            if s1_change == s2:
                return True
        return False
    elif len(s1) < len(s2):      #s2에서 문자 1개를 제거했을 때 s1과 같아지는지 확인
        for i in range(len(s2)): #s2 길이만큼 반복
            s2_change = s2[:i] + s2[i+1:] #첫글자 제외 담음(ats), 두번째글자 제외 담음(cts), 세번째글자 제외 담음(cas), 끝글자 제외 담음(cat)
            if s1 == s2_change:   #동일할 때 
                return True
        return False
    
print(OneEditApart('cat', 'acts'))