import os


#status = os.system('hello.py') 
#print ("Child exited with",status)

for line in os.popen('tasklist').readlines():
    print (":", line, end="")
   


print ("All done")
