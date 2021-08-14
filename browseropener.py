from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(
    executable_path=r'D:\coding projects\geckodriver.exe')

driver.get("https://lainchan.org/%CE%94/catalog.html")

try:
    results = driver.find_element_by_class_name("threads")
    print(results.text)
    threadcount = str(results.text).split('R:')
    print(len(threadcount))
except:
    print("Cannot Fetch Results")
    driver.quit()

time.sleep(10)
driver.quit()

