import os, sys
#class CustomError(Exception): 
#        pass
        
def myfunc(*arguments):
    if not all(arguments):
        raise ValueError("False argument in myfunc")    
        
    #except IOError as exc:
    #    raise CustomError('something went wrong') from exc

        
try:
    myfunc('Tom','',42)
except ValueError as err:
    print ("Oops:",err)
