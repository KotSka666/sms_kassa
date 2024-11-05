from selenium import webdriver
from bs4 import BeautifulSoup
import time


main_url = "http://192.168.8.1/?origin=xxx#/sms"


options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)

try:
    browser.get(main_url)
    time.sleep(5)

    page_source = browser.page_source
    soup = BeautifulSoup(page_source, "html.parser")


    all_sms = soup.find_all(class_="borderBottom sms_main_page_td1 paddingleft_10")
    for sms in all_sms:
        print(sms.text.strip())
finally:
    browser.quit()