import glob
import os
import sys


def get_dir(path):
    print('entering get_dir')
    pattern = path + '/*'
    
    """
    for file in glob.iglob(pattern):
        if os.path.isdir(file):
            get=yield file
            print('gen',get)
    """
    
    yield from glob.iglob(pattern) 

            
for dir in get_dir('C:/QA/Python'):
    print(dir)




        