"""
This Module fetch data from Database client and
generate responses to be sent as Dialogflow fulfillment.
"""
# import general dependencies
import requests, json
import datetime

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
    return{
        "speech": "I could not find what you were looking for."
    }

# Method for returning carousel containing details of all available doctors.
def handle_all_doctors():
    endpoint = base_url + 'allDoctors.php'
    response = json.loads(requests.get(endpoint).text)

    if response['status'] != 1:
        return handle_status_error()

    template = {
        "speech": "These are all the doctors in the hospital",
        "displayText": "No",
        "messages": [{
            "type": "carousel_card",
            "items": [
            ]
        }]
    }  

    for item in response['data']:
        data = {
            "heading": item['name'],
            "status": item['status'],
            "title1": "Department: "+item['department'],
            "title2": "Room: "+item['room']
        }
        template['messages'][0]['items'].append(data)

    return template

    # return actions_client.carousel_card(response)

    # return {
    #     "speech": "I want to wrie this"
    #     "messages": [{
    #         "type": "carousel_card",
    #         "items": [
    #             {
    #                 "title": "Doctor Singh",
    #                 "id": "C01",
    #                 "image": {
    #                     "url": "https://user-images.githubusercontent.com/29799995/53495668-6392a000-3ac6-11e9-8f15-a66dede37a1d.png",

    #                 },
    #                 "optionInfo": {
    #                     "key": "K01"
    #                 },
    #                 "description": "Room No: 54, Phone Number: 6789"
    #             },
    #             {
    #                 "title": "Doctor Madhav",
    #                 "id": "C02",
    #                 "image": {
    #                     "url": "https://user-images.githubusercontent.com/29799995/53495668-6392a000-3ac6-11e9-8f15-a66dede37a1d.png",

    #                 },
    #                 "optionInfo": {
    #                     "key": "K02"
    #                 },
    #                 "description": "Room No: 44, Phone Number: 7789"
    #             }
    #         ]
    #     }],
    #     "source": "flask",
    # }

def handle_all_Beds(type):
    endpoint = base_url + 'allBeds.php'
    response = json.loads(requests.get(endpoint).text)
    
    if response['status'] != 1:
        return handle_status_error()

    template = {
        "speech": "These are the beds satisfying your requirement",
        "displayText": "No",
        "messages": [{
            "type": "carousel_card",
            "items": [
            ]
        }]
    }  

    if type=="":
        for item in response['data']:
            data = {
                "heading": item['roomtype'],
                "status": item['status'],
                "title1": "BedNo: "+item['bedno'],
                "title2": "Charges: "+item['charges']
            }
            template['messages'][0]['items'].append(data)
    else:
          for item in response['data']:
            if item['roomtype']==type:
                data = {
                    "heading": item['roomtype'],
                    "status": item['status'],
                    "title1": "BedNo: "+item['bedno'],
                    "title2": "Charges: "+item['charges']
                }
                template['messages'][0]['items'].append(data)      

    return template

def handle_patient_appointments(name):
    endpoint = base_url + 'appointmentByPatient.php?name='+name
    response = json.loads(requests.get(endpoint,).text)
    
    if response['status'] != 1:
        return handle_status_error()

    template = {
        "speech": "Your id is "+response['data'][0]['id']+"and appointment is on "+response['data'][0]['date']
    }

    return template

def handle_doctors_contact(name):
    endpoint = base_url + 'contactByDoctor.php?name='+name
    response = json.loads(requests.get(endpoint).text)
    
    if response['status'] != 1:
        return handle_status_error()

    item=response['data'][0]

    template = {
        "speech": "This is the contact information of the doctor. You can click on the button to compose a mail",
        "displayText": "No",
        "messages": [{
            "type": "basic_card",
            "heading": item['name'],
            "title1": "Mobile: "+item['mobile'],
            "title2": "Email: "+item['email'],
            "button": {
                "title1": "Mail Doctor",
                "uri1": "mailto:"+item['email'],
                "title2": "Call Doctor",
                "uri2": "tel:"+item['mobile']
            }
        }]
    }

    return template 

def handle_department_doctors(dept):
    endpoint = base_url + 'doctorByDepartment.php?dept='+dept
    response = json.loads(requests.get(endpoint).text)
    
    if response['status'] != 1:
        return handle_status_error()

    template = {
        "speech": "These are the doctors in "+dept,
        "displayText": "No",
        "messages": [{
            "type": "carousel_card",
            "items": [
            ]
        }]
    }  

    for item in response['data']:
        data = {
            "heading": item['name'],
            "status": item['status'],
            "title1": "Phone: "+str(item['phone']),
            "title2": "Room: "+item['room']
        }
        template['messages'][0]['items'].append(data)

    return template

def handle_fee_doctors(name):
    endpoint = base_url + 'feeByDoctor.php?name='+name
    response = json.loads(requests.get(endpoint).text)
    
    if response['status'] != 1:
        return handle_status_error()

    template = {
        "speech": "His fees is ₹ "+response['data'][0]['fees']
    }

    return template

