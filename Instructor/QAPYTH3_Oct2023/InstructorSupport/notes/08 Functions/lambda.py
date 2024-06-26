
compare = lambda a,b: -1 if a < b else (+1 if a > b else 0)

x = 42
y = 3

print ("a>b",compare(x,y))
print ("a<b",compare(y,x))
print ("a=b",compare(x,x))