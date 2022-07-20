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
import os


def HowManyPeople( check_time ):  
    dir_path = 'C:\ICL 2022\week3\DATA\Q3. people_in_office\'
    #dir_path = 'C:/Users/선아/Desktop/ICL/22summer_python/week3/DATA/Q3. people_in_office/'
    file_path = dir_path+'commute_daily_log.txt'

    check_time = check_time.split(':')
    check_time = int(check_time[0])*3600 + int(check_time[1])*60 + int(check_time[2])
#    print("check_time:", check_time, "s")
    f = open(file_path, "r", encoding="UTF-8")
    txt_content = f.read()
    txt_content = txt_content.split('\n')
    f.close()
    count = 0
    for i in txt_content:
        if ':' in i:
            i = i.split(' ')
            #print(i)
            goto = i[0]
            goto = goto.split(':')
            goto = int(goto[0])*3600+int(goto[1])*60+int(goto[2])
            getoff = i[1]
            getoff = getoff.split(':')
            getoff = int(getoff[0])*3600+int(getoff[1])*60+int(getoff[2])
            if check_time in range(goto, getoff+1):
                count +=1
#                print("go to:", goto, "s, get off:",  getoff, "s, Y/N: Y", )
#            else:
#                print("go to:", goto, "s, get off:",  getoff, "s, Y/N: N", )
    return count
    

print("총", HowManyPeople("11:05:20"), "명")
print("총", HowManyPeople("08:05:20"), "명")
print("총", HowManyPeople("12:05:20"), "명")
print("총", HowManyPeople("14:05:20"), "명")

