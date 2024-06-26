import sys
import getprocs

plist = getprocs.getallprocs()
print(plist)
print("Ref count:",sys.getrefcount(plist[0])) 
print('')

