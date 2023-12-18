# course-analysis-swlab
Analyze courses of IITB CS and help compare different courses!
---
### DIFFERENT MODULES of the project:
- Timetable -> Details like slot, venue, instructor - **bash script, python** - _OUTPUT: CSV_
- Grading -> Scrap from asc - **py script**
    - Store the data for diff courses in json - **py**  _OUTPUT: JSON_
    - Graphically analyze % of top grades etc. **py**  _OUTPUT: PNG_
- Web - for components and weightage - **Web HTML, CSS, JS**
- API - **Flask Python**

---
OUTPUTS
- Some sample images
![image](https://github.com/SwethaMagesh/course-analysis-swlab/assets/43994542/050bfdb3-4db0-4480-8e35-219fdadaa954)
![image](https://github.com/SwethaMagesh/course-analysis-swlab/assets/43994542/e1e9f2f1-fe0d-4802-bea0-0ee24c50aae0)

![image](https://github.com/SwethaMagesh/course-analysis-swlab/assets/43994542/f6780354-e42b-4b75-92e2-9a022adb4aff)


---
### How to run this project
**MODULE grading**
- To run scraping for a new year and its courses
- First scrap the simple html files of the course with fname cs<xxx>.html in ASC folder in the right year
- Run the script file `bash generatecsv.py <year>`
- To run plot and generate png files run py file `python3 plot.py`

  
**MODULE timetable**
- To add a new timetable to generate csv: add the pdf file in that module and run the
- `bash timetable.sh`

**MODULE server**
- Run `python3 server.py`

**VIEW OUTPUT from MODULE WEB**

----


----
**Requirements**: Python requirements:
- selenium
- flask
- flask_cors
- numpy
- matplotlib


Install poppler-utils for pdf to text conversion in bash
