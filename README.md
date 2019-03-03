# SwayamSevak Fulfillment Server

Install dependecies using `python3 -m pip install -r requirements.txt`  
Start server in debug mode using `python3 app.py`  

## Supported Queries
Hospital: 
1) Provide me with a list of doctors available right now. [Done] [Trained] 
3) Provide me with a list of doctors by Department. [Done] 
4) Provide me with the schedule of a doctor by name. [Done] 
5) The fee of a doctor.[Done] 
6) Contact details of a doctor by name. [Done] 
7) Is this medicine available right now? [Done] 
9) Are beds available right now (alongside charges)? [Done] 
11) When is my next appointment? [Done] 

## API Endpoint
Base: http://2019.almafiesta.com/testing2019/html/ContactFrom_v11/api/  

allDoctors.php  
allBeds.php  
appointmentByPatient.php?name=<patient_name>  
contactByDoctor.php?name=<doctor_name>  
doctorByDepartment.php?dept=<dept_name>  
feeByDoctor.php?name=<doctor_name>  
medicineByName.php?name=<medicine_name>  
scheduleByDoctor.php?name=<doctor_name>  

**Functionality 1**</br>
This functionality allows the chatbot to show a list of doctors in the hospital right now.</br>
The intent name in Dialogflow backend is **Doctors**</br>
The API call made by the main python application to get the result is [API 1](http://2019.almafiesta.com/testing2019/html/ContactFrom_v11/api/allDoctors.php).</br>
The JSON response returned is of the format:</br>
**status**: *1*, if there is relevant data returned by the API call, *0* if no data is returned.</br>
**data**: A List, where each entry is a JSON object, with the following keys: 
1. name: Name of the doctor
2. phone: Contact room
3. email: Email-id of the doctor
4. room: Which room the doctor is sitting in
5. status: *1* or *0*, based on whether the doctor is on duty or off duty.

![api1](https://user-images.githubusercontent.com/25523604/53680002-d2583f00-3cfa-11e9-966d-6cf5751b7a14.png)

**Functionality 2**</br>
This functionality allows the chatbot to show the schedule of a doctor by name now.</br>
The intent name in Dialogflow backend is **Doctors**</br>
The API call made by the main python application to get the result is [http://2019.almafiesta.com/testing2019/html/ContactFrom_v11/api/scheduleByDoctor.php?name=doctor_name](http://2019.almafiesta.com/testing2019/html/ContactFrom_v11/api/scheduleByDoctor.php?name=<doctor_name>
).</br>
*doctor_name* is the required parameter.</br>
The JSON response returned is of the format:</br>
**status**: *1*, if there is relevant data returned by the API call, *0* if no data is returned.</br>
**data**: A list containing a JSON object, with the following 2 keys: 
1. name: Name of the doctor
2. schedule: A JSON object having 7 keys:
a. monday: *0* if not available; if available displays the time when he is available
b. tuesday: *0* if not available; if available displays the time when he is available
c. wednesday: *0* if not available; if available displays the time when he is available
d. thursday: *0* if not available; if available displays the time when he is available
e. friday: *0* if not available; if available displays the time when he is available
f. saturday: *0* if not available; if available displays the time when he is available
g. sunday: *0* if not available; if available displays the time when he is available


![scheduleofdoctors](https://user-images.githubusercontent.com/25523604/53680080-fd8f5e00-3cfb-11e9-8740-8db290ec49a4.JPG)

**Functionality 3**</br>
This functionality allows the chatbot to shows the ID, fees and room associated with a doctor in the hospital right now.</br>
The intent name in Dialogflow backend is **Doctors**</br>
The API call made by the main python application to get the result is [API 1](http://2019.almafiesta.com/testing2019/html/ContactFrom_v11/api/allDoctors.php).</br>
The JSON response returned is of the format:</br>
**status**: *1*, if there is relevant data returned by the API call, *0* if no data is returned.</br>
**data**: A List, where each entry is a JSON object, with the following keys: 
1. id: id of doctor
2. name: name of doctor
3. fees: fees taken by doctor
4. room: room number of doctor

![feesofdoctor](https://user-images.githubusercontent.com/25523604/53680077-fb2d0400-3cfb-11e9-9408-6087b30ebcfa.JPG)

**Functionality 4**</br>
This functionality allows the chatbot to shows the contact details associated with a doctor in the hospital right now.</br>
The intent name in Dialogflow backend is **Doctors**</br>
The API call made by the main python application to get the result is [API 2](http://2019.almafiesta.com/testing2019/html/ContactFrom_v11/api/contactByDoctor.php).</br>
The JSON response returned is of the format:</br>
**status**: *1*, if there is relevant data returned by the API call, *0* if no data is returned.</br>
**data**: A List, where each entry is a JSON object, with the following keys: 
1. name: name of doctor
2. mobile: mobile number of doctor
3. email: mail address of doctor

![contactofdoctor](https://user-images.githubusercontent.com/25523604/53680076-fb2d0400-3cfb-11e9-9496-78341bda5667.JPG)

**Functionality 5**</br>
This functionality allows the chatbot to shows the availability and ID of medicines right now.</br>
The intent name in Dialogflow backend is **Doctors**</br>
The API call made by the main python application to get the result is [http://2019.almafiesta.com/testing2019/html/ContactFrom_v11/api/medicineByName.php?name=medicine_name
](http://2019.almafiesta.com/testing2019/html/ContactFrom_v11/api/medicineByName.php?name=medicine_name
).</br>
*medicine_name* is required.</br> 
The JSON response returned is of the format:</br>
**status**: *1*, if there is relevant data returned by the API call, *0* if no data is returned.</br>
**data**: A List, where each entry is a JSON object, with the following keys: 
1. id: id of the doctor
2. name: name of doctor
3. status: *1* or *0*, based on whether the medicine is available or not

![medicineavailability](https://user-images.githubusercontent.com/25523604/53680078-fbc59a80-3cfb-11e9-9083-f3a6098cc1b8.JPG)

**Functionality 6**</br>
This functionality allows the chatbot to shows the bed number, room number, room type, charges and status for booking a bed.</br>
The intent name in Dialogflow backend is **Doctors**</br>
The API call made by the main python application to get the result is [http://2019.almafiesta.com/testing2019/html/ContactFrom_v11/api/allBeds.php
](http://2019.almafiesta.com/testing2019/html/ContactFrom_v11/api/allBeds.php).</br>
The JSON response returned is of the format:</br>
**status**: *1*, if there is relevant data returned by the API call, *0* if no data is returned.</br>
**data**: A List, where each entry is a JSON object, with the following keys: 
1. bedno: number of that particular bed
2. roomno: room number where the bed is located
3. roomtype: type of room where the bed is located
4. charges: price of booking the bed
5. status: *1* or *0*, based on whether the bed is available or not

![bedavailability](https://user-images.githubusercontent.com/25523604/53680075-fa946d80-3cfb-11e9-97b3-af92b7803565.JPG)

**Functionality 7**</br>
Try saying any one of the following phrases for getting help from the bot regarding things it can do:</br>
**Help**, <b>What can you do?</b>, <b>I need help</b></br>
You will get a list of the various functionalities the chatbot can perform, which are:</br>
1. Finding all the doctors present within the hospital.
2. Finding the schedule of a doctor by name.
3. Getting the fees of a doctor by name.
4. Getting the contact details of any doctor.
5. Checking the availability status of a medicine.
6. Checking the next appointment date with the doctor.
7. Getting remote help from support stuff via video call.

**Functionality 8**</br>
This functionality allows the chatbot to shows the Patient ID, name, doctor name, date and time for a particular patient's appointment.</br>
The intent name in Dialogflow backend is **Doctors**</br>
The API call made by the main python application to get the result is [appointmentByPatient.php?name=patient_name](http://2019.almafiesta.com/testing2019/html/ContactFrom_v11/api/appointmentByPatient.php?name=patient_name).</br>
*patient_name* is the required parameter.</br>
The JSON response returned is of the format:</br>
**status**: *1*, if there is relevant data returned by the API call, *0* if no data is returned.</br>
**data**: A List, where each entry is a JSON object, with the following keys: 
1. id: id of patient
2. name: name of patient
3. doctor: name of doctor assigned
4. date: date and time of appointment

![patientappointment](https://user-images.githubusercontent.com/25523604/53680079-fc5e3100-3cfb-11e9-88c5-53556289647b.JPG)
