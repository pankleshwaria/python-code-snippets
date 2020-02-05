# In this tutorial we deal with file IO operations
# File Mode
# r - To read a file
# w - To write a file
# x - Exclusive creation - fails if a file already exists
# a - To append at the end of the file. Create if it dosent exists
# t - Text mode (Default)
# b - Binary mode (For binary file like iages and videos)
# + - To open file in reading or writing mode

# Read file content
todo = open('todo.txt', mode='r', encoding='utf-8')
content = todo.read()
todo.close()
print(content)

# Read with byte size
byte_size = 10
todo = open('todo.txt', mode='r', encoding='utf-8')
print(f'Reading only {byte_size} bytes...')
content = todo.read(byte_size)
todo.close()
print(content)

print(f'Reading single line...')
todo = open('todo.txt', mode='r', encoding='utf-8')
content = todo.readline()
todo.close()
print(content)

print(f'Reading line by line...')
todo = open('todo.txt', mode='r', encoding='utf-8')
lines = todo.readlines()
todo.close()
for line in lines:
    print(line, end='')

# Reading file within context manager using with statement
# No need to close the file resource it will automatically be
# closed once it is out of context
print(f'Reading lines within context manager...')
with open('todo.txt', mode='r', encoding='utf-8') as todo:
    for line in todo:
        print(line, end='')

print(f'Is file closed... {todo.closed}')

# seek() - Pointer goes to the specific position in the file
with open('todo.txt', mode='r', encoding='utf-8') as todo:
    line = todo.readline()

    # Going back to beginning of the line
    print(f'Position of file pointer before seek: {todo.tell()}')
    todo.seek(0)
    print(f'Position of file pointer after seek: {todo.tell()}')

# tell() - Returns the position of the file pointer
with open('todo.txt', mode='r', encoding='utf-8') as todo:
    line = todo.readline()
    # Position of file pointer after reading one line
    print(f'Position of file pointer after reading one line: {todo.tell()}')

# Check if file is allowed to be read
with open('todo.txt', mode='r', encoding='utf-8') as todo:
    print(f'Is the file seekable: {todo.seekable()}')
    print(f'Is the file readable: {todo.readable()}')
