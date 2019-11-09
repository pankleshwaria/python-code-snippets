#       Parent
#       /   \
#   ChildA  ChildB
#       \   /
#       GrandChild


class Parent:

    def __init__(self, name, serial):
        self.name = name
        self.serial = serial

    def speaks(self):
        print("Parent speaks")


class ChildA(Parent):

    def __init__(self, a_name, a_serial, **kwargs):
        self.a_name = a_name
        self.a_serial = a_serial
        super().__init__(**kwargs)

    def speaks(self):
        print("ChildA speaks")
        super().speaks()


class ChildB(Parent):

    def __init__(self, b_name, b_serial, **kwargs):
        self.b_name = b_name
        self.b_serial = b_serial
        super().__init__(**kwargs)

    def speaks(self):
        print("ChildB speaks")
        super().speaks()


class GrandChild(ChildA, ChildB):

    def __init__(self):
        super().__init__(name='blah', a_name='a blah', b_name='b blah', a_serial=60, b_serial=65, serial=85)

    def speaks(self):
        print("GrandChild speaks")
        super().speaks()


grand_child = GrandChild()
print(f"ChildA name is {grand_child.a_name}")
print(f"ChildB name is {grand_child.b_name}")
print(f"Parent name is {grand_child.name}")
print()
grand_child.speaks()

