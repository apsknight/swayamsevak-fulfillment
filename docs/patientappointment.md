**Functionality 7**</br>
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