
def make_list(val, times):    
   res = str(val) * times 
   return res

one = make_list(5, 3)
two = make_list(0, 4)
print ("One:",one,"(",type(one),")\nTwo:",two)

def print_list(val, times): 
   print (str(val) * times)

print_list (5, 30)

def change_list(inlist, val, times):
    print ("change_list(in) :",inlist)
    inlist += str(val) * times
    print ("change_list(out):",inlist)
    
mylist=[]
change_list(mylist, 'h', 8)
print ('mylist:',mylist)

change_list([], 'h', 8)
 
change_list(mylist[:], 'h', 8)
print ('mylist:',mylist)
