result = 3

def myfunc():
    result = 12
    def scope_test():
        nonlocal result
        print(result)
        if result < 45:
            result += 1
            scope_test()
            
    scope_test()
    print (result,"from myfunc")

myfunc()
print (result,"from main")