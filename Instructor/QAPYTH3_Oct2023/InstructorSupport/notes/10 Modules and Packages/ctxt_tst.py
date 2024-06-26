import sys

sys.path.append('./DemoModules')

import DemoModules.Ctxt
items = 42

try:
    with DemoModules.Ctxt(items) as ct:
        ct.method()
except (ValueError) as err:
    print ("except trapped",err)