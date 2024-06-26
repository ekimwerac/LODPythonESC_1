
def sum (*args):
    total = 0
    for arg in args:
        total += arg
    return total
    
print (sum(3,6,42,1))
print (sum())

def print_vat (*, gross=0, vatpc=17.5, message='Summary:'):
   net = gross/(1 + (vatpc/100))
   vat = gross - net
   print  (message,'Net: {0:5.2f} Vat: {1:5.2f}'.format(net,vat))

print_vat(vatpc=15, gross=9.55)
print_vat()

#print_vat(15,9.55)
