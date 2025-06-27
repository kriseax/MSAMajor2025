import flask
from flask import request, jsonify
import student_generator_v2 as sg

#create a flask app object
app = flask.Flask(__name__)

#tell the server to reload each time the code changes
app.config["DEBUG"] = True

"""
Function to query the student dictionaries based on a searck key
Input: searchkey
Output: list of results
"""
def search_student_data(search_value, search_key):
    #get students with major major
    #get all students
    student_dictionaries = sg.get_student_dictionaries()
    list_of_results = []
    #use for loop to search
    for student in student_dictionaries:
        if search_value.lower() == student[search_key].lower():
            list_of_results.append(student)
    
    return list_of_results


#create a route to display our name
@app.route('/', methods=['GET'])
def index():
    return "<h1> My name is Kristofferson Culmer</h1>"

#create a route to return all student data
@app.route('/api/students/all', methods=['GET'])
def api_all():
    #load student dictionaries
    student_dictionaries = sg.get_student_dictionaries()
    return jsonify(student_dictionaries)

#create a route to return students by major
@app.route('/api/majors/<string:major>', methods=['GET'])
def api_students_by_major(major:str):
    
    #get students with major major
    #get all students
    major_students = search_student_data(major, "major")
   
    return jsonify(major_students)

#create a route to return a student based on an id url parameter
@app.route("/api/students/<string:id>", methods=['GET'])
def api_student_by_id(id:str):
    #get all students
    student_dictionaries = sg.get_student_dictionaries()

    target_student = None
    #search student dictionaries for the student based on ID
    for student in student_dictionaries:
        if student['id'] == id:
            target_student = student
            break
    return jsonify(target_student)

@app.route('/api/students/class/<string:class_rank>', methods=['GET'])
def api_student_by_class(class_rank:str):
    student_by_class = search_student_data(class_rank, "class")
    return jsonify(student_by_class)


#run the application
app.run()
