import sys
import os

def myfunc():
    try:
        f = open("foo") 
    except EnvironmentError as err:
        print (err)
    else:
        print ("Everything is OK")
    finally:
        print ("Finally block", file=sys.stderr)
        
try:
    myfunc()
except Exception: 
    print ("An error occurred", 
           file=sys.stderr)
           
print ("We are all done")