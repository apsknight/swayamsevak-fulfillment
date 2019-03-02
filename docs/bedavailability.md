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