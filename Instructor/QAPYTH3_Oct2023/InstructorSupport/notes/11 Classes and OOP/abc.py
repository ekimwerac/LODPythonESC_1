from abc import *

class Vehicle(metaclass = ABCMeta):
    @abstractmethod
    def getReg(self):
        pass

class Car(Vehicle):
    def getReg(self):
        print("Car isa Vehicle")
        
beepbeep = Car()

beepbeep.getReg()