# take the output json files and plot graph for all courses as separate graphs
import json
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os

# get the list of all json files
json_files = [pos_json for pos_json in os.listdir('./') if pos_json.endswith('.json')]
print(json_files)

# for each json file, plot the graph in a folder named by filename
# diverging map of RdBu

color_list = plt.cm.PiYG(np.linspace(0, 1, 10))
color_list = color_list[::-1]
for file in json_files:
    print("FILE",file)
    with open(file) as f:
        data = json.load(f)
        print(len(data))
        for course in data:
            # plot a simple plt and save it in a folder
            plt.figure()
            grades = list(course.values())[0]
            # get the values of grades to int from string
            grades = {k: int(v) for k, v in grades.items() if k != 'course' and k != 'year'}
            # plot the grades dictionary, maintain the order of keys and x axis labels as keys
            plt.bar(range(len(grades)-1), list(grades.values())[:-1], align='center', color=color_list)
            # show y axis as integers and y value on bar
            for k,v in enumerate(list(grades.values())[:-1]):
                plt.text(k, v, str(v), ha='center', va='bottom')
            # add text at top right saying total number of students
            plt.text(0.9, 0.9, 'Total: '+str(grades['Total']), ha='center', va='bottom', transform=plt.gca().transAxes)
            plt.xticks(range(len(grades)-1), list(grades.keys())[:-1])
            plt.xlabel('Grade')
            plt.ylabel('Number of students')  
            plt.title(list(course.keys())[0])
            if len(grades.values())>2:
                max_val = max(list(grades.values())[:-1])
            else:
                max_val = 5
            plt.axis(ymin=0, ymax=max_val+10)
           
            file_saved = file.split('.')[0]+'/'
            if not os.path.exists(file_saved):
                os.makedirs(file_saved)
            plt.savefig(file_saved+list(course.keys())[0]+'.png')
            # plt.show()