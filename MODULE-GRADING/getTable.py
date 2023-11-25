
import sys
import time
import os
import json
from selenium import webdriver

from selenium.webdriver.common.by import By


def getTableFromXpath(path):
    # make headless
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    abs_path = 'file:///' + \
        os.path.split(os.path.abspath('.'))[0] + '/'+year+'/' + path
    print(abs_path)
    # use options
    driver = webdriver.Chrome(options=options)
    driver.get(abs_path)
    try:
        time.sleep(2)
        table = driver.find_element(
            By.XPATH, "//table/tbody/tr[5]/td/table/tbody/tr/td/table")
        return table.text

    except Exception as e:
        print(e.msg)


def process_raw_text(raw_text, grade_dict, course_code):

    for line in raw_text.split('\n')[1:]:
        line = line.split(' ')
        if len(line) == 2:
            grade_dict[line[0]] = line[1]
    grade_dict["course"] = course_code
    grade_dict["year"] = year


def convert_dict_to_jsonfile(master_dict):
    with open('../../MODULE-GRADING/'+year+'grades.json', 'r+') as fp:
        # add a comma if the file is not empty
        if os.stat('../../MODULE-GRADING/'+year+'grades.json').st_size != 0:
            # remove the last character ]
            fp.seek(0, os.SEEK_END)
            fp.seek(fp.tell() - 1, os.SEEK_SET)
            fp.write(',')
            json.dump(master_dict, fp)
            fp.write(']')
        else:
            #  add [ if the file is empty
            fp.write('[')
            json.dump(master_dict, fp)
            fp.write(']')


path = sys.argv[1]
year = sys.argv[2]
raw_text = getTableFromXpath(path)
grade_dict = {}
master_dict = {}
process_raw_text(raw_text, grade_dict, course_code=path.split('.')[0])
master_dict[grade_dict["course"]] = grade_dict
print(master_dict)
convert_dict_to_jsonfile(master_dict)
