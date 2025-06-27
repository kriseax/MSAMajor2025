from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#make a Flask app
app = Flask(__name__)
app.config["DEBUG"] = True

#set secret key
app.config["SECRET_KEY"] = "your secret key"

"""
Functtion to request student data from the api
Input: url
Output: JSON student data
"""
def get_student_data(url:str):
    #make a request
    response = requests.get(url)

    #convert response format to JSON
    response_json = response.json()
    return response_json

#create a route for the website index/root. Will display all student data
@app.route('/', methods=['GET'])
def index():
    #make a request to the student data api
    url = 'http://127.0.0.1:5000/api/students/all'

    #get the student data
    student_data = get_student_data(url)
    return render_template('index.html', student_data=student_data)

#create a route for the majors search page with GET request
@app.route('/majors', methods=['GET'])
def majors_get():
    #get a list of student data
    url = 'http://127.0.0.1:5000/api/students/all'
    student_data = get_student_data(url)

    #ceate a list to store unique majors
    major_list = []

    #use for loop to iterate throught the student list
    for student in student_data:
        #add major to majors list if majot not currently in list
        if student['major'] not in major_list:
            major_list.append(student['major'])
        
        #sort the major list
        major_list.sort()

    return render_template('majors.html', major_list=major_list)

#create a route for the majors search page with GET request
@app.route('/majors', methods=['POST'])
def majors_post():
    #get a list of student data
    url = 'http://127.0.0.1:5000/api/students/all'
    student_data = get_student_data(url)

    #ceate a list to store unique majors
    major_list = []

    #use for loop to iterate throught the student list
    for student in student_data:
        #add major to majors list if majot not currently in list
        if student['major'] not in major_list:
            major_list.append(student['major'])
        
    #sort the major list
    major_list.sort()

    #get the form data: chosen major
    major = request.form.get('major')
    print(major)

    #create the request url to get students with that major
    url = f"http://127.0.0.1:5000/api/majors/{major}"

    #send the request and get the response
    result_list = get_student_data(url)
    return render_template('majors.html', major_list=major_list, result_list=result_list)


#run the flask app
app.run(port=5001)
