"""
This Module fetch data from Database client and
generate responses to be sent as Dialogflow fulfillment.
"""
# import general dependencies
import requests, json

# import Response Generator library
import df_response_lib

# Clients for building responses
fulfillment_client = df_response_lib.fulfillment_response()
actions_client = df_response_lib.actions_on_google_response()

# Base route for Database client
base_url = 'http://2019.almafiesta.com/testing2019/html/ContactFrom_v11/'

# To be implemented
def handle_key_error(error):
    pass

def handle_status_error():
    pass

# Method for returning carousel containing details of all available doctors.
def handle_available_doctors():
    endpoint = base_url + 'availableDoctor.php'
    response = json.loads(requests.get(endpoint).text)
    
    if response['status'] != 1:
        return handle_status_error()

    return actions_client.basic_card('Hello World', 'This is a card subtitle',
        'This is a formatted text.')