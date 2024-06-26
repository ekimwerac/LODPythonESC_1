import sys

sys.path.append('./DemoModules')
from employee import Employee
from person import Person

me = Employee("Fred Bloggs", 
              'm', 'IT')
print (me)

if isinstance(me,Employee):
    print(me,"isa Employee!")
    
if isinstance(me,Person):
    print(me,"isa Person!")
    
if issubclass(Employee,Person):
    print("Employee is a subclass of Person")

print(me.get_attr())

print(me.get_name())