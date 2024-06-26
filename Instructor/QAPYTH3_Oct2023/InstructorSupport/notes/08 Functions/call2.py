def myfunc (arg1, *arg2):
    print ("arg1:", arg1, "arg2:", arg2)
    
myfunc('The', 'quick', 'brown', 'fox')

def print_vat (**arg):
   print (arg)

print_vat(vatpc=15, gross=9.55, message='Summary')

def print_vat (**arg1, arg2):
    pass