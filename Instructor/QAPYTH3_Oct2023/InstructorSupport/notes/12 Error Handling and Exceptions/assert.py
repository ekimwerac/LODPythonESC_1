import os, sys

def myfunc(*arguments):
    assert all(arguments), "False argument in myfunc"
    print ("Arguments all OK")
        

myfunc('Tom','',42)
