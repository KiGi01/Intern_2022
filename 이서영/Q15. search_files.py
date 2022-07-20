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

import os                                               # 디렉토리 내의 모든 파일에 접근해야할 때 os 모듈 사용

def search(dirname) :
    filenames = os.listdir(dirname)                     # os.listdir():디렉터리 안에 있는 것을 보여줌
    for filename in filenames :
        if '.' in filename :
                print(filename)

fpath = 'DATA\\Q1. finding_files'

search(fpath)

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

import os                                               # 디렉토리 내의 모든 파일에 접근해야할 때 os 모듈 사용

def search(dirname) :
    for (path, dir, files) in os.walk(dirname) :        # os.walk():하위폴더들을 for문을 통해 차례대로 탐색
                                                        # path : 디렉토리와 파일이 있는 경로
                                                        # dir : path 아래에 있는 폴더
                                                        # files : path 아래에 있는 파일
        for filename in files :
            if '.' in filename :
                print(filename)

fpath = 'DATA\\Q1. finding_files'

search(fpath)

"""
=============================================================================
과제 3. 과제 파일 내부에 함께 제공되는 'DATA\\Q1. finding_files'와 
       그 하위 폴더 내에 존재하는 모든 파일 중에서 확장자가 .txt인 파일의 이름을 출력해주는 프로그램을 작성하시오.  
       - 출력되어야 하는 파일명 : JI_FILE_1.txt, [FINAL] JI_FILE_3.txt, KANG_FILE_2.txt, [FINAL] KANG_FILE_3.txt, 
         (순서무관)             LEE_FILE_3.txt, [FINAL] LEE_FILE_3.txt, TXT_form.txt
=============================================================================
"""

import os                                               # 디렉토리 내의 모든 파일에 접근해야할 때 os 모듈 사용

def search(dirname) :
    for (path, dir, files) in os.walk(dirname) :  
        for filename in files :
            if '.txt' in filename :                     # .txt 일 경우, 파일 이름 출력
                print(filename)

fpath = 'DATA\\Q1. finding_files'

search(fpath)

"""
=============================================================================
과제 4. 과제 파일 내부에 함께 제공되는 'DATA\\Q1. finding_files'에 존재하는 .txt파일 중에서    (하위 폴더 포함) 
       내용에 'life is too short'이 포함되는 경우, 그 파일명을 출력해주는 프로그램을 작성하시오.
        - 출력되어야 하는 파일명 : JI_FILE_1.txt, [FINAL] JI_FILE_3.txt(순서무관)           
=============================================================================
"""

import os # 디렉토리 내의 모든 파일에 접근해야할 때 os 모듈 사용

def search(dirname) :
    for (path, dir, files) in os.walk(dirname) :  
        for filename in files :
            if '.txt' in filename :
              f = open(os.path.join(path, filename), 'r')   # os.path.join('C:\Tmp', 'a', 'b') -> "C:\Tmp\a\b"
                                                            # 경로를 병합하여 새로운 경로 생성
              txt = f.read()
              if 'life is too short' in txt :
                print(filename)
                
fpath = 'DATA\\Q1. finding_files'

search(fpath)
