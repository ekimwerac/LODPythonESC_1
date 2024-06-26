#======================================================================
#
#  Filename:     stack.pyc
#  Description:  Definition and implementation of the stack class
#
#======================================================================

class stack:               

    # constructor
    def __init__(self, s):
        print ("\nHello from the stack constructor")
        self._size = int(s)				
        self._pdata = []		

    # Destructor
    def __del__(self):
        print ("Au revoir from the stack destructor")

    def push(self,value):       
        
        if len(self._pdata) < self._size:
            self._pdata.append(value)
        else:
            print ("Stack size reached")
            self._size *= 2

    def pop(self):
        if len(self._pdata) == 0:
            print ("Oops! The stack is empty (returning -1 instead)")
            return -1
        else:
            return self._pdata.pop()
