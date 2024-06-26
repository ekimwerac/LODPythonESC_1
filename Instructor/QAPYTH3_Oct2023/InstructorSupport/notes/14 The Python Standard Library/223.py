import sys
import os
import glob
from subprocess import *

if len(sys.argv) > 1:
    dir = sys.argv[1]
else:
    dir = '.'

script = os.path.join(sys.prefix,'Tools','Scripts','2to3.py')
print (script)

procs = []
pattern = os.path.join(dir, '*.py')
for name in glob.iglob(pattern):
    procs.append(Popen([sys.executable, 
                       script, '-w', name]))

while len(procs) > 0:
    proc = procs.pop(0)
    proc.wait()
    