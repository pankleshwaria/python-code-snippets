class Employee:

    increment = 1.5
    no_of_employees = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees += 1

    def increase(self):
        self.salary = int(self.salary * Employee.increment)

    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount


class Programmer(Employee):

    def __init__(self, fname, lname, salary, prog_lang, exp):
        super().__init__(fname, lname, salary)
        self.prog_lang = prog_lang
        self.exp = exp

    def increase(self):
        self.salary = int(self.salary * (Employee.increment + 0.2))

    def get_experience(self):
        return f'{self.fname} has {self.exp} of experience in {self.prog_lang}'


percy = Programmer('Percy', 'Ankleshwaria', 1000, 'Python', '2 years')
magan = Employee('Magan', 'Fox', 1000)

print(f'{percy.fname} salary before increment {percy.salary}')
print(f'{magan.fname} salary before increment {magan.salary}')

percy.increase()
magan.increase()

print(f'{percy.fname} salary after increment {percy.salary}')
print(f'{magan.fname} salary after increment {magan.salary}')

print(percy.get_experience())
