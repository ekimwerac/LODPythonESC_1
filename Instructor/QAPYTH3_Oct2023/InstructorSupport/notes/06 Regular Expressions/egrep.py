# grep equivalent

import sys, fileinput, re, operator, glob

def ArgError():
   print ("Usage:", sys.argv[0], "pattern [ file ...]")
   raise 'Argument Error'

if (len(sys.argv) < 3):
   ArgError()

# shift
pattern = sys.argv.pop(1)

if sys.platform == "win32":
   sys.argv[1:] = glob.glob(sys.argv[1])

more_files = len (sys.argv[1:])
if more_files == 0:
   print ("Input file not found")
   ArgError()

# Process all lines in succession
for line in fileinput.input():
   m = re.search (pattern, line)
   if m:
      if more_files > 1:
         print (fileinput.filename(),": ", end='')
      print (line)
