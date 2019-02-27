# import flask dependencies
import requests
import json
from flask import Flask, jsonify, request
from df_response_lib import fulfillment_response

fulfillment_client = fulfillment_response()

# initialize the flask app
app = Flask(__name__)

# default route
base_url = 'http://2019.almafiesta.com/testing2019/html/ContactFrom_v11/'


def handle_available_doctors():
    endpoint = base_url + 'availableDoctor.php'
    resp = json.loads(requests.get(endpoint).text)
    result = ""
    for doctor in resp['data']:
        result = result + doctor['name']

    res = {
        'speech': result,
        'displayText': result,
        'source': 'server'
    }

    return jsonify(res)


@app.route('/', methods=['POST', 'GET'])
def index():
    fulfillment_text = fulfillment_client.fulfillment_text("Test Test!")
    # return jsonify(fulfillment_client.main_response(fulfillment_text, fulfillment_messages=None, output_contexts=None, followup_event_input=None))
    return "Hello"
# create a route for webhook


@app.route('/webhook', methods=['POST'])
def webhook():
    d = json.loads(request.data)
    intentName = d['result']['metadata']['intentName']

    if (intentName == 'available_doctors'):
        return handle_available_doctors()


# run the app
if __name__ == '__main__':
    app.run()
