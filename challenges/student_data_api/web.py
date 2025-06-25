import flask
from flask import request, jsonify

#create a flask app object
app = flask.Flask(__name__)

#tell the server to reload each time the code changes
app.config["DEBUG"] = True

#load student dictionaries

#create a route to display our name
@app.route('/', methods=['GET'])
def index():
    return "<h1> My name is Kristofferson Culmer</h1>"

#Create 2 routes
# - return all student data
# - return students by major

#run the application
app.run()
