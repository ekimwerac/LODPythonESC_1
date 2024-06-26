import sys
import os
import glob
from subprocess import *
import time


proc = Popen([sys.executable, 'client.py']) 
    
while not proc.poll():
    time.sleep(0.1)
    print(("In loop:",proc.returncode))
    if proc.returncode != None:
        break

print ("All done")