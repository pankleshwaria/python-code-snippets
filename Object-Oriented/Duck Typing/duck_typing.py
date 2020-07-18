# Duck Typing and Asking Forgiveness, Not Permission
# In Python, we follow the principle - If it walks like a duck and talks like a duck, it must be a duck
# Which means that Python dosent care which class object it is, if it is an object and required behaviour is present for
# that than it will work.
# The type of object is distinguished only at runtime.


class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:

    def quack(self):
        print("I'm quacking like a duck")

    def fly(self):
        print("I'm flapping my arms")


def quack_and_fly(thing):

    try:
        thing.quack()
        thing.fly()
    except AttributeError as e:
        print(e)

    print()


duck = Duck()
quack_and_fly(duck)

person = Person()
quack_and_fly(person)
