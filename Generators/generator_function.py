# Generators are functions with yield statement


# generator function
# return single value at a time
# Waits for next iteration i.e next() to be called
def get_actor_names(actors):
    for actor in actors:
        yield actor


actors = ['Leonardo Dicaprio', 'Brad Pitt', 'Hugh Jackman', 'Hugh Laurie']

# Return a generator object <generator object get_actor_names at 0x103360eb8>
actors_list = get_actor_names(actors)

# A generator object is iterator, means you can use next() function on it
# Its also an iterable, you can loop through it
print(next(actors_list))
print(next(actors_list))
print(next(actors_list))
print()

# Regenerate the items as the generator is exhausted from previous 3 iterations
actors_list = get_actor_names(actors)

for actor in actors_list:
    print(actor)
