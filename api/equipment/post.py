import requests
import json

def post_queue():
    data = {
        'equipment_id': '12346',
        'user_id': '12345',
        'from_division': 1,
        'to_division': 2,
        'issue_date': '20220807',
    }
    data = json.dumps(data)
    r = requests.post(url='http://127.0.0.1:5000/queue', data=data, headers= {'Content-Type':'application/json'})
    return r.text

def post_equipment():
    r = requests.post('http://127.0.0.1:5000/equip')
    return r.json()