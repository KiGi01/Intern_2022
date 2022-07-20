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
print('과제1')

import os
#os.listdir: 괄호 안에 지정된 디렉토리의 모든 파일 목록을 반환
files = [file for file in os.listdir('python_seminar/DATA/Q1. finding_files') if '.' in file]
print(', '.join(files))


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
print('\n과제2')
import os

dir_path = "python_seminar/DATA/Q1. finding_files"
#os.walk: 지정된 디렉터리부터 그 아래의 모든 하위 폴더와 파일까지 차례대로 접근
for (root, directories, files) in os.walk(dir_path): #파일 목록, 모든 하위 폴더 아래의 파일 목록에 접근
    for file in files:                            #파일 목록을 하나씩 출력
        print(file, end = ', ')



"""
=============================================================================
과제 3. 과제 파일 내부에 함께 제공되는 'DATA\\Q1. finding_files'와 
       그 하위 폴더 내에 존재하는 모든 파일 중에서 확장자가 .txt인 파일의 이름을 출력해주는 프로그램을 작성하시오.  
       - 출력되어야 하는 파일명 : JI_FILE_1.txt, [FINAL] JI_FILE_3.txt, KANG_FILE_2.txt, [FINAL] KANG_FILE_3.txt, 
         (순서무관)             LEE_FILE_3.txt, [FINAL] LEE_FILE_3.txt, TXT_form.txt
=============================================================================
"""

print('\n과제3')
import os

for (root, dir, files) in os.walk(dir_path): # 모든 하위 디렉토리와 파일에 접근
    for filename in files:  #파일 하나씩 확인
        if '.txt' in filename:   #.txt가 파일명에 들어가는 조건을 만족할 때
            print(filename, end = ', ')


"""
=============================================================================
과제 4. 과제 파일 내부에 함께 제공되는 'DATA\\Q1. finding_files'에 존재하는 .txt파일 중에서    (하위 폴더 포함) 
       내용에 'life is too short'이 포함되는 경우, 그 파일명을 출력해주는 프로그램을 작성하시오.
        - 출력되어야 하는 파일명 : JI_FILE_1.txt, [FINAL] JI_FILE_3.txt(순서무관)           
=============================================================================
"""

print('\n과제4')
import os

for (root, dir, files) in os.walk(dir_path): #os.walk 모든 하위 디렉토리와 파일에 접근
    for filename in files:  
        if '.txt' in filename: 
                f = open(os.path.join(root, filename),'r')  #디렉토리 경로에 파일 이름을 조합하는 함수, open으로 읽기 모드로 열기
                txt = f.read()   #파일에서 문자열 읽기
                if 'life is too short' in txt:
                        print(filename)
                f.close()
                