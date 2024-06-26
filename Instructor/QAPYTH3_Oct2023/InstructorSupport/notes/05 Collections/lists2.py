#
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print (cheese.count('Stilton'))

#i = cheese.index('Brie')
#print (i,cheese)

#cheese.sort()
#print ("cheese: ",cheese)

cheese.sort(key=len)
print(cheese)

nums = ['1001','34','3','77','42','9','87']
print (sorted(nums, reverse=True))
print (sorted(nums, key=int, reverse=True))
