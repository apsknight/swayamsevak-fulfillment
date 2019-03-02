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

![alt text][logo]

[logo]: https://github.com/apsknight/swayamsevak-fulfillment/tree/master/images/API1.png "Result of API 1"
