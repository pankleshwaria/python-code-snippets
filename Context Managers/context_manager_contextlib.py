# With statement & context managers
# This example we are gonna cover writing context manger using the contextlib library
# Use @contextmanager decorator to function
# Code block inside try works like __enter__ method
# Code block inside finally works like __exit__ method

from contextlib import contextmanager


@contextmanager
def file_manager(name):
    try:
        file = open(name, mode='w')
        yield file
    finally:
        file.close()


with file_manager('hello.txt') as file:
    file.write('Hey you!')
