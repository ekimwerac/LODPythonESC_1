import glob
import os

pattern = 'C:/QA/Python/*'
sizes = [os.path.getsize(name)
         for name in glob.iglob(pattern)]

print(sizes)

dirs1=[]
for name in (glob.iglob(pattern)):
    if os.path.isdir(name):
        dirs1 += [name]
print(dirs1)

dirs2 = [name for name in glob.iglob(pattern) 
        if os.path.isdir(name)]

print(dirs2)