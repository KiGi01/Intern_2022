"""
시저 암호는, 고대 로마의 황제 줄리어스 시저가 만들어 낸 암호이다.
예를 들어 알파벳 A를 입력했을 때, 그 알파벳의 n개 뒤에 오는 알파벳이 출력되는 것이다.
예를 들어 바꾸려는 단어가 'CAT"고, n을 5로 지정하였을 때 "HFY"가 되는 것이다.
어떠한 암호를 만들 문장과 n을 입력했을 때 암호를 만들어 출력하는 프로그램을 작성해라.
"""

"""
==========================================================================
# 과제 1. 대문자로 구성된 단어 1개를 입력받을 경우를 가정하여 시저 암호를 만드세요. input() 함수를 사용하세요.
## input = "ICL"
## n = 3
## 출력 : LFO
==========================================================================
==========================================================================
# 과제 2. 대문자와 소문자로 구성된 단어 1개를 입력받을 경우를 가정하여 시저 암호를 만드세요. input() 함수를 사용하세요.
## input = "Library"
## n = 5
## 출력 : Qngwfd
==========================================================================
==========================================================================
# 과제 3. 대문자와 소문자를 포함하는 문장을 입력받을 경우를 가정하여 시저 암호를 만드세요. input() 함수를 사용하세요.
## input = "MMy subject is Library & Information Science."
## n = 2
## 출력 : Oa uwdlgev ku Nkdtcta & Kphqtocvkqp Uekgpeg.
==========================================================================
"""
#1 
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 알파벳 대문자로 구성된 리스트 생성
a = input("input = ").upper() # 대문자로 입력
n = 3

for i in a: # 문자열 반복
    for j in range(len(alpha)): # 리스트 개수만큼 반복
        if i == alpha[j]: # 문자가 리스트에 있는 경우
            print(alpha[(j+3)%26],end='') # 26으로 나눌 경우 26보다 작은 수는 그대로 출력, 26이상은 나머지 출력
            
#2

alpha_low = 'abcdefghijklmnopqrstuvwxyz' # 소문자로 구성된 알파벳 리스트
alpha_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 대문자로 구성된 알파벳 리스트 
a = input("input_1 = ") # 입력
n = 5
lst=[] # lst 생성



for i in a: # 문자열 반복
    if i.isupper(): # 입력 받은 문자가 대문자인 경우
        for j in range(len(alpha_up)): # 알파벳 개수만큼 반복
            if i == alpha_up[j]:       # 문자가 리스트에 있는 경우
                lst.append(alpha_up[(j+5)%26]) # lst 리스트에 문자 추가
    else:
        for j in range(len(alpha_low)):
            if i == alpha_low[j]:
                lst.append(alpha_low[(j+5)%26])
                    
print(''.join(lst)) # 리스트를 하나의 문자열로 합쳐서 출력


#3
alpha_low = 'abcdefghijklmnopqrstuvwxyz'
alpha_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = input("input_1 = ")
n = 2
lst=[]



for i in a:
    if i.isupper():
        for j in range(len(alpha_up)): # 대문자인 경우 lst에 추가
            if i == alpha_up[j]:
                lst.append(alpha_up[(j+2)%26])
    elif i.islower():
        for j in range(len(alpha_low)): # 소문자인 경우 lst에 추가 
            if i == alpha_low[j]:
                lst.append(alpha_low[(j+2)%26])
    else: # 특수기호는 그대로 저장
        lst.append(i)                
print(''.join(lst))
            
