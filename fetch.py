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
base_url = 'http://2019.almafiesta.com/testing2019/html/ContactFrom_v11/api/'

# To be implemented
def handle_key_error(error):
    pass

def handle_status_error():
    pass

# Method for returning carousel containing details of all available doctors.
def handle_all_doctors():
    endpoint = base_url + 'allDoctors.php'
    response = json.loads(requests.get(endpoint).text)
    
    if response['status'] != 1:
        return handle_status_error()

    return actions_client.basic_card('Hello World', 'This is a card subtitle',
        'This is a formatted text.')

def handle_all_Beds():
    endpoint = base_url + 'allBeds.php'
    response = json.loads(requests.get(endpoint).text)
    
    if response['status'] != 1:
        return handle_status_error()

    return actions_client.basic_card('Hello World', 'This is a card subtitle',
        'This is a formatted text.')

def handle_patient_appointments(name):
    endpoint = base_url + 'appointmentByPatient.php?name='+name
    response = json.loads(requests.get(endpoint,).text)
    
    if response['status'] != 1:
        return handle_status_error()

    return actions_client.basic_card('Hello World', 'This is a card subtitle',
        'This is a formatted text.')

def handle_doctors_contact(name):
    endpoint = base_url + 'contactByDoctor.php?name='+name
    response = json.loads(requests.get(endpoint).text)
    
    if response['status'] != 1:
        return handle_status_error()

    return actions_client.basic_card('Hello World', 'This is a card subtitle',
        'This is a formatted text.')

def handle_department_doctors(dept):
    endpoint = base_url + 'doctorByDepartment.php?dept='+dept
    response = json.loads(requests.get(endpoint).text)
    
    if response['status'] != 1:
        return handle_status_error()

    return actions_client.basic_card('Hello World', 'This is a card subtitle',
        'This is a formatted text.')

def handle_fee_doctors(name):
    endpoint = base_url + 'feeByDoctor.php?name='+name
    response = json.loads(requests.get(endpoint).text)
    
    if response['status'] != 1:
        return handle_status_error()

    return actions_client.basic_card('Hello World', 'This is a card subtitle',
        'This is a formatted text.')

def handle_medicines(name):
    endpoint = base_url + 'medicineByName.php?name='+name
    response = json.loads(requests.get(endpoint).text)
    
    if response['status'] != 1:
        return handle_status_error()

    return actions_client.basic_card('Hello World', 'This is a card subtitle',
        'This is a formatted text.')

def handle_schedule_doctors(name):
    endpoint = base_url + 'scheduleByDoctor.php?name='+name
    response = json.loads(requests.get(endpoint).text)
    
    if response['status'] != 1:
        return handle_status_error()

    return actions_client.basic_card('Hello World', 'This is a card subtitle',
        'This is a formatted text.')
