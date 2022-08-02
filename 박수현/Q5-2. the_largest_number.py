"""
음수가 아닌 수들이 주어졌을 때 그 수들을 이어서 만들 수 있는 가장 큰 수를 구하시오.

예를 들어 [1,2,3]이 주어졌을 때 만들 수 있는 가장 큰 수는 321이고, [3, 30, 34, 5, 9] 가 주어지면 만들 수 있는 가장 큰 수는 9534330이다.
"""
"""
========================================================================
과제1. 아래에 입력이 num_list로 주어졌을 때, 그 수들을 이어서 만들 수 있는 가장 큰 수인 출력값을 구하시오. 
        - 조건 1. 입력된 숫자들은 음수가 아닌 자연수
        - num_list = [1, 2, 3] 
        - 출력값 : 321
========================================================================
"""

# num_list = 자연수에 대한 리스트 (','을 기준으로 분해)
num_list = input('음수가 아닌 수들을 입력하세요 : ').split(', ')

for i in num_list:                # num_list의 하나씩 다음 행위 반복
    if '-' in i:                  # 만약 음수가 있다면, 예외 발생시키기
        raise Exception('잘못 입력했습니다. (음수가 아닌 자연수)')

num_list.sort(reverse = True)     # num_list 내림차순 정렬
print(''.join(num_list))          # 만들 수 있는 가장 큰 수 출력
print()

"""
========================================================================
과제2. 아래에 입력이 num_list로 주어졌을 때, 그 수들을 이어서 만들 수 있는 가장 큰 수인 출력값을 구하시오. 
        - 조건 1. 입력된 숫자들은 음수가 아닌 자연수
        - 조건 2. 아래와 같은 입력값을 도출하시오. 
        - num_list = [3, 30, 34, 5, 9] 
        - 출력값 : 9,534,330
========================================================================
"""

# 리스트를 사용해 만들 수 있는 가장 큰 수를 구하는 프로그램 정의
def is_the_largest_num(num_list):
    for i in num_list:                      # num_list의 하나씩 다음 행위 반복
        if '-' in i:                        # 만약 음수가 있다면, 예외 발생시키기
            raise Exception('잘못 입력했습니다. (음수가 아닌 자연수)')

    num_list.sort(reverse = True)           # num_list 내림차순 정렬
    new_list = num_list[:]                  # new_list에 num_list 복사
    for i in range(1, len(new_list)):       # 1부터 길이만큼 다음 행위 반복
        for j in range(i):                  # i만큼 다음 행위 반복
        # 만약 앞 위치 값과 첫 자리가 같은데, 길이는 다르고, 그 값의 1의 자리 수보다 큰 수가 있다면, 순서 바꾸기
        # ex. [31, 33, 3, 34, 30] > [34, 33, 3, 30, 31]
            if new_list[j][0] == new_list[i][0] and len(new_list[i]) < len(new_list[j]) and new_list[j][-1] < new_list[i][0]:
                new_list.insert(j, new_list[i])
                new_list.pop(i + 1)
                
                num_list = new_list         # num_list에 new_list 복사

    largest_num = ''.join(num_list)         # 만들 수 있는 가장 큰 수 출력
    print('{:,}'.format(int(largest_num)))

if __name__ == '__main__':
    # num_list = 자연수에 대한 리스트 (','을 기준으로 분해)
    num_list = input('음수가 아닌 수들을 입력하세요 : ').split(', ')

    is_the_largest_num(num_list)            # 가장 큰 수를 구하는 프로그램 실행