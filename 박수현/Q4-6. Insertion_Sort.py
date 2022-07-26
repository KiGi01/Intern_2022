"""
위 그림은 {5,2,4,6,1,3} 이라는 배열을 소트하는 방법을 보여준다.
배열의 두번째 인덱스부터 시작하여 시작한 인덱스(검정색 블록) 좌측의 항목 중 자신이 들어가야 할 위치를 판단(소트되도록)하여 이동 한다.
좌측의 배열 요소들은 본인보다 좌측에 값이 삽입되어 들어올 경우 한칸씩 우측으로 이동한다. 단, 삽입되어 들어오는 요소(그림에서 검정색 블록)가 있던 인덱스(원래의 위치)까지만 이동한다.
마지막 인덱스까지 위 과정을 반복한다.
이와 같은 기능을 하는 소트 프로그램을 작성하시오.

그림 설명 : http://codingdojang.com/scode/443?answer_mode=hide
"""
"""
=============================================================================
과제 1. 위 문제의 알고리즘으로 배열을 정렬하시오. 
        - 조건 : 결과값을 저장하기 위해 새로운 리스트를 생성할 수 없다.
        - input = [5,2,6]
        - 출력 : [2,5,6]
=============================================================================
"""

# 리스트를 오름차순으로 정렬하는 프로그램 정의 (변수는 input_num_zip)
def is_sort(input_num_zip):
    for i in range(1, len(input_num_zip)):                      # 1부터 길이만큼 다음 행위 반복
        if input_num_zip[i] < input_num_zip[i - 1]:             # 만약 해당 위치의 수가 앞의 수보다 작다면,
            input_num_zip.insert(i - 1, input_num_zip[i])       # 그 수를 앞에 삽입한 후 원래 위치에서 삭제
            input_num_zip.pop(i + 1)

    print(input_num_zip)                                        # 오름차순으로 정렬한 리스트 출력

if __name__ == '__main__':
    # input_num_zip 입력받을 때, 이를 ',' 기준으로 분해 후 이를 숫자(정수)로 변환
    input_num_zip = list(map(int, input('리스트를 입력하세요 : ').split(',')))

    is_sort(input_num_zip)                                      # is_sort 실행
    print()

"""
=============================================================================
과제 2. 위 문제의 알고리즘으로 배열을 정렬하시오
        - 조건 : 결과값을 저장하기 위해 새로운 리스트를 생성할 수 없다.
        - input = [5,2,4,6,1,3]
        - 출력 : [1,2,3,4,5,6]
=============================================================================
"""

# 리스트를 오름차순으로 정렬하는 최종 프로그램 정의 (변수는 input_num_zip)
def is_sort_final(input_num_zip):
    for i in range(1, len(input_num_zip)):                      # 1부터 길이만큼 다음 행위 반복
        for j in range(i):                                      # i만큼 다음 행위 반복
            if input_num_zip[i] < input_num_zip[j]:             # 만약 해당 위치의 수가 앞의 수보다 작다면,
                input_num_zip.insert(j, input_num_zip[i])       # 그 수를 앞에 삽입한 후 원래 위치에서 삭제
                input_num_zip.pop(i + 1)

    print(input_num_zip)                                        # 오름차순으로 정렬한 리스트 출력

if __name__ == '__main__':
    # input_num_zip 입력받을 때, 이를 ',' 기준으로 분해 후 숫자(정수)로 변환
    input_num_zip = list(map(int, input('리스트를 입력하세요 : ').split(',')))

    is_sort_final(input_num_zip)                                # is_sort_final 실행