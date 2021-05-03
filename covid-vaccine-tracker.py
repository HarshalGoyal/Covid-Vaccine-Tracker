import requests
import json 
import datetime

url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin'

pin =str(input("Enter the pin: "))
print("\n")

for i in range(1,8):
    date_check = datetime.date.today() 
    date_check = date_check + (datetime.timedelta(days=i)) 
    date_check = str(date_check)
    date_check = date_check.split('-')
    date_check = '-'.join(date_check[::-1])
    
    new_url = url + '?pincode='+pin+'&date='+ date_check

    r = requests.get(new_url)
    file_fetched = r.json()

    parameters = ["name","fee_type","sessions"]
    session_params = ["slot","date","available_capacity","min_age_limit","slots"]
    print("Date: ",date_check)
    for key,value in file_fetched.items():
        if  bool(len(value)):
            for i in range(0,len(value)):
                fetched_data = (value[i])
                for key_data,value_data in fetched_data.items():
                    if key_data in parameters:
                        if(key_data == "sessions"):
                            fetched_session_details =value_data[0]
                            for key_session,value_session in fetched_session_details.items():
                                if key_session in session_params:
                                    print(key_session+' : ',value_session)
                        else:
                            print(key_data+' : ',value_data)
                print("\n")
        else:
            print("No vaccine available on the specified date!")