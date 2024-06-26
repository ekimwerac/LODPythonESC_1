from person import Person

class Employee(Person):

    def __init__ (self, name, gender, dept):
        super().__init__(name, gender)
        self__dept = dept