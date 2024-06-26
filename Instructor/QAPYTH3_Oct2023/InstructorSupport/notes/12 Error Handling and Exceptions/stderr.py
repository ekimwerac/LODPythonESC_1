import sys

def something_nasty():
    return 1
    
    
if something_nasty():
    print("Invalid types compared", file=sys.stderr)
    exit(1)


