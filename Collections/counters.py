from collections import Counter

counter = Counter('Hello')
print(counter) # This will print Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})

# you can find the most common and least common element
counter = Counter([1, 1, 1, 3, 4, 5, 6, 7, 7])
print(counter.most_common(1))

keys = counter.keys()
values = counter.values()
elements = counter.elements()

print("Printing keys....")
for key in keys:
    print(key, sep=' ')

print("Printing values....")
for value in values:
    print(value, sep=' ')

print("Printing elements....")
for element in elements:
    print(element, sep=' ')

# Update collection
counter = Counter([1, 1, 1, 3, 4, 5, 6, 7, 7])
data = [1, 1, 3]
counter.update(data)
print(counter)

# Subtract collection
counter = Counter([1, 1, 1, 3, 4, 5, 6, 7, 7])
data = [1, 1, 3]
counter.subtract(data)
print(counter)

# Clear collection
counter = Counter([1, 1, 1, 3, 4, 5, 6, 7, 7])
counter.clear()
print(counter)

# union
counter1 = Counter({'h': 1, 'e': 2, 'l': 3, 'l': 4, 'o': 5})
counter2 = Counter('lhfhu8')
print(counter1 + counter2)

# intersection
counter1 = Counter({'h': 1, 'e': 2, 'l': 3, 'l': 4, 'o': 5})
counter2 = Counter('lhfhu8')
print(counter1 | counter2)
