import pickle


class Employee:

    def __init__(self, first_name, last_name, email, department):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.department = department


# Serializing / Pickling - converting a Python object into a byte stream
employee = Employee('Johnny', 'Walter', 'jwalter@gmail.lcl', 'IT')

serialized_employee = pickle.dumps(employee)
print(serialized_employee)

# Serializing and writing to a file
with open('serialized_data.txt', mode='wb') as file:
    pickle.dump(serialized_employee, file)

# Unserializing / Unpickling - converting byte string to Python object
emp = pickle.loads(serialized_employee)

# Unserializing data from file
with open('serialized_data.txt', mode='rb') as r_file:
    employee = pickle.load(r_file)
    print(employee)

