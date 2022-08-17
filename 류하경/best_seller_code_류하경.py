from selenium import webdriver
from selenium.webdriver.common.by import By

# 구글 접속
driver = webdriver.Chrome('/Users/user/chromedriver')
driver.implicitly_wait(3)
driver.get('https://google.com')
driver.maximize_window()

# 교보문고 접속
element = driver.find_element(By.NAME, "q")
element.send_keys('교보문고')
element.submit()