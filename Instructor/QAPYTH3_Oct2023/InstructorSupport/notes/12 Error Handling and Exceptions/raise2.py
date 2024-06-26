import os, sys
class MyError(Exception): 
    pass
        
def myfunc(*arguments):
    #if not all(arguments):
    #    raise MyError("False argument in myfunc")    
        
    except IOError as exc:
        raise CustomError('something went wrong') from exc

        
try:
    myfunc('Tom','',42)
except MyError as err:
    print ("Oops2:",err)
