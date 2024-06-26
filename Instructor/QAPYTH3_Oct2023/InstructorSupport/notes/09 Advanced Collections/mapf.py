import glob
import os

pattern = 'C:/QA/Python/*'

for name in (filter(os.path.isdir,glob.iglob(pattern))):
    print(name)

dirs = list(filter(os.path.isdir,glob.iglob(pattern)))    
print(dirs)