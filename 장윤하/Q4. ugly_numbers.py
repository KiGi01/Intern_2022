'''
심술쟁이 수는 2,3,5의 곱으로 만들 수 있는 수이다. 다음과 같은 순서의 수가 11개의 심술쟁이 수이다.

1,2,3,4,5,6,8,9,10,12,15,....
처음 수는 1로 시작하도록 한다. 입력은 받지 않고, <number> 에 1500번째 심술쟁이 수가 출력되게 한다.

Sample Output

The 1500'th ugly number is <number>.
답

859963392
(1550번째는 1093500000, 십만번째는 290142196707511001929482240000000000000)
'''
"""     
========================================================================
과제1. 숫자 2,3,5의 곱으로 만들 수 있는 수 작은 순서대로 11개를 출력하시오. 
      - 출력 : 1,2,3,4,5,6,8,9,10,12,15
========================================================================
"""
n = int(input("출력할 수의 개수를 입력하세요: "))   # 출력할 수의 개수를 입력
result = [1]                                   # ugly number를 저장할 리스트 생성
while True:                                         # 무한 루프
    multi_lst = []                                  # 배수 리스트 생성
    for r in result:                                # Ugly number 반복
        for t in  r * 2, r * 3, r * 5:              # result에 저장된 값을 계속해서 곱한다.
            if t > result[-1]:                      # 리스트의 마지막 요소보다 클 경우 (중복을 피하기 위해)
                multi_lst.append(t)                 # 해당 숫자를 추가
    result.append(min(multi_lst))                   # 최종 결과 리스트에 배수 중 가장 작은 수를 추가

    if len(result) == n:                            # 원하는 길이와 같아질 경우 리스트 프린트하고 루프 중단
        print(result)
        break


"""
========================================================================
과제2. 숫자 2,3,5의 곱으로 만들 수 있는 수를 오름차순으로 정렬할 경우 1550번째 값을 구하시오. 
      - 출력 : 1,093,500,000
========================================================================
"""
n = int(input("출력할 수의 개수를 입력하세요: "))   # 출력할 수의 개수를 입력
result = [1]                                   # ugly number를 저장할 리스트 생성
while True:                                         # 무한 루프
    multi_lst = []                                  # 배수 리스트 생성
    for r in result:                                # Ugly number 반복
        for t in  r * 2, r * 3, r * 5:              # result에 저장된 값을 계속해서 곱한다.
            if t > result[-1]:                      # 리스트의 마지막 요소보다 클 경우 (중복을 피하기 위해)
                multi_lst.append(t)                 # 해당 숫자를 추가
    result.append(min(multi_lst))                   # 최종 결과 리스트에 배수 중 가장 작은 수를 추가

    if len(result) == n:                            # 원하는 길이와 같아질 경우 리스트 마지막 값 프린트하고 루프 중단
        print(result[-1])
        break
