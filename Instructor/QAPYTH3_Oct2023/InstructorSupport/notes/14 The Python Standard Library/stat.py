import os, sys
from stat import *

def myfunc(dirname):
    mode = os.stat(dirname)[ST_MODE]
    assert not S_ISDIR, filename+" is not a directory"
    try:
        f = open(filename) 
    except IOError as err:
        print (err)
    
        
try:
    myfunc('stat.py')
except AssertionError as err: 
    print (err, file=sys.stderr)
           
print ("We are all done")