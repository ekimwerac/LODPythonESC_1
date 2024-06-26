
def make_list(val, times):    
   res = str(val) * times 
   return res

one = make_list(5, 3)
two = make_list(0, 4)
print ("One:",one,"\nTwo:",two)

def print_list(val, times): 
   print (str(val) * times)

print_list (5, 30)

def change_list(inlist, val, times):
    inlist += str(val) * times
    
mylist=[]
change_list(mylist, 'h', 8)
print (mylist)

change_list([], 'h', 8)
 

def print_vat (gross, vatpc=17.5, message='Summary:'):
   net = gross/(1 + (vatpc/100))
   vat = gross - net
   #print (message,'Net: %5.2f' % net, 'Vat: %5.2f' % vat)
   print (message,'Net: {0:5.2f} Vat: {1:5.2f}'.format(net,vat))

print_vat(9.55)

#print_vat2(9.55, ,'Hello')

def calc_vat (gross, vatpc=17.5):
   net = gross/(1 + (vatpc/100))
   vat = gross - net
   return ['{0:05.2f}'.format(net), 
           '{0:05.2f}'.format(vat)]
  


result = calc_vat(42.30)
print ("Result:",result)
   
print (calc_vat(9.55))

