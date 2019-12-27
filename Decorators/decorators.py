import time


def time_it(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        print('{} function took {} milsec'.format(fun.__name__, (end - start) * 1000))
        return result
    return wrapper


@time_it
def cal_square(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result


@time_it
def cal_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result


number_array = range(10000)
print(cal_square(number_array))
print(cal_cube(number_array))

