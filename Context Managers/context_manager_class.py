# With statement & context managers
# Context managers are a great way for simplifying some of the common resource
# management patterns.
# Resource can be Files, locks or network connections.
# To implement context manager for our class we need to support 2 statements
# __enter__ & __exit__


class FileManager:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileManager('hello.txt') as file:
    file.write('Hello, world!')
