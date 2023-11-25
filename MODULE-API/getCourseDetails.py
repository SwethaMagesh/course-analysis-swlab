import os
def get_year_and_semester(code):
    pass


def get_course_details_from_csv(code, year, semester):
    BASE='../MODULE-TIMETABLE/output'
    file_path = os.path.join(BASE, f'{year}{semester}.pdf.csv')
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == code:
                try:
                    row[1] = int(row[1])
                except:
                    row[1] = 0
                return row[1], row[2], row[3], row[4]

get_course_details_from_csv('CS1010', '2022', 'Spring')
def get_course_details(code):
    # get year and spring/autumn
    year, semester = get_year_and_semester(code)
    # get course details from csv file - venue, instructor, title, slot
    title, slot, venue, instructor = get_course_details_from_csv(code, year, semester)

    # get clashing courses from csv file for current sem and year
    clashing_courses = get_clashing_courses(code, year, semester)

    # get course strength from grading stats (avg?)
    strength = get_course_strength(code, year)

    # get course difficulty from grading stats (avg?)
    difficulty_analysis = get_course_difficulty(code, year)

    # pack into a dict and return
    return {
        'code': code,
        'year': year,
        'semester': semester,
        'title': title,
        'slot': slot,
        'clashing_courses': clashing_courses,  # list of course code titles
        'venue': venue,
        'instructor': instructor,
        'strength': strength,
        'difficulty': difficulty_analysis,
    }
