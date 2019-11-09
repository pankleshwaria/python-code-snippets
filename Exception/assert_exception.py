# Assertions are statements that assert or state a fact confidently in your program. For example,
# while writing a division function, you're confident the divisor shouldn't be zero,
# you assert divisor is not equal to zero.
#
# Assertions are simply boolean expressions that checks if the conditions return true or not.
# If it is true, the program does nothing and move to the next line of code. However, if it's false,
# the program stops and throws an error.


def average(marks):
    assert len(marks) != 0, "Cannot be an empty list"

    avg_marks = sum(marks)/len(marks)
    return avg_marks


marks_list = [10, 15, 25, 33, 42, 50]
avg_score = average(marks_list)
print(f'Avg score is {avg_score}')

# throws an assert error
marks_list = []
avg_score = average(marks_list)
print(f'Avg score is {avg_score}')

# Assert using classes


class Person:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def vote(self):

        assert self.age > 18, f"Hey {self.name} you need to be an adult to vote"
        print("I vote for humanity!!")


mike = Person('Mike Poser', 'Male', 10)
mike.vote()
