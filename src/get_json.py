import json
import os
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv

load_dotenv()

class GetJsonFromApi():
    def __init__(self):
        super(GetJsonFromApi, self).__init__()
    
    def get_json(self):
        url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
        step = timedelta(days=1)
        current_date = datetime.now()
        prev_date = current_date - step
        formatted_current_date = current_date.strftime('%Y-%m-%d')
        formatted_prev_date = prev_date.strftime('%Y-%m-%d')
        querystring1 = {f"date":{formatted_prev_date}}
        querystring2 = {f"date": {formatted_current_date}}

        headers = {
            "X-RapidAPI-Key": f"{os.getenv('API_KEY')}",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        response1 = requests.get(url, headers=headers, params=querystring1)
        response2 = requests.get(url, headers=headers, params=querystring2)

        if response1.status_code == 200:
            json_data = response1.json()
            
            with open('data1.json', 'w') as json_file:
                json.dump(json_data, json_file)
            
            print("Data has been written to data.json")
        else:
            print("Failed to retrieve data. Status code:", response1.status_code)

        if response2.status_code == 200:
            json_data = response2.json()
            
            with open('data2.json', 'w') as json_file:
                json.dump(json_data, json_file)
            
            print("Data has been written to data.json")
        else:
            print("Failed to retrieve data. Status code:", response2.status_code)

        with open('data1.json', 'r') as file:
            data1 = json.load(file)

        with open('data2.json', 'r') as file:
            data2 = json.load(file)

        merged_json = data1['response'] + data2['response']

        merged_data = {
            'get': 'fixtures',
            'parameters': {'live': 'all'},
            'errors': [],
            'results': len(merged_json),
            'paging': {'current': 1, 'total': 1},
            'response': merged_json
        }

        with open('data.json', 'w') as file:
            json.dump(merged_data, file, indent=4)

