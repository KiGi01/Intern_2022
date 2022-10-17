from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def is_book_barcode(i):
    book_barcode_list = []
    link_class = [4107, 4109, 4111, 4115, 4117, 4119, 4121, 4123]
    # 4202, 4204, 4206, 4208, 4210, 4212, 4214, 4216, 4220
    for i in range(8):
        book_link = f"https://product.kyobobook.co.kr/category/KOR/{link_class[i]}"
        driver.get(book_link)
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.ID, "allSort-button").click()
        driver.find_element(By.ID, "ui-id-7").click()
        time.sleep(2)
        driver.find_element(By.ID, "allPer-button").click()
        driver.find_element(By.ID, "ui-id-11").click()
        time.sleep(2)

        for i in range(10):
            try:
                search_page = BeautifulSoup(driver.page_source, "html.parser")
                for book_barcode in search_page.find_all("li", {"class":"prod_item"}):
                    try:
                        book_barcode_list.append(book_barcode.get("data-id"))
                    except:
                        pass
                driver.find_element(By.CSS_SELECTOR, "button.btn_page.next").click()
                time.sleep(3)
            except:
                break
    
    return book_barcode_list

if __name__ == '__main__':
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get("https://google.com")

    for i in range(1):
        category_name = ["유아(0~7세)"]
        # "어린이(초등)"

        with open(f"{category_name[i]}.txt", "w", encoding="UTF-8") as f:
            for barcode in is_book_barcode(i):
                f.write(barcode + "\n")

    print("done")
    driver.quit()