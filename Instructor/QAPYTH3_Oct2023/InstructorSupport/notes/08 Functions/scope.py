result = 3

def scope_test1():    
   result = 42

scope_test1()
print (result)   # prints 3

def scope_test2():    
   global result
   result = 42

scope_test2()
print (result)   # prints 42

def scope_test3():
   global result
   result = 37
   
   
scope_test3()
print (result)   # prints 42