from person import Person

class Employee(Person):

    def __init__ (self, name, gender, dept):
        super().__init__(name, gender)
        self.__dept = dept
        self.stuff = 'Employee stuff'
        
    def get_attr (self):
        return (self.__dept, self.public)    
        
    def __some_name (self):
       print("some_name",self.__class__.__name__)