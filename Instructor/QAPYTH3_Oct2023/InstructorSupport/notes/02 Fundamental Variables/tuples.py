mytuple=('eggs', 'bacon','spam','tea')
print (mytuple)
print (mytuple[1])
print (mytuple[-1])


print (mytuple[2 : 4])
print (mytuple[-4])
mylist = mytuple
print (mylist[1:])
print (mylist[:2])

cheese = ['Cheddar', 'Camembert', 'Brie', 'Stilton']
del cheese[1:3]
print (cheese)

mytuple=('Brian', 'Eric');
print (mytuple)
#mytuple[2] = 'John'


a = 'Hairdresser'
b = 'Lumberjack'
(a,b) = (b,a)
print (a)
print (b)

Gouda, Edam, Caithness = range(3)
print (Gouda, Edam, Caithness)

another = mytuple * 4
print (another)
#another[4] = 'here'
