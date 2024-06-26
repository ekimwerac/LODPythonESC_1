import sys

sys.path.append('./DemoModules')

#import mymodule

#print (sys.path)

#mymodule.myfunc()

# Alias
#import mymodule as fred

#fred.myfunc1()

#from mymodule import myfunc1

#myfunc1()

#from mymodule import \
#     (myfunc1 as fred, myfunc2 as jim)
#
#fred()
#jim()

import DemoModules.MyModuleA
import DemoModules.MyModuleB
import DemoModules.MyModuleB

DemoModules.MyModuleA.MyFunc1()
DemoModules.MyModuleB.MyFunc1()

print (DemoModules.MyModuleB.var1)
print ("Module:", DemoModules.MyModuleA.__doc__)
print (DemoModules.MyModuleA.MyFunc1.__doc__)
