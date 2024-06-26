
import sys
import os
from stat import *


flt = 22/7;
#print ("Float format: %11.8f, scientific: %e" % (flt, flt))
print ("Float: {0:11.8f}, sci: {0:e}".format(flt))

first = 'Gengis';
second = 'Khan';
#print ("Name: %-20s %-10s" % (first, second));
print ("Name: {0:<20s} {1:<10s}".format(first, second));

#fred = '%x' % 3735928559
fred = '{0:#x}'.format(3735928559)
print (fred)

file = sys.argv[0] 
perms = '0{0:o}'.format((os.stat(file)[ST_MODE]) & 0o7777);

print (perms)
print()

planets = {'Mercury' : 57.91,
           'Venus'   : 108.2,
           'Earth'   : 149.597870,
           'Mars'    : 227.94}

for i,key in enumerate(planets.keys()):
    print("{:2d} {:<10s} {:06.2f} Gm".
          format(i,key,planets[key]))
print()
for i,key in enumerate(sorted(planets.keys(),key=lambda a:float(planets[key]))):
    print("{:2d} {:<10s} {:06.2f} Gm".
          format(i,key,planets[key]))

# centred          
print()
for i,key in enumerate(sorted(planets.keys(),key=lambda a:float(planets[key]))):
    print("{:2d} {:^10s} {:06.2f} Gm".
          format(i,key,planets[key]))
          
