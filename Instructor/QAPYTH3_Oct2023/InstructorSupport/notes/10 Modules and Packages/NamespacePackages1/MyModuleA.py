# comment

"""This is a test module containing two
functions, MyFunc1 and MyFunc2 (at start)"""

import sys

#__doc__ = """This is a test module containing two
#functions, MyFunc1 and MyFunc2"""

var1 = 42

def MyFunc1():
    "MyFunc1 has no parameters and prints 'Hello'"
    print ("Hello from", __name__)
    
def MyFunc2():
    print ("Goodbye from", __name__)

