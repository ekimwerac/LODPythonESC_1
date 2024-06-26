import sys

num = 42
pi  = 3.142
num = 42/pi
print (num)
num = 42//pi
print (num)

count = 2000
#print ("Unused port: "  +  count)

print ("Unused port: " + str(count))

print (sys.getsizeof(count))
print (sys.getsizeof(str(count)))



