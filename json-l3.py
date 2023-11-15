import json

# Math Module

# coverts json into python

jsonn = '{"name": "Umais", "city": "Faislabad", "id": 1}'
con_py = json.loads(jsonn)
print(con_py)


# coverts python into json

pyth = {'name': 'Umais', 'city': 'Faislabad', 'id': 1}
con_jsonn = json.dumps(pyth)
print(con_jsonn)