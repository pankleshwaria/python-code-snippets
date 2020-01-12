# Importing custom module
from my_module import find_index, test

# Importing standard library module
import random

courses = ['History', 'Math', 'Physics', 'CompSci']

print(find_index(courses, 'Math'))
print(test)

random_choice = random.choice(courses)
print(random_choice)

