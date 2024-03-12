import json
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

class GetJsonFromApi():
    def __init__(self):
        super(GetJsonFromApi, self).__init__()
    
    def get_json(self):
        url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
        current_date = datetime.now()
        formatted_date = current_date.strftime('%Y-%m-%d')
        querystring = {f"date":{formatted_date}}

        headers = {
            "X-RapidAPI-Key": f"{os.getenv('API_KEY')}",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            json_data = response.json()
            
            file_path = "data.json"
            with open(file_path, 'w') as json_file:
                json.dump(json_data, json_file)
            
            print("Data has been written to", file_path)
        else:
            print("Failed to retrieve data. Status code:", response.status_code)

