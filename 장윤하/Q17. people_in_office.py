"""
-----------------  Question  -----------------
A사무실에는 특정일자의 출퇴근 시간이 기록된 거대한 로그파일이 있다고 한다.
파일의 형식은 다음과 같다. (한 라인에서 앞부분은 출근시간(HH:MM:SS), 뒷부분은 퇴근시간이다)
- 09:12:23 11:14:35
- 10:34:01 13:23:40
- 10:34:31 11:20:10
특정시간을 입력(예:11:05:20)으로 주었을 때 그 시간에 총 몇 명이 사무실에 있었는지 알려주는 함수를 작성하시오.
----------------------------------------------
"""
"""
=============================================================================
과제 1. 'DATA\\Q3. people_in_office'폴더 내에 있는 '출퇴근기록.txt'를 읽어들이고, 
        주어진 시간(check_time)에 총 몇명이 사무실에 있었는지 알려주는 함수를 작성하시오.
        - check_time = "11:05:20"
        - 출력 : 4
=============================================================================

"""
def cnt_people(check_time):
    cnt_p = 0
    file_path = "C:\세미나\week3\python_seminar\python_seminar\DATA\Q3. people_in_office\commute_daily_log.txt"
    with open(file_path) as f:
        lines = f.read().splitlines() # 텍스트 파일을 한 줄씩 읽어 들임

    split_lst = []
    for i in range(0, len(lines)):
        lines_split = lines[i].split()  # 한 줄을 다시 공백에 따라 두 가지 요소로 분리
        split_lst.append(lines_split)   # 리스트에 리스트를 저장

        start_time = int(split_lst[i][0].replace(":",""))   # ':'를 삭제하여 하나의 숫자로 저장 ( 11:09:08 -> 110908 )
        last_time = int(split_lst[i][1].replace(":",""))
        check_hour = int(check_time.replace(":",""))


        if start_time <= check_hour <= last_time:           # 입력한 시간이 출근 시간과 퇴근 시간 사이에 있는 경우
            cnt_p += 1                                      # 변수에 1씩 더함

    return(cnt_p)

if __name__ == '__main__':
    check_time = input("check_time = ")
    print(cnt_people(check_time))




