#
import json

#
data1 = {
    'name': 'Bubba',
    'animal': 'Cat',
    'age':2,
    'city': 'Seattle, WA',
    'interests': ['Purring', 'Eating', 'Napping', 'Playing', 'Belly rubs'],
    'is_student': False
}

# Creating a JSON and writing the python object contents to the JSON
with open('data1.json','w') as json_file:

    json.dump(data1,json_file,indent=4)

print("Data has been written to data1.json")