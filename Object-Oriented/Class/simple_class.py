class Employee:

    def __init__(self, first, last, department):
        self.first = first
        self.last = last
        self.email = f"{self.first}.{self.last}@gmail.com"
        self.department = department

    def __str__(self):
        return f"{self.first} {self.last}"

    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.department})"

    def full_name(self):
        return f"{self.first} {self.last}"


emp = Employee("Tony", "Stark", "Avengers")
print(f"This is {emp.full_name()} from {emp.department}")
