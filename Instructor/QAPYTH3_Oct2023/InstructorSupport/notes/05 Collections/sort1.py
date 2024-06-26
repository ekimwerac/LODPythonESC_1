
cheese = ['Cornish Yarg','Oke','Edam','Stilton']
cheese.sort(key=len)
print(cheese)

nums = ['1001','34','3','77','42','9','87']
newstr = sorted(nums)
newnum = sorted(nums, key=int)

print('newstr:',newstr)
print('newnum:',newnum)
