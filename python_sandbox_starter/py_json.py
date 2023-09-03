# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

user_json = '{"first_name": "John", "last_name": "Doe", "age": 30}'

#parse to dict
user = json.loads(user_json)
print(user)
print(user['first_name'])



#dict to json
car = {'mark': 'Ford', 'model': 'Mustang', 'year': 1970}
car_json = json.dumps(car)
print(car_json)