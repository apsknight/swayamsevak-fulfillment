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