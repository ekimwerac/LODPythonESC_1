# py3 version

import glob
import os.path

#import os
#for name in (filter(os.path.isdir,glob.iglob(pattern))):
#    print(name)

#dirs = list(filter(os.path.isdir,glob.iglob(pattern)))    
#print(dirs)

def get_dir(path):
    print('entering get_dir')
    pattern = os.path.join(path,'*')  
    print("Pattern:",pattern)
    for file in glob.iglob(pattern):
        if os.path.isdir(file):
            get=yield file
            #print 'gen',get 
            

for dir in (get_dir('C:/QA/Python')):
    print(dir) 

dirs = list(get_dir('C:/QA/Python'))
print(dirs) 

gen = get_dir('C:/QA/Python')

while True:
    name = next(gen,False)
    if name: print(name) 
    else: break

print next(gen) 
print next(gen) 
print next(gen)  
gen.send('C:/QA')
print(next(gen)) 




