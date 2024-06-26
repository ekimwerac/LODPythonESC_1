import sys
import os

def myfunc():
    try:
        f = open("foo") 
    finally:
        print ("Finally block", file=sys.stderr)
        
try:
    myfunc()
except EnvironmentError: 
    print ("An Environment error occurred", 
           file=sys.stderr)