
import requests
from datetime import datetime
import os
nut_id = os.environ.get('nut_id')
nut_key = os.environ.get('nut_key')
sheety_end = os.environ.get('sheety_end')
today=datetime.now()
nut_url = os.environ.get('nut_url')
ask_user = input("Tell me which exercises you've done:\n ")
bearer = os.environ.get('bearer')

nut_headers = {
    "x-app-id": nut_id,
    "x-app-key": nut_key,
}
user_params = {
    "query" : ask_user,
    "gender" : "male",
    "weight_kg" : 60,
    "height_cm" : 173,
    "age" : 25
}

header = {"Authorization": f"Bearer {bearer}"}
response = requests.post(nut_url, json=user_params, headers=nut_headers)
result =response.json()

for i in range(len(result['exercises'])):
  
    data = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": result['exercises'][i]['user_input'].title(),
            "duration": result['exercises'][i]['duration_min'],
            "calories": result['exercises'][i]['nf_calories']
        }
    }

    sh_response = requests.post(sheety_end, json=data, headers=header)
