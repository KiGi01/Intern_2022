from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import json

# chromedriver 설정 및 웹 페이지 열기
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(r'C:\Users\선아\Desktop\ICL\22summer_python\crwaling\chromedriver.exe' 
                          , options=options) 
driver.get('https://google.com')

# 페이지 로딩 5초
driver.implicitly_wait(5)

# 교보문고 검색 및 홈페이지 클릭
element = driver.find_element(By.NAME,"q").send_keys("교보문고")
driver.find_element(By.NAME,"q").send_keys(Keys.ENTER)
driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/a/h3").click()

# 국내도서 클릭
driver.find_element(By.XPATH, "//*[@id='header']/div[3]/ul[1]/li[1]/a").click()
# 유아(0~7세) 클릭
driver.find_element(By.XPATH, "//*[@id='main_snb']/div[1]/ul[3]/li[1]/a/em").click()
# 베스트셀러 클릭
driver.find_element(By.XPATH, "//*[@id='container']/div[2]/div/div/div[3]/ul/li[2]/a/span").click()
