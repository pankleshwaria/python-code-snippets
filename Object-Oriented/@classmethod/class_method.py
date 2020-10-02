# Class methods takes class as parameter
# You could you class methods as factory to create objects
# Below is the eg of Pizza class factory


class Pizza:

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza( {self.ingredients} )'

    @classmethod
    def margherita(cls):
        return cls(['cheese', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['cheese', 'tomatoes', 'ham', 'mushrooms'])


print(Pizza.margherita())
print(Pizza.prosciutto())