def handle_medicines(name):
    endpoint = base_url + 'medicineByName.php?name='+name
    response = json.loads(requests.get(endpoint).text)
    
    if response['status'] != 1:
        return handle_status_error()

    if response['data'][0]['status'] == 1:   
        template = {
            "speech": "The medicine "+response['data'][0]['name']+" is available"
        }
    else:
        template = {
            "speech": "The medicine "+response['data'][0]['name']+" is unavailable"
        }        

    return template


def handle_schedule_doctors(name):
    endpoint = base_url + 'scheduleByDoctor.php?name='+name
    response = json.loads(requests.get(endpoint).text)
    
    if response['status'] != 1:
        return handle_status_error()

    template = {
        "speech": response['data'][0]['name']+" is available on the following days",
        "displayText": "No",
        "messages": [{
            "type": "carousel_card",
            "items": [
            ]
        }]
    }  

    item = response['data'][0]['schedule']
    if item['monday']!='0':
        data = {
            "heading": "Monday",
            "title1": "Timings: "+item['monday']
        }
        template['messages'][0]['items'].append(data)
    if item['tuesday']!='0':
        data = {
            "heading": "Tuesday",
            "title1": "Timings: "+item['tuesday']
        }
        template['messages'][0]['items'].append(data)
    if item['wednesday']!='0':
        data = {
            "heading": "Wednesday",
            "title1": "Timings: "+item['wednesday']
        } 
        template['messages'][0]['items'].append(data)           
    if item['thursday']!='0':
        data = {
            "heading": "Thursday",
            "title1": "Timings: "+item['thursday']
        }
        template['messages'][0]['items'].append(data) 
    if item['friday']!='0':
        data = {
            "heading": "Friday",
            "title1": "Timings: "+item['friday']
        }
        template['messages'][0]['items'].append(data) 
    if item['saturday']!='0':
        data = {
            "heading": "Saturday",
            "title1": "Timings: "+item['saturday']
        }
        template['messages'][0]['items'].append(data) 
    if item['sunday']!='0':
        data = {
            "heading": "Sunday",
            "title1": "Timings: "+item['sunday']
        }
        template['messages'][0]['items'].append(data) 
    else:
        data={}

    template['messages'][0]['items'].append(data)

    return template 

def handle_video_call():
    return{
        "speech": "Click on the button to start, when you are ready",
        "displayText": "No",
        "messages": [{
            "type": "basic_card",
            "heading": "Customer Support",
            "title1": "Here you go",
            "button": {
                "title1": "Call",
                "uri1": "https://madhavchoudhary.github.io/swayamsevak-call/Basic%20Video%20Chat/"
            }
        }]
    }     

def handle_help():
     return{
        "speech": "These are the things I can do!",
        "messages": [
        {
            "type":"simple",
            "speech":"Provide you with a list of doctors."
        },
        {
            "type":"simple",
            "speech":"Provide you with the schedule of a doctor."
        },
        {
            "type":"simple",
            "speech":"Tell the fee of a doctor."
        },
        {
            "type":"simple",
            "speech":"Give you the contact details of a doctor."
        },
        {
            "type":"simple",
            "speech":"Check availability of a medicine."
        },
        {
            "type":"simple",
            "speech":"Give you details of beds availability and charges."
        },
        {
            "type":"simple",
            "speech":"Check your next appointment."
        }, 
         {
            "type":"simple",
            "speech":"Connect you via video call to the support staff."
        },             
        ]
    }

def handle_broadcast(map,session_id):
    endpoint = base_url + 'broadcast.php?'
    response = json.loads(requests.get(endpoint).text)
    
    if response['status'] != 1:
        return {}

    template = {
        "displayText": "No",
        "messages": []
    }

    for item in response['data']:
        # print (datetime.datetime.now().strftime("%H:%M:%S")+" "+item['mtime'])
        if datetime.datetime.now().strftime("%H:%M:%S")>=item['mtime'] and map.get(session_id,'0')<item['id']:
            map[session_id]=item['id']
            # print("Got "+session_id+" for "+item['id'])
            data = {
                "type": "broadcast_card",
                "announcement": item['mdata']
            }
            template['messages'].append(data)

    return template

def handle_register(name, dob, sex):
    endpoint = base_url + 'register.php?name='+name+'&dob='+dob+'&sex='+sex
    response = json.loads(requests.get(endpoint).text)

    if response['status'] != 1:
        handle_status_error()

    return{
        "speech": "Registration Successful"
    }

def handle_register(name, docname, time):
    endpoint = base_url + 'appointment.php?name='+name+'&docname='+docname+'&time='+time
    response = json.loads(requests.get(endpoint).text)

    if response['status'] != 1:
        return{
            "speech": "Slot Not free, try another slot"
        }

    return{
        "speech": "Registration Successful"
    }