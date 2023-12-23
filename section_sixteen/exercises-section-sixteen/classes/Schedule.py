from classes.Person import Person


class Schedule(Person):

    def stores_person(self, name, age, height):
        super().__init__(name, age, height)

    def remove_person(self, name):
        self.set_name(name)

    def search_person(self, name):
        return name

    def print_schedule(self):
        print(self._name)
        print(self._age)
        print(self._height)
