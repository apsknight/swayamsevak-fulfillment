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