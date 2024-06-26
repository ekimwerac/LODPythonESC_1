
class Ctxt:
    
    def __init__(self):
        print ("init")
    
    def __enter__(self):
        print ("enter")
        
    def __exit__(self, exc_type, exc_value, traceback):
        print ("exit", exc_type, exc_value, traceback)
        
    def method (self):
        print ("method")
        
    def crash (self):
        raise ValueError("Raised by crash")