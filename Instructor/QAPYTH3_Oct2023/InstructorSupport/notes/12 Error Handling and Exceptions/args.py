import sys

try: 
    f = open("foo") 
except IOError as err: 
    print ("Could not open", 
           err.filename, 
           err.args[1],
           file=sys.stderr)
           
    print ("Exception arguments:",err.args,
           file=sys.stderr)
