'''
week 7. 유아 베스트셀러 목록에 있는 각각의 도서 페이지 진입하기까지 완료
'''

# 0. 필요한 모듈 가져오기
# selenium : 사이트 이동 등을 위함
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
# time : 시간 지연을 위함
import time

# 1. 크롬 드라이버 설정 및 웹 페이지 열기
# chromedriver.exe을 드라이버로 설정
driver = webdriver.Chrome("./chromedriver.exe")
# 구글 웹 페이지 진입
driver.get("https://google.com")
# 크롬 브라우저 창 최대화
driver.maximize_window()

# 2. 교보문고 검색 및 홈페이지 클릭하기
# 요소 중 name="q"인 것을 찾아 "교보문고(엔터)" 값 전송
driver.find_element(By.NAME, "q").send_keys("교보문고\n")
# XPATH 경로에 해당하는 요소 클릭 ("교보문고 홈페이지", "welcomeAdLayer 닫기 버튼" 위치에 해당)
driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/a").click()
# (교보문고 홈페이지에 들어가면 welcomeAdLayer가 메인 화면으로 적용되기 때문에 다른 요소를 클릭할 수 없다.)
driver.find_element(By.XPATH, "//*[@id='welcomeAdLayer']/div/button").click()
# "오늘 하루동안 보지 않겠습니까?" 팝업의 확인 버튼 클릭 
pop_up = Alert(driver)
pop_up.accept()

# 3. 유아 베스트셀러 페이지 진입하기
# link text가 "국내도서", "유아(0~7세)", "베스트셀러"인 것을 찾아 클릭
driver.find_element(By.LINK_TEXT, "국내도서").click()
driver.find_element(By.LINK_TEXT, "유아(0~7세)").click()
driver.find_element(By.LINK_TEXT, "베스트셀러").click()
# 2초 쉬기
time.sleep(2)

"""
베스트셀러 목록의 타켓 페이지 이동 버튼에 대한 각 XPATH
//*[@id="eventPaging"]/div/ul/li[1]/a
//*[@id="eventPaging"]/div/ul/li[2]/a
...
//*[@id="eventPaging"]/div/ul/li[8]/a

베스트셀러 목록에 있는 도서에 대한 각 XPATH (타겟 페이지를 이동해도 변함이 없음)
//*[@id="prd_list_type1"]/li[1]/div/div[1]/div[2]/div[1]/a
//*[@id="prd_list_type1"]/li[3]/div/div[1]/div[2]/div[1]/a
...
//*[@id="prd_list_type1"]/li[39]/div/div[1]/div[2]/div[1]/a

150위까지 제공하기 때문에 마지막 페이지는 변함이 있음
//*[@id="prd_list_type1"]/li[19]/div/div[1]/div[2]/div[1]/a
"""

# 4. 베스트셀러 목록에 있는 도서 페이지 진입하기
# 다음 행위 8번 반복 (2부터 9까지)
for i in range(2, 10):
    # 만약 타겟 페이지가 8이라면, j를 1부터 19 중 홀수로 지정한 후 XPATH 경로에 해당하는 요소 클릭 ("도서 제목" 위치에 해당)
    if i == 9:
        for j in range(1, 20, 2):
            driver.find_element(By.XPATH, f"//*[@id='prd_list_type1']/li[{j}]/div/div[1]/div[2]/div[1]/a").click()
            time.sleep(2)
            # 이전 페이지로 돌아가기
            driver.back()
            time.sleep(2)

    # 만약 타겟 페이지가 8이 아니라면, j를 1부터 39 중 홀수로 지정한 후 XPATH 경로에 해당하는 요소 클릭
    else:
        for j in range(1, 40, 2):
            driver.find_element(By.XPATH, f"//*[@id='prd_list_type1']/li[{j}]/div/div[1]/div[2]/div[1]/a").click()
            time.sleep(2)
            driver.back()
            time.sleep(3)

        # i를 2부터 8로 지정한 후 XPATH 경로에 해당하는 요소 클릭 ("다음 타겟 페이지 버튼" 위치에 해당)
        driver.find_element(By.XPATH, f"//*[@id='eventPaging']/div/ul/li[{i}]/a").click()
        time.sleep(2)