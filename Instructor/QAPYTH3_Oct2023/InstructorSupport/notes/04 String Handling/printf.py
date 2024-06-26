
import sys
import os
from stat import *


flt = 22/7;
print ("Float format: %11.8f, scientific: %e" % (flt, flt))

first = 'Gengis';
second = 'Khan';
print ("Name: %-20s %-10s" % (first, second));

fred = '%x' % 3735928559
print (fred)

file = sys.argv[0] 
perms = '0%lo' % ((os.stat(file)[ST_MODE]) & 0o7777);

print (perms)



