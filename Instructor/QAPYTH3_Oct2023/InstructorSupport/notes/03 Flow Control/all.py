
mylist = [0,1,2,3]

if mylist:
    print ("mylist1 is True")

if all(mylist):
    print ("mylist1 all are True")
else:
    print ("mylist1 all are not True")
    
if not all(mylist):
    print ("mylist: all are not True")

if any(mylist):
    print ("At least one item in mylist is true")

    
mylist = []
if mylist:
    print ("mylist2 is True")
 
if all(mylist):
    print ("mylist2 all is True")
    
