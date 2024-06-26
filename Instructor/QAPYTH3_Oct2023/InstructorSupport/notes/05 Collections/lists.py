#cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
#print (cheese[1])
#cheese[-1] = 'Red Leicester'
#print (cheese)
#
#cheese += 'Oke'
#b = len(cheese)
#cheese[b-3:b] = []
#cheese += ['Oke', 'Devon Blue']
#print (cheese)

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese[:0] = ['Cheshire', 'Ilchester']
print (cheese)

#cheese += 'Oke'
cheese.append('Oke')

cheese += ['Oke', 'Devon Blue']
cheese.extend(['Oke', 'Devon Blue'])
print (cheese)

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese.insert(2, 'Cornish Brie')
print (cheese)

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese[2:2] = ['Cornish Brie']
print (cheese)

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
saved = cheese.pop()
print ("Saved:",saved,", Result:",cheese)

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
del cheese[-1]
print ("Saved:",saved,", Result:",cheese)

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg', 'Oke', 'Devon Blue']
b = len(cheese)
cheese[b-3:b] = []
print (cheese)

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
saved = cheese.pop(1)
print ("Saved1:",saved,", Result:",cheese)
saved = cheese.pop()
print ("Saved2:",saved,", Result:",cheese)

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg', 'Oke', 'Devon Blue']
del cheese[1:3]
#print (cheese)

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg', 'Oke', 'Devon Blue']
cheese.remove ('Oke')
#print (cheese)

#cheese.remove ('Brie')

