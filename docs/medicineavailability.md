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