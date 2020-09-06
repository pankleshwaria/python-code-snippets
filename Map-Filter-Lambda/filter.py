# filter(func, iterable) function example


def starts_with_s(name):
    return name.lower().startswith('s')


def hello_names_with_s(name):
    return 'Hello ' + name


names = ['Sherry', 'Jeniffer', 'Ron', 'Sam', 'Messi']

s_manes = list(filter(starts_with_s, names))
print(s_manes)

# We can also use filter(...) with map(...) function in combination

greetings = list(map(hello_names_with_s, filter(starts_with_s, names)))
print(greetings)