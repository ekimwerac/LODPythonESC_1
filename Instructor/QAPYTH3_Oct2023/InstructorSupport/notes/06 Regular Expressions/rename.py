import re
import os
import sys

sys.argv[1:] = ['one.txt', 'txt', 'dat']

name, old, new = sys.argv[1:]

#new_name = re.sub(r'\.%s$' % old, '.' + new, name)
#print("Renaming %s to %s" % (name, new_name))

new_name = re.sub(r'\.{:}$'.format(old), '.' + new, name)
print("Renaming {:} to {:}".format(name, new_name))

#os.rename(name, new_name)
