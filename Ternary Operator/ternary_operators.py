# Use of ternary operators in Python
# Syntax [on_true] if [condition] else [on_false]
from random import randint


age = 10
print("Is Adult" if age > 18 else "Is Minor")

a, b = randint(1, 10), randint(1, 10)
max = 'a' if a > b else 'b'
print(max)
print(a, b)


# Ternary operator using Tuple, Dictionary & lambda
# Tuple syntax: (on_true, on_false) [condition]

a, b = randint(1, 10), randint(1, 10)
print(('a', 'b')[a > b])
print(a, b)

# Dictionary syntax: {True: [on_true], False: [on_false]} [condition]
a, b = randint(1, 20), randint(1, 20)
print({True: 'a', False: 'b'}[a > b])
print(a, b)

# Lambda syntax: (lambda: [on_true], lambda: [on_false])[condition]
print((lambda: a, lambda: b)[a > b])

# Nested ternary operator

a, b = 10, 20
print('Both a & b are equal' if a == b else 'a is greater than b' if a > b else 'b is greater than a')
