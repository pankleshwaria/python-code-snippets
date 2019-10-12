# Use of generator in class


class Actor(object):

    def __init__(self, name, movie, year, awards = None):
        self.name = name
        self.movie = movie
        self.year = year
        self.awards = awards

    # Readable form of object
    def __str__(self):
        return f"{self.name} made {self.movie} in the year {self.year}"

    def __repr__(self):
        return f"Actor('{self.name}', '{self.movie}', {self.year})"

    # Generator function
    def get_awards_won(self):
        for award in self.awards:
            yield award


actor = Actor('Leonardo Dicaprio', 'Titanic', 1997, ['Best Picture', 'Best Director'])
print(actor.__str__())
print(actor.__repr__())
print()

print(f"{actor.movie} won following awards:")
for index, award in enumerate(actor.get_awards_won(), start=1):
    print(index, award)

# can also be called with next()
# print(next(actor.get_awards_won()))
# print(next(actor.get_awards_won()))
