
def outer():
    num = 42

    def inner():
        print (num, "in inner")
        
    inner();
    print (num, "in outer")
    
    
outer()
inner()