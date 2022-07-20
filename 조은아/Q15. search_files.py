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

file_path = os.chdir('C:\ICL 2022\week3\DATA\Q1. finding_files')
#file_path = os.chdir('C:/Users/선아/Desktop/ICL/22summer_python/week3/DATA/Q1. finding_files')
all_name = os.listdir(file_path)
file_name = []

for i in all_name: 
    if '.' in i: 
        file_name.append(i)

print("Sol #1: ")
print(', '.join(file_name))

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

import itertools

dir_path = 'C:\ICL 2022\week3\DATA\Q1. finding_files'
#dir_path = 'C:/Users/선아/Desktop/ICL/22summer_python/week3/DATA/Q1. finding_files'
file_name2 = []

for (root, directories, files) in os.walk(dir_path):
    file_name2.append(files)

print(len(file_name2))

file_name2 = list(itertools.chain(*file_name2))
print(len(file_name2))

print("Sol #2: ", ', '.join(file_name2))

"""
=============================================================================
과제 3. 과제 파일 내부에 함께 제공되는 'DATA\\Q1. finding_files'와 
       그 하위 폴더 내에 존재하는 모든 파일 중에서 확장자가 .txt인 파일의 이름을 출력해주는 프로그램을 작성하시오.  
       - 출력되어야 하는 파일명 : JI_FILE_1.txt, [FINAL] JI_FILE_3.txt, KANG_FILE_2.txt, [FINAL] KANG_FILE_3.txt, 
         (순서무관)             LEE_FILE_3.txt, [FINAL] LEE_FILE_3.txt, TXT_form.txt
=============================================================================
"""


file_name3 = []

for i in file_name2: 
    if '.txt' in i: 
        file_name3.append(i)


#print(len(file_name3))
print("Sol #3: ", ', '.join(file_name3))

"""
=============================================================================
과제 4. 과제 파일 내부에 함께 제공되는 'DATA\\Q1. finding_files'에 존재하는 .txt파일 중에서    (하위 폴더 포함) 
       내용에 'life is too short'이 포함되는 경우, 그 파일명을 출력해주는 프로그램을 작성하시오.
        - 출력되어야 하는 파일명 : JI_FILE_1.txt, [FINAL] JI_FILE_3.txt(순서무관)           
=============================================================================
"""


file_name4=[]
dir_path = 'C:\ICL 2022\week3\DATA\Q1. finding_files'
#dir_path = 'C:/Users/선아/Desktop/ICL/22summer_python/week3/DATA/Q1. finding_files'

for (root, directories, files) in os.walk(dir_path):
    for file in files:
        if '.txt' in file:
            file_path = os.path.join(root, file)
            f = open(file_path, "r", encoding="UTF-8")
            txt_content = f.read()
            f.close()
            if 'life is too short' in txt_content:
                file_name4.append(file)


print('Sol #4: ', ', '.join(file_name4))


