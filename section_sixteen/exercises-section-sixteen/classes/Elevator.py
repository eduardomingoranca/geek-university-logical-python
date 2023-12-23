from classes.Person import Person


def goes_into(name, age, height):
    person = [name, age, height]
    return person


class Elevator(Person):

    def __init__(self, capacity, floors, name, age, height):
        super().__init__(name, age, height)
        self.capacity = capacity
        self.floors = floors

    def leaves(self, name, age, height):
        super().__init__(name, age, height)

    def rise(self, floors):
        self.floors = floors + 1

    def go_down(self, floors):
        self.floors = floors - 1

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_floors(self):
        return self.floors

    def set_floors(self, floors):
        self.floors = floors
