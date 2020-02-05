# In this tutorial we deal with file IO operations
# File Mode
# r - To read a file
# w - To write a file
# x - Exclusive creation - fails if a file already exists
# a - To append at the end of the file. Create if it dosent exists
# t - Text mode (Default)
# b - Binary mode (For binary file like iages and videos)
# + - To open file in reading or writing mode

# Write file content
content = 'Fruit list'
fruits = ['apple\n', 'oranges\n', 'banana\n', 'grapes\n']

# Writing data to file
todo = open('todo.txt', mode='w', encoding='utf-8')
todo.write(content)
for index, fruit in enumerate(fruits, start=1):
    todo.write(f'{index} {fruit}')
todo.close()

# Writing multiple lines to file
todo = open('todo.txt', mode='w', encoding='utf-8')
todo.writelines(fruits)
todo.close()

# Appending data to file
todo = open('todo.txt', mode='a', encoding='utf-8')
todo.write('Mango')
todo.close()

# Writing file within context manager using with statement
# No need to close the file resource it will automatically be
# closed once it is out of context
print(f'Writing lines within context manager...')
with open('todo.txt', mode='w', encoding='utf-8') as todo:
    for index, fruit in enumerate(fruits, start=1):
        todo.write(f'{index} {fruit}')

print(f'Is file closed... {todo.closed}')

# seek() - Pointer goes to the specific position in the file
with open('todo.txt', mode='a', encoding='utf-8') as todo:

    # Going back to beginning of the line
    print(f'Position of file pointer before seek: {todo.tell()}')
    todo.seek(0)
    print(f'Position of file pointer after seek: {todo.tell()}')

# tell() - Returns the position of the file pointer
with open('todo.txt', mode='a', encoding='utf-8') as todo:

    # Position of file pointer after reading one line
    print(f'Position of file pointer before writing: {todo.tell()}')
    line = todo.write('---THE END---')
    print(f'Position of file pointer after writing one line: {todo.tell()}')

# Check if file is allowed to be read
with open('todo.txt', mode='a', encoding='utf-8') as todo:
    print(f'Is the file seekable: {todo.seekable()}')
    print(f'Is the file writeable: {todo.writable()}')
