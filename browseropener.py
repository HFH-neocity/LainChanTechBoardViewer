from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(
    executable_path=r'D:\coding projects\geckodriver.exe')

p = input("enter a board you wanna go to:")
if p == "tech":
    driver.get("https://lainchan.org/%CE%A9/catalog.html")
elif p == "programming":
    driver.get("https://lainchan.org/%CE%BB/catalog.html")
elif p == "security":
    driver.get("https://lainchan.org/sec/catalog.html")
elif p == "diy":
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

