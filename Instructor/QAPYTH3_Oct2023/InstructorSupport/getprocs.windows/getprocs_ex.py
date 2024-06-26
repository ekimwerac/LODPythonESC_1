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

print('')

pids = {pid:value for pid,*value in igetprocs()}
print(pids)
       