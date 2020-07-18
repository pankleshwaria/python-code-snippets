# static and class methods


class Person:

    # class or static variable
    population = 50

    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    @classmethod
    def get_population(cls):
        return cls.population

    @staticmethod
    def is_adult(age):
        return age > 18

    def display(self):
        print(f'{self.name} is {self.age} years old')


person1 = Person('Jack', 'Doe')
person2 = Person('Bob', 'Marley')

Person.population += 5

print(person1.population)
print(person2.population)
