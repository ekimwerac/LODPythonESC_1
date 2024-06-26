import os
import time
import shutil
shutil.copy2('lines.bak.txt', 'lines.txt')

fo = open('lines.txt', 'r')

while True:
    line = fo.readline()
    
    if not line:
        time.sleep(1)
        fo.seek(fo.tell())
    else:
        print (line, end="")

        

        

