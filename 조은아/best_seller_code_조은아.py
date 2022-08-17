#모듈 설치
#pip install selenium

#모듈 불러오기
from selenium import webdriver
import json

#chromedriver설정(chromedriver.exe) 및 크롬으로 웹 페이지 열기
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#driver 변수로 크롬 드라이버 불러오기
#크롬드라이버 위치 절대경로로 설정 (raw문자열_프로그래밍 언어로 변경)
driver = webdriver.Chrome(r'C:\Users\선아\Desktop\ICL\22summer_python\crwaling\chromedriver.exe' 
                          , options=options) 
#구글 웹 페이지 열기
driver.get('https://google.com')