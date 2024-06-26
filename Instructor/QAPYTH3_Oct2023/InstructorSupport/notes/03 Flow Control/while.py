import sys
line = ""

while line != 'done':
   line = input('Type "done" to complete: ')
   
   # 3.2 fix http://bugs.python.org/issue11272)
   if sys.platform == 'win32':
       line = line.rstrip()
   
   print('<',line,'>')
