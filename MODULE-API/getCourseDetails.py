import os
import csv
import json


def get_year_and_semester(code):
    BASE = '../MODULE-TIMETABLE/output'
    results = []
    for file in os.listdir(BASE):
        if file.endswith('.pdf.csv'):
            index = file.find('.pdf.csv')
            year = file[:4]
            semester = file[4:index]
            file_path = os.path.join(BASE, file)
            with open(file_path, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[0] == code:
                        results.append([year, semester])
                        break
    if len(results) == 1:
        return results[0][0], results[0][1]
    elif len(results) > 1:
        # ToDO
        # # return the latest year and semester
        results.sort(key=lambda x: x[0])
        return results[-1][0], results[-1][1]
                    
    return (None, None)


def get_course_details_from_csv(code, year, semester):
    BASE = '../MODULE-TIMETABLE/output'
    file_path = os.path.join(BASE, f'{year}{semester}.pdf.csv')
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == code:
                try:
                    row[1] = int(row[1])
                except:
                    row[1] = 0

                return (row[1], row[2], row[3], row[4])
    return [None, None, None, None]


def get_clashing_courses(code, slot, year, semester):
    results = []
    if slot == 0:
        return results
    BASE = '../MODULE-TIMETABLE/output'
    file_path = os.path.join(BASE, f'{year}{semester}.pdf.csv')
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                row[1] = int(row[1])
            except:
                row[1] = 0
            if row[1] == slot and row[0] != code:
                results.append(row[0]+': '+row[3])
    return results


def get_course_strength(code):
    res = []
    BASE = '../MODULE-GRADING'
    # for all {year}grades.json files in BASE check if code exists
    for file in os.listdir(BASE):
        if file.endswith('grades.json'):
            file_path = os.path.join(BASE, file)
            with open(file_path, 'r') as f:
                data = json.load(f)
                for obj in data:
                    if list(obj.keys())[0] == code.lower():
                        res.append(obj[code.lower()]['Total']+' in '+obj[code.lower()]['year'])
        
    return '. '.join(res)


def get_course_grade_analysis(code):
    # return difficulty and category (3,2,1 or 0)
    grade_analysis = []

    BASE = '../MODULE-GRADING'
    # for all {year}grades.json files in BASE check if code exists
    for file in os.listdir(BASE):
        if file.endswith('grades.json'):
            file_path = os.path.join(BASE, file)
            with open(file_path, 'r') as f:
                data = json.load(f)
                for obj in data:
                    if list(obj.keys())[0] == code.lower():
                        grades = obj[code.lower()]
                        analyse_and_append(grades, grade_analysis)
                        break
    if len(grade_analysis) == 0:
        return None
    else:
        return '. '.join(grade_analysis)

def analyse_and_append(grades, grade_analysis):
    top = 0
    top2 = 0
    top3 = 0
    if 'AP' in grades:
        top = top + int(grades['AP'])  
    if 'AA' in grades:
        top = top + int(grades['AA'])
    if 'AB' in grades:
        top2 = int(grades['AB'] )
    if 'BB' in grades:
        top3 = int(grades['BB'] )
    total = int(grades['Total'])
    if total == '0':
        return
    statement = 'In {}, {}% students scored A while {}% scored AB, {}% scored BB'.format(grades['year'],top*100//total, top2*100//total, top3*100//total)
    grade_analysis.append(statement)
    
    return None


def get_course_analysis(code):
    result = {}
    code=code.upper()

    # get year and spring/autumn
    year, semester = get_year_and_semester(code)
    if year != None and semester != None:
        result['year'] = year
        result['semester'] = semester

    # get course details from csv file - venue, instructor, title, slot
    if 'year' in result and 'semester' in result:
        slot, venue, title, instructor = get_course_details_from_csv(
            code, year, semester)
        if not slot == 0 or slot != None:
            result['slot'] = slot
        if not title == None:
            result['title'] = title
        if not venue == None:
            result['venue'] = venue
        if not instructor == None:
            result['instructor'] = instructor

    # get clashing courses from csv file for current sem and year
    if 'slot' in result:
        clashing_courses = get_clashing_courses(code, slot, year, semester)
        result['clashing_courses'] = clashing_courses

    # get course strength from grading stats (avg?)
    strength = get_course_strength(code)

    # get course difficulty from grading stats (avg?)
    grade_analysis = get_course_grade_analysis(code)
    if grade_analysis == None:
        grade_analysis = 'Not Available'
    if strength == None or strength == '':
        strength = 'Not Available'
    result['strength'] = strength
    result['difficulty'] = grade_analysis

    # pack into a dict and return
    return result



