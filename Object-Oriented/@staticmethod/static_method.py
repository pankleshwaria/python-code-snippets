import math


class Pizza:

    def __init__(self, ingredients, radius):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return f'Pizza( {self.ingredients, self.radius} )'

    def area(self):
        return self._circle_area(self.radius)

    @staticmethod
    def _circle_area(radius):
        return radius ** 2 * math.pi


print(Pizza(['cheese'], 5))
print(Pizza(['cheese'], 5).area())

