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