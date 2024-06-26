from subprocess import *
import os

#status = call (['dir.exe', '*.py'])
#status = call (['python','hello.py'])

proc = Popen('hello.py', shell=True) 
proc.wait()
print ("Child exited with",proc.returncode)

proc = Popen('tasklist') 
proc.wait()
print ("Child exited with",proc.returncode)

print ("All done")
