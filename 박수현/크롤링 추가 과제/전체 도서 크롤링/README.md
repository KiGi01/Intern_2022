### 교보문고 내 유아(0~7세) 및 어린이(초등)의 전체 도서를 추출하기 위한 코드입니다.
- 추출해야 하는 도서의 권수가 많기 때문에(약 20만 권) isbn을 모두 추출하여 텍스트 파일에 저장한 후, 그 텍스트 파일을 사용하여 추출하는 방식으로 작성했습니다.
- 컴퓨터 사양 문제로 인해 샘플 및 최종 데이터를 제공해 드릴 수 없는 점 양해 부탁드립니다.
- book_all_barcode_박수현.py : 유아(0~7세) 및 어린이(초등)의 전체 도서에 대한 isbn을 수집한 후, 이를 텍스트 파일에 저장하는 코드입니다.
- book_append_barcode_박수현.py : 교보문고 목록에 새롭게 업로드된 도서의 isbn을 수집한 후, 이를 텍스트 파일에 저장하는 코드입니다. (크롤링을 마친 이후 추가적인 크롤링이 필요하다면, 처음부터 다시 추출하는 수고를 덜해 시간을 절약할 수 있도록 제작해 봤습니다.)
- book_all_info_박수현.py : "book_all_barcode_박수현.py" 및 "book_append_barcode_박수현.py"을 통해 저장한 텍스트 파일을 활용해 전체 도서를 추출하는 코드입니다. (크롤링 중 오류가 발생한다면 내부에 적힌대로 코드를 수정하여 활용하면 됩니다.)

+) 2020.10.17 교보문고 홈페이지의 리뉴얼로 인하여 현재 코드 사용 불가
