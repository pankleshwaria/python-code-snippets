class Vehicle:

    def __init__(self, color, no_of_wheels, no_of_air_bags=0):
        self.color = color
        self.no_of_wheels = no_of_wheels
        self.no_of_air_bags = no_of_air_bags

    # Returns default air bags count
    def get_air_bags_count(self):
        return self.no_of_air_bags


class BMW(Vehicle):

    def __init__(self, color, no_of_wheels, no_of_air_bags, make_type):
        super().__init__(color, no_of_wheels)
        self.make_type = make_type
        self.no_of_air_bags = no_of_air_bags

    def get_air_bags_count(self):
        return self.no_of_air_bags


class Ducati(Vehicle):

    def __init__(self, color, no_of_wheels, make_type):
        super().__init__(color, no_of_wheels)
        self.make_type = make_type


bmw = BMW("Blue", 4, 6, "Premium Sedan")
ducati = Ducati("Red", 2, "Sports Bike")

print(f"BMW are fitted with {bmw.get_air_bags_count()} airbags")
print(f"Ducati are fitted with {ducati.get_air_bags_count()} airbags")
