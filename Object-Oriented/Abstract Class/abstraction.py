# This is an abstract class. Abstract class is a class with one or more abstact method.
# You cant initialize abstract class. Abstract classes are incomplete because they have methods which have no body.

from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def no_of_sides(self):
        pass

    @staticmethod
    @abstractmethod
    def shape_name():
        pass


class Triangle(Polygon):

    def no_of_sides(self):
        print("I have 3 sides")

    @staticmethod
    def shape_name():
        print("Its Triangle")


class Pentagon(Polygon):

    def no_of_sides(self):
        print("I have 5 sides")

    @staticmethod
    def shape_name():
        print("Its Pentagon")


class Hexagon(Polygon):

    def no_of_sides(self):
        print("I have 6 sides")

    @staticmethod
    def shape_name():
        print("Its Hexagon")


class Quadrilateral(Polygon):

    def no_of_sides(self):
        print("I have 4 sides")

    @staticmethod
    def shape_name():
        print("Its Quadrilateral")


triangle = Triangle()
triangle.shape_name()
triangle.no_of_sides()

quadrilateral = Quadrilateral()
quadrilateral.shape_name()
quadrilateral.no_of_sides()

pentagon = Pentagon()
pentagon.shape_name()
pentagon.no_of_sides()

hexagon = Hexagon()
hexagon.shape_name()
hexagon.no_of_sides()

