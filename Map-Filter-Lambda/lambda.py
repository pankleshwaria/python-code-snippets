# In python lambda stands for an anonymous function.
# A lambda function can only perform one lines worth of operations on a given input.

greeting = lambda name: 'Hello ' + name
print(greeting('Viewers'))

# You can also use lambda with map(...) and filter(...) functions

names = ['Sherry', 'Jeniffer', 'Ron', 'Sam', 'Messi']

s_manes = list(filter(lambda name: name.lower().startswith('s'), names))
print(s_manes)

greetings = list(map(lambda name: 'Hey ' + name, s_manes))
print(greetings)
