# Generators are functions with yield statement
# You can also chain multiple generators from a single generator


def generator_function1(start, end):
    for i in range(start, end):
        yield i


def generator_function2(start, end):
    for i in range(start, end):
        yield i


def generator_function3(start, end):
    yield from generator_function1(start, end)
    yield from generator_function2(start=5, end=10)
    yield from generator_function2(start=10, end=15)


list_1 = [number for number in generator_function1(1, 5)]
list_2 = [number for number in generator_function2(5, 10)]
list_3 = [number for number in generator_function3(1, 5)]

print(list_1)
print(list_2)
print(list_3)
