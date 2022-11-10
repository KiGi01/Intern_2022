### 교보문고 홈페이지 링크 및 책소개 전체 리뉴얼에 따른 코드 수정
- book_all_info_박수현.py : 어린이(초등)_set.txt, 유아(0~7세)_set.txt을 활용해 도서를 추출하는 코드입니다. (크롤링 중 오류가 발생한다면 내부에 적힌대로 코드를 수정하여 활용하면 됩니다.)
- book_barcode_new_code_박수현.py : 기존 바코드(ISBN)가 아닌 새로운 형식의 상품코드가 만들어졌습니다. 목록 내 상품코드를 추출하는 코드입니다.
- book_barcode_set_code_박수현.py : 위 코드를 통해 추출된 상품코드 중 중복된 상품코드를 제외한 후 다시 저장하는 코드입니다.
- 어린이(초등)_set.txt, 유아(0~7세)_set.txt : 유아 및 어린이 세부 도서 목록 > 전체 보기 > 판매량순에서 중복을 제외하여 추출한 결과
- [book_all_info_박수현.json](https://drive.google.com/file/d/1fLetabDd1coWoQmWcs00t2lvvTBLAAJE/view?usp=share_link) : book_all_info_박수현.py을 통해 추출한 결과입니다.
