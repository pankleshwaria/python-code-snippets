class Employee:

    raise_amt = 1.5

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{self.first}.{self.last}@gmail.com"
        self.pay = pay

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        if self.employees is not None:
            for emp in self.employees:
                print(f"=> {emp.full_name()} earns ${emp.pay}")


dev1 = Developer("Elliot", "Alderson", 1000, "Python")
dev2 = Developer("Thomas", "Anderson", 1000, "C")

manager = Manager("Morpheus", "", 1000, [dev1])
manager.add_emp(dev2)

print(f"{manager.full_name()} team")
manager.print_emps()

manager.apply_raise()
dev1.apply_raise()
dev2.apply_raise()

print()
print(f"{manager.full_name()} after raise")
print(f"{manager.full_name()} earns ${manager.pay}")

print()
print(f"{manager.full_name()} team after raise")
manager.print_emps()

