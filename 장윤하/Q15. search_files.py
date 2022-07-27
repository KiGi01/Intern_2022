"""
-----------------  Question  -----------------
A라는 디렉토리 하위에 있는 텍스트 파일(*.txt) 중에서
LIFE IS TOO SHORT 라는 문자열을 포함하고 있는 파일들을
모두 찾을 수 있는 프로그램을 작성하시오.
단, 하위 디렉토리도 포함해서 검색해야 함.
----------------------------------------------
"""
"""
=============================================================================
과제 1. 과제 파일 내부에 함께 제공되는 'DATA\\Q1. finding_files'폴더 내에 있는
        3개의 파일명을 프린트해주는 프로그램을 작성하시오.
        - 출력되어야 하는 파일명(순서무관) : Dock_form.docx, HWP_form.hwp, TXT_form.txt
=============================================================================
"""


import os

dir_root = "C:\세미나\week3\python_seminar\python_seminar\DATA\Q1. finding_files" # 디렉토리의 경로설정
save_lst = [] # 파일만 저장할 리스트 생성
item_list = os.listdir(dir_root) # 지정된 경로에 존재하는 파일과 폴더의 이름을 리스트에 저장

for item in item_list:                         # 앞서 저장한 파일과 폴더 반복
    path = dir_root + '/' + item               # path를 지정함 (지정해야 파일인지 폴더인지 구분 가능)

    if os.path.isfile(path):                   # 해당 path에 위치하는 것이 파일인 경우
        save_lst.append(item)                  # 리스트에 저장
print(', '.join(save_lst))




"""
=============================================================================
과제 2. 과제 파일 내부에 함께 제공되는 'DATA\\Q1. finding_files'와 
       그 하위 폴더 내에 존재하는 모든 파일을 출력해주는 프로그램을 작성하시오.
       - 출력되어야 하는 파일명 : Docx_form.docx, HWP_form.hwp, TXT_form.txt, JI_FILE_1.txt, JI_FILE_2.hwp, JI_FILE_3.docx,
         (순서무관)             KANG_FILE_1.docx, KANG_FILE_2.txt, KANG_FILE_3.hwp, LEE_FILE_1.docx, LEE_FILE_2.hwp, LEE_FILE_3.txt,
                               [FINAL] JI_FILE_1.docx, [FINAL] JI_FILE_2.hwp, [FINAL] JI_FILE_3.txt, [FINAL] KANG_FILE_1.docx, [FINAL] KANG_FILE_2.hwp, 
                               [FINAL] KANG_FILE_3.txt, [FINAL] LEE_FILE_1.docx, [FINAL] LEE_FILE_2.hwp, [FINAL] LEE_FILE_3.txt
=============================================================================
"""

dir_path = "C:\세미나\week3\python_seminar\python_seminar\DATA\Q1. finding_files"

file_name = []
for (root, directories, files) in os.walk(dir_path):  # 현재 디렉토리의 경로, 현재 디렉토리의 하위 디렉토리 목록, 현재 디렉토리의 일반 파일 목록 생성
    for file in files:                                # 하위 디렉토리 및 현재 디렉토리의 파일 리스트를 반복
        file_path = os.path.join(root, file)          # 디렉토리의 경로와 파일 이름을 이어줌

        file_name.append(os.path.basename(file))      # 리스트에 파일의 이름만 저장
print(', '.join(file_name))

"""
=============================================================================
과제 3. 과제 파일 내부에 함께 제공되는 'DATA\\Q1. finding_files'와 
       그 하위 폴더 내에 존재하는 모든 파일 중에서 확장자가 .txt인 파일의 이름을 출력해주는 프로그램을 작성하시오.  
       - 출력되어야 하는 파일명 : JI_FILE_1.txt, [FINAL] JI_FILE_3.txt, KANG_FILE_2.txt, [FINAL] KANG_FILE_3.txt, 
         (순서무관)             LEE_FILE_3.txt, [FINAL] LEE_FILE_3.txt, TXT_form.txt
=============================================================================
"""
dir_path = "C:\세미나\week3\python_seminar\python_seminar\DATA\Q1. finding_files"

file_name = []
for (root, directories, files) in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)

        if file_path[-3:] == 'txt':                     # 모든 파일의 경로 중, 끝에서 세 글자가 txt인 경우
            file_name.append(os.path.basename(file))    # 파일의 이름만 저장
print(', '.join(file_name))

"""
=============================================================================
과제 4. 과제 파일 내부에 함께 제공되는 'DATA\\Q1. finding_files'에 존재하는 .txt파일 중에서    (하위 폴더 포함) 
       내용에 'life is too short'이 포함되는 경우, 그 파일명을 출력해주는 프로그램을 작성하시오.
        - 출력되어야 하는 파일명 : JI_FILE_1.txt, [FINAL] JI_FILE_3.txt(순서무관)           
=============================================================================
"""
dir_path = "C:\세미나\week3\python_seminar\python_seminar\DATA\Q1. finding_files"

file_name = []
for (root, directories, files) in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)

        if file_path[-3:] == 'txt':             # 모든 파일 중, txt파일의 경우
            open_file = open(file_path, 'r')    # 해당 파일을 읽기 모드로 연다
            s = open_file.read()                # 파일을 읽어 들인 후,
            if 'life is too short' in s:        # 해당 파일 내에 'life is too short'가 포함될 경우
                file_name.append(os.path.basename(file)) # 리스트에 파일 이름만 저장

print(', '.join(file_name))