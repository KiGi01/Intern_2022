"""
-----------------  Question  -----------------
어떤 정수 n에서 시작해, n이 짝수면 2로 나누고, 홀수면 3을 곱한 다음 1을 더한다.
이렇게 해서 새로 만들어진 숫자를 n으로 놓고, n=1 이 될때까지 같은 작업을 계속 반복한다.
예를 들어, n=22이면 다음과 같은 수열이 만들어진다.
- 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
n이라는 값이 입력되었을때 1이 나올때까지 만들어진 수의 개수(1을 포함)를 n의 사이클 길이라고 한다.
위에 있는 수열을 예로 들면 22의 사이클 길이는 16이다.
i와 j라는 두개의 수가 주어졌을때, i와 j사이의 모든 수(i, j포함)에 대해 최대 사이클 길이를 구하라.
----------------------------------------------
"""
"""
=============================================================================
과제 1. 입력 값(n)이 40일때, 사이클 길이를 구하시오.
       - input = 40
       - 출력 : 9
=============================================================================
"""

def CylcleLength(n):
    result = 1
    while n != 1:
        if n%2: #홀수
            n = n*3+1
        else:
            n /= 2
        result += 1

    return result

#print('Cylcle Length:', CylcleLength(22))
print('Cylcle Length:', CylcleLength(40)) #9


"""
=============================================================================
과제 2. i와 j라는 두개의 수가 주어졌을때, i와 j사이의 모든 수에 대한 최대 사이클 길이(i와 j도 사이클 길이에 포함됨)를 구하라.
       - start = 1
       - end = 10
       - 출력 : 20
=============================================================================
"""

def MaxCylcleLength(i, j):
    result = []
    for z in range(i, j+1):
        #print("z: ", z)
        #print("CylcleLength: ", CylcleLength(z))
        result.append(CylcleLength(z))
    result = max(result)
    return result


print('Maximum Cylcle Length:',  MaxCylcleLength(1, 10))



"""
=============================================================================
과제 3. i와 j라는 두개의 수가 주어졌을때, i와 j사이의 모든 수에 대한 최대 사이클 길이(i와 j도 사이클 길이에 포함됨)를 구하라.
       - start_num_list = [1, 100, 201, 900]
       - end_num_list = [10, 200, 210, 1000] 
       - 출력 : [20, 125, 89, 174]
=============================================================================
"""

def MaxCylcleLength_list(zip_ij):
    result = []
    for i, j in zip_ij:
        #print('Maximum Cylcle Length:', MaxCylcleLength(i,j))
        result.append( MaxCylcleLength(i,j))
    return result


start_num_list = [1, 100, 201, 900]
end_num_list = [10, 200, 210, 1000] 
print(MaxCylcleLength_list( zip(start_num_list,end_num_list)))

