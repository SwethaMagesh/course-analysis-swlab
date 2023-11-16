# flask server for the module api

from flask import Flask, request, jsonify
from flask_cors import CORS
# cors



app = Flask(__name__)
CORS(app)
# set routes
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/api/v1.0/courseDetails', methods=['GET'])
def process_get_request():
    courseCode = request.args.get('code')
    return jsonify(get_course_details(courseCode))

def get_course_details(code):
    return {'code': code, 
            'title': 'Introduction to Programming', 
            'slot': 4,
            'venue': 'LT1',
            'instructor': 'Dr. Tan',
            'strength': 100,
            'difficulty': 3,
            'projects':'yes',
            'recommended':'yes'
            }
if __name__ == '__main__':
    app.run()
