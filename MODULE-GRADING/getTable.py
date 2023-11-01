# First get argument coursename_html
# Scrap the table using xpath : //table[@id='grades']//table//table
# Save the table as either csv or db table or json
import sys
import time
import os
import json
from selenium import webdriver

from selenium.webdriver.common.by import By

def getTableFromXpath(path):
    driver = webdriver.Edge()
    abs_path = 'file:///' + os.path.split(os.path.abspath('.'))[0] + '/SingleFile/' + path
    print(abs_path)
    driver.get(abs_path)
    try:
        time.sleep(5)
        table = driver.find_element(By.XPATH, "//table/tbody/tr[5]/td/table/tbody/tr/td/table")
        # table = driver.find_element(By.XPATH, "//table[@id='grades']//table//table")
        return table.text

    except Exception as e:
        print(e.msg)    

def process_raw_text(raw_text, grade_dict, course_code):
    for line in raw_text.split('\n')[1:]:        
        line = line.split(' ')
        if len(line) == 2:
            grade_dict[line[0]] = line[1]
    grade_dict["course"] = course_code
    
def convert_dict_to_jsonfile(master_dict):
    with open('grades.json', 'a') as fp:
        json.dump(master_dict, fp)

path = sys.argv[1]
raw_text = getTableFromXpath(path)
grade_dict = {}
master_dict = {}
process_raw_text(raw_text, grade_dict, course_code=path.split('.')[0])
master_dict[grade_dict["course"]] = grade_dict
print(master_dict)
convert_dict_to_jsonfile(master_dict)


