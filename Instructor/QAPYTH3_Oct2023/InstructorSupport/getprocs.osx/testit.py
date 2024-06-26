#!/usr/bin/python3
# Python 3 version
import sys
import getprocs

plist = getprocs.getallprocs()
print(plist)
print("Ref count:", sys.getrefcount(plist[0]))
