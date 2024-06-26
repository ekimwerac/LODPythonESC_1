import sys

for arg in sys.argv :
   print ("Command line argument:",arg)
   
else:
   print (len(sys.argv), 'arguments')


some_list = [45, 2, 8, 34, 66, 1, 90]
for i in range(0,len(some_list)):
    print (some_list[i])
    
for num in some_list:
    print(num)

for i in range(0,len(some_list)):
    if some_list[i] > 42: some_list[i] += 1
    
print (some_list)

new_list = list(map(lambda a: a+1,some_list))
print (new_list)


