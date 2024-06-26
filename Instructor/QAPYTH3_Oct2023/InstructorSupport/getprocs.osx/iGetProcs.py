#!/usr/bin/python3
import getprocs

   
###################################################################

def igetprocs():
    
    Retn = getprocs.getfirstproc()
    yield Retn
    
    while Retn:
        Retn = getprocs.getnextproc()
        if Retn:
            yield Retn

###################################################################

for proc in igetprocs():
    print(proc)
