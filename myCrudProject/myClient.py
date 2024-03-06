import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

#get method
# def get_data(id = None):
#     data = {}
#     if id is not None:
#         data = {'id':id}
#     json_data = json.dumps(data)
#     r = requests.get(url= URL, data = json_data)
#     data = r.json()
#     print(data)

# get_data(2)
    


# post method
# def post_data():
#     data = {
#         'name': 'utsav',
#         'roll': 105,
#         'city': 'Patna'
#     }
    
#     jsonData = json.dumps(data)
#     r = requests.post(url= URL, data = jsonData)
#     data = r.json()
#     print(data)

# post_data()

#update method
def update_data():
    data = {
        'id': 4,
        'name': 'Rahul Kumar',
        'roll': 104,
        'city': 'Godda'
    }
    
    jsonData = json.dumps(data)
    r = requests.put(url= URL, data = jsonData)
    data = r.json()
    print(data)

update_data()


