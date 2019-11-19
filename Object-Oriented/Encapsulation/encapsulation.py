# In Python, we denote private attribute using underscore as prefix i.e single “ _ “ or double “ __“.


class Employee:

    def __init__(self, first, last, department, pay=None):
        self.first = first
        self.last = last
        self.email = f"{self.first}.{self.last}@gmail.com"
        self.department = department
        self.__pay = pay

    def get_full_name(self):
        return f"{self.first} {self.last}"

    def set_pay(self, pay):
        self.__pay = pay

    def get_pay(self):
        return self.__pay


emp = Employee('Wade', 'Wilson', 'Acting')
emp.set_pay(100)

# Does not change the pay as __pay is a private attribute
emp.__pay = 2000
print(f"{emp.get_full_name()} get ${emp.get_pay()} a movie")
