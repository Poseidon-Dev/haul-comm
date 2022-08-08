import requests

def get_queue():
    r = requests.get('http://127.0.0.1:5000/queue')
    return r.json()

def get_equipment():
    r = requests.get('http://127.0.0.1:5000/equip')
    return r.json()