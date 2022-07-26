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

def OneEditApart (s1, s2): #함수에 s1과 s2를 넣는다.
    if len(s1) == len(s2): #만약에 s1과 s2의 길이가 같다면
        for i in range (len(s1)): #길이만큼 돌린다.
            compare_s1 = s1[:i] + s1[i+1:] #비교단어1는 s1 단어의 조합이 된다.
            compare_s2 = s2[:i] + s2[i+1:] #비교단어2는 s2 단어의 조합이 된다.
            if compare_s1 == compare_s2: #만약 비교단어1과 비교단어2가 같다면
                return True 
        return False

    elif len(s1) > len(s2): #길이가 s1이 더 크다면
        for i in range (len(s1)): #길이만큼 돌린다.
            compare_s1 = s1[:i] + s1[i+1:] #비교단어1는 첫번째 단어들의 조합이 된다.
            if compare_s1 == s2: #만약 비교단어1가 두번째 단어와 같다면 
                return True #True가 나오고
        return False #아니라면 False가 나온다
    
    elif len(s1) < len(s2): #길이가 s2와 같다면 
        for i in range (len(s2)): #길이만큼 돌린다. 
            compare_s2 = s2[:1] + s2[i+1:] #비교하고 싶은 단어는 두번째 단어들의 조합으로 만들어진다.
            if s1 == compare_s2: #s1와 비교하고 싶은 단어가 같다면
                return True #True가 나오고
        return False #아니라면 False가 나온다.

s1 = input("첫번째 단어를 입력하세요: ")
s2 = input("두번째 단어를 입력하세요: ")

print (OneEditApart(s1, s2))



"""
=============================================================================
과제2. s1을 기준으로 한개의 문자를 삽입, 제거, 변환하였을 경우 s2가 나올 수 있는지 판별하시오.
       - 조건 : 문자열에서 문자 1개를 삽입, 제거, 변환할 수 있는 횟수는 총 1회이다. (예 : 삽입과 제거 동시 사용 불가능)
       - s1 = ‘cat’
       - s2 =‘acts’
       - 출력 = false
=============================================================================
""" 

def OneEditApart (s1, s2): #함수에 s1과 s2를 넣는다.
    if len(s1) == len(s2): #만약에 s1과 s2의 길이가 같다면
        for i in range (len(s1)): #길이만큼 돌린다.
            compare_s1 = s1[:i] + s1[i+1:] #비교단어1는 s1 단어의 조합이 된다.
            compare_s2 = s2[:i] + s2[i+1:] #비교단어2는 s2 단어의 조합이 된다.
            if compare_s1 == compare_s2: #만약 비교단어1과 비교단어2가 같다면
                return True 
        return False

    elif len(s1) > len(s2): #길이가 s1이 더 크다면
        for i in range (len(s1)): #길이만큼 돌린다.
            compare_s1 = s1[:i] + s1[i+1:] #비교단어1는 첫번째 단어들의 조합이 된다.
            if compare_s1 == s2: #만약 비교단어1가 두번째 단어와 같다면 
                return True #True가 나오고
        return False #아니라면 False가 나온다
    
    elif len(s1) < len(s2): #길이가 s2와 같다면 
        for i in range (len(s2)): #길이만큼 돌린다. 
            compare_s2 = s2[:1] + s2[i+1:] #비교하고 싶은 단어는 두번째 단어들의 조합으로 만들어진다.
            if s1 == compare_s2: #s1와 비교하고 싶은 단어가 같다면
                return True #True가 나오고
        return False #아니라면 False가 나온다.

s1 = input("첫번째 단어를 입력하세요: ")
s2 = input("두번째 단어를 입력하세요: ")

print (OneEditApart(s1, s2))