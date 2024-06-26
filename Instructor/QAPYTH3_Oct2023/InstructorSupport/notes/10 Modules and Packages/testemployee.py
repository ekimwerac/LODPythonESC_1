import sys

sys.path.append('./DemoModules')
from employee import Employee

me = Employee ("Fred Bloggs", 
               'm', 'IT')
print (me)