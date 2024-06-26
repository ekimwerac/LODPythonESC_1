import sys

sys.path.append('./DemoModules')
from person import Person

me = Person("Clive Darke", 'm')
print(me)

if hasattr(me, '__str__'):
    print("Person has __str__")
else:
    print("Person does not have __str__")


