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

def oneEditApart(s1, s2):     #함수 생성
    s1 = list(s1) 
    s2 = list(s2)
    if len(s1)+1 <len(s2):   
        result = False
    elif len(s1)-1 >len(s2):
        result = False    
    
    elif len(s1)+1 == len(s2):    # 제거하는 경우
        for i in range(len(s2)):
            if not(s2[i] in s1):
                del s2[i] 
                if s2 == s1:   # s2의 다른 문자 제거 시, 반드시 s1과 같아져야 함 
                    result = True
                    break
                else:
                    result = False
    
    elif len(s1)-1 == len(s2): # 삽입하는 경우
        idx_s1 = []
        for i in range(len(s2)):
            if not(s2[i] in s1):
                result = False   #s2는 무조건 s1에 있어야하므로
                break
            else:
                idx = s1.index(s2[i])
                idx_s1.append(idx)
        
        if idx_s1 == sorted(idx_s1): #append된 s1인덱스 순서가 오름차순이어야  s2에 문자1개 삽입만으로 s1가 같아질 수 있음
            result = True
        else:
            result = False
               
    elif len(s1) == len(s2):    # 변환하는 경우
        cnt = 0
        for i in range(len(s2)):
            if s1[i] == s2[i]:
                cnt +=1
        if cnt == len(s2)-1: 
            result = True
        else:
            result = False
    
    return result



s1 ='cat'
s2 ='cats'
print(oneEditApart(s1,s2))



"""
=============================================================================
과제2. s1을 기준으로 한개의 문자를 삽입, 제거, 변환하였을 경우 s2가 나올 수 있는지 판별하시오.
       - 조건 : 문자열에서 문자 1개를 삽입, 제거, 변환할 수 있는 횟수는 총 1회이다. (예 : 삽입과 제거 동시 사용 불가능)
       - s1 = ‘cat’
       - s2 =‘acts’
       - 출력 = false
=============================================================================
"""

s1 ='cat'
s2 ='acts'
print(oneEditApart(s1,s2))



print( oneEditApart("cat", "dog") )  # false
print( oneEditApart("cat", "cats"))  # true
print( oneEditApart("cat", "cut") )  # true


print( oneEditApart("cat", "cast"))  # true


print( oneEditApart("cat", "at") )   # true
print( oneEditApart("cat", "acts"))  # false



