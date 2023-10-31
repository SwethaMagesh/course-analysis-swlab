# First get argument coursename_html
# Scrap the table using xpath : //table[@id='grades']//table//table
# Save the table as either csv or db table or json
import sys
import time
import os
from selenium import webdriver

from selenium.webdriver.common.by import By

def getTableFromXpath(path):
    driver = webdriver.Edge()
    abs_path = 'file:///' + os.path.split(os.path.abspath('.'))[0] + '/ASC-Grading/' + path
    print(abs_path)
    driver.get('https://www.google.com')
    driver.get(abs_path)
    try:
        head = driver.find_element(By.TAG_NAME, 'table')
        print(head.text)
        table = driver.find_element(By.XPATH, "//table/tbody/tr[5]/td/table/tbody/tr/td/table")
        # table = driver.find_element(By.XPATH, "//table[@id='grades']//table//table")
        print(table.text)
    except Exception as e:
        print(e.msg)
    time.sleep(50)
    # print(table)

path = sys.argv[1]
print(path)
getTableFromXpath(path)

