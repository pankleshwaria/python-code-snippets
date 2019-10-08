# import json module
import json

person = [
    {
        "name": "Percy Ankleshwaria",
        "email": "percy@gmail.com",
        "department": "Development"
    },
    {
        "name": "John Davis",
        "email": "john@gmail.com",
        "department": "QA"
    },
    {
        "name": "Kelly Swift",
        "email": "kelly@gmail.com",
        "department": "HR"
    }
]

# dictionary to JSON string
json_str = json.dumps(person, indent=2)
print(json_str)

# JSON to string
json_obj = json.loads(json_str)
print(json_obj)

# writing json to file
filename = "person_info.json"

with open(filename, "w") as json_file:
    json.dump(person, json_file, indent=2)

# reading JSON file
with open(filename, "r") as json_file:
    json_obj = json.load(json_file)
    print(json_obj)
