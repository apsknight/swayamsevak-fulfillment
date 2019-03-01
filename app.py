# import libraries
import json

# import flask dependencies
from flask import Flask, jsonify, request

# import response functions for intent requests
from fetch import *

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

    print (json.dumps(content,indent=2))

    try:
        intentName = content['result']['metadata']['intentName']
    except KeyError as e:
        return jsonify(handle_key_error(e))

    if intentName == 'Doctors':
        return jsonify(handle_all_doctors())
    elif intentName == 'videoCall':
        return jsonify(handle_video_call())
    elif intentName == 'doctorFee':
        return jsonify(handle_fee_doctors(content['result']['parameters']['name']))
    elif intentName == 'GetSchedule':
        return jsonify(handle_schedule_doctors(content['result']['parameters']['name']))

# run the app
if __name__ == '__main__':
    app.run()