from subprocess import *
import os

#(output, error) = Popen('tasklist', 
#                         stdout=PIPE, stderr=PIPE).communicate()

proc = Popen('tasklist', stdout=PIPE, stderr=PIPE)
(output, error) = proc.communicate()


if error != None:
    print ("error:", error.decode())
    
print ("output:", output.decode())

print ("All done")
