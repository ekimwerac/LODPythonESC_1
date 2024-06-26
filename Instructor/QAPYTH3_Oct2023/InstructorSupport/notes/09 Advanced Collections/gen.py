#py3
import glob
import os
import sys

#for name in (filter(os.path.isdir,glob.iglob(pattern))):
#    print(name)

#dirs = list(filter(os.path.isdir,glob.iglob(pattern)))    
#print(dirs)

def get_dir(path):
    print('entering get_dir')
    pattern = os.path.join(path,'*')  
    for file in glob.iglob(pattern):
        if os.path.isdir(file):
            get=yield file
            #print('gen',get)
            

for dir in get_dir('C:/QA/Python'):
    print(dir)

sys.exit()

dirs = list(get_dir('C:/QA/Python'))
print(dirs)

gen = get_dir('C:/QA/Python')
print(next(gen))
print(next(gen))
print(next(gen))
gen.send('C:/QA')
print(next(gen))



        