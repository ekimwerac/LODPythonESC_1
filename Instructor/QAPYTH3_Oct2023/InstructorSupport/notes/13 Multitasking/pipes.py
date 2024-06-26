from subprocess import *

proc = Popen('python client.py', stdin=PIPE)

proc.communicate ("hello".encode())


