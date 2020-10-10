# The Python runtime does not enforce function and variable type annotations.
# They can be used by third party tools such as type checkers, IDEs, linters, etc.

class Person:

    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def greeting(self) -> str:
        print(f'Hello, {self.name}')

    def can_vote(self) -> str:
        if self.is_adult(self.age):
            return 'Yes'
        else:
            return 'No'

    @staticmethod
    def is_adult(age) -> bool:
        if age > 21:
            return True

        return False


professor = Person('Professor', 32, 'Male')
professor.greeting()
print(f'Can vote? {professor.can_vote()}')
