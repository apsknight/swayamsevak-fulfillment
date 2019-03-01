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
