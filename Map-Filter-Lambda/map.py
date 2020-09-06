# map(func, iterable) function example


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def square(num):
    return num ** 2


sq_list = list(map(square, numbers))
print(sq_list)