# import libraries
import json

# import flask dependencies
from flask import Flask, jsonify, request

# import response functions for intent requests
from fetch import *

map = dict()

# initialize the flask app
app = Flask(__name__)

# Default route for homepage
@app.route('/', methods=['POST', 'GET'])
def index():
    return "Hello World! This is fulfillment server for SwayamSevak."

# Route for Dialogflow webhook (Only support POST requests)
@app.route('/webhook', methods=['POST'])
def webhook():
    content = json.loads(request.data)

    # print (json.dumps(content, indent=2))

    intentName = content['result']['metadata']['intentName']
    name=""
    session_id = content['sessionId']

    if 'name' in content['result']['parameters']:
        name = content['result']['parameters']['name']
    if 'dob' in content['result']['parameters']:
        dob = content['result']['parameters']['dob']
    if 'sex' in content['result']['parameters']:
        sex = content['result']['parameters']['sex']   
    if 'docname' in content['result']['parameters']:
        docname = content['result']['parameters']['docname']  
    if 'time' in content['result']['parameters']:
        time = content['result']['parameters']['time'] 

    print ("Indent: "+intentName)

    if intentName == 'Doctors':
        return jsonify(handle_all_doctors())

    elif intentName == 'videoCall':
        return jsonify(handle_video_call())

    elif intentName == 'doctorFee':
        return jsonify(handle_fee_doctors(name))

    elif intentName == 'GetSchedule':
        return jsonify(handle_schedule_doctors(name))

    elif intentName == 'doctorContact':
        return jsonify(handle_doctors_contact(name))

    elif intentName == 'bedCheck':
        return jsonify(handle_all_Beds(name))

    elif intentName == 'Help':
        return jsonify(handle_help())

    elif intentName == 'departmentDoctors':
        return jsonify(handle_department_doctors(name))

    elif intentName == 'Broadcast':
        return jsonify(handle_broadcast(map,session_id))

    elif intentName == 'Register':
        return jsonify(handle_registration(name,dob,sex))

    elif intentName == 'makeAppointment':
        return jsonify(handle_appointment(name,docname,time))

# run the app
if __name__ == '__main__':
    app.run()