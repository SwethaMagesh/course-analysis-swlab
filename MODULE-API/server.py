# flask server for the module api

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from getCourseDetails import *

app = Flask(__name__)
CORS(app)

# set routes
@app.route('/api/v1.0/courseDetails', methods=['GET'])
def process_get_request():
    course_code = request.args.get('code')
    return jsonify(get_course_details(course_code))

def get_course_details(code):
    obj = get_course_analysis(code)
    if obj is None:
        # return status code 404
        response = {}
        return response
    else:
        return obj

@app.route('/api/v1.0/get_images/<coursecode>')
def get_images(coursecode):
    base_folder = '../MODULE-GRADING'
    years = ['2020grades', '2021grades', '2022grades']  # Add more years as needed
    image_paths = []
    for year in years:
        folder_path = os.path.join(base_folder, year)
        file_path = os.path.join(folder_path, f'{coursecode}.png')
        print(file_path)
        if os.path.exists(file_path):
            image_paths.append({'year': year[:4], 'path': file_path})
    return jsonify({'image_paths': image_paths})

if __name__ == '__main__':
    app.run()
