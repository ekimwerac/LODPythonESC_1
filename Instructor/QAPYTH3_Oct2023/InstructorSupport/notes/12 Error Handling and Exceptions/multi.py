import sys

filename = "foo"
# filename = 42
try: 
    f = open(filename) 
except IOError:
    errmsg = "Could not open foo"
except (TypeError,ValueError):
    errmsg = "Invalid filename"
    
if errmsg != "":
    exit(errmsg)
    

