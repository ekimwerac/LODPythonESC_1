import re, sys, os

drink = 'A glass of Miller Genuine Draft'
pattern = r'A (glass|bottle|barrel) of (Bud|Miller|Coors)'
m = re.search(pattern, drink)
if m:
    print("This drink is suitable for Americans")
    print(m.groups())

pattern = r'A (?:glass|bottle|barrel) of (?:Bud|Miller|Coors)'
m = re.search(pattern, drink) 
if m:
    print("This drink is suitable for Americans")
    print(m.groups())

name, old, new = sys.argv[1:];
print(name, old, new)
new_name = name;
new_name = re.sub(r'\.'+old, '.'+new, new_name)
print("Renaming",name,"to",new_name)

os.rename (name, new_name)
os.rename (new_name, name)

print()

txt = 'Stranger in a strange land';
m = re.search(r'range\b',txt)
print(m.start())

txt = 'Stranger in a strange land';
m = re.search(r'range\B',txt)
print(m.start())
print()

port = 'ttyp3'
m = re.search(r'^ttyp\d$',port)

name = 'JoHn'
m = re.search(r'(?i)john',name)
print(m.start())
m = re.search(r'[A-Za-z][A-Za-z][A-Za-z]',name)
m = re.search(r'(?i)[a-z][a-z][a-z]',name)
print()

line = ':fred'
m = re.search(r'[:;,]?\s*\w+', line)
if m: print('A:',m.start())
sound = 'kkkkboinkkkk'
m = re.search(r'boink+', sound)
if m: print('B:',m.start())
m = re.search(r'(boink)+', sound) 
if m: print('C:',m.start())
print()

phone = 'Telephone number: 619-456 1234'
m = re.search(r'\d{3}-\d{2,4}\s?\d{4,8}', phone)
if m: print('tel:',m.start())
print()

txt = '2 456 first 3456 second third 98765 fourth 123'
m = re.search(r'(\d+) ([a-z]+) (\d+)',txt)
if m:
   print(m.groups())
   print([m.start(i) for i in range(1,m.lastindex+1)])
   print([m.end(i)   for i in range(1,m.lastindex+1)])
print()

df = '/dev/sd3d  135398  69683  52176  57%  /home/stuff'
m = re.search('''
        ^(?P<fs>\S+)   \s+ (?:\d+)       \s+ (?:\d+) \s+
         (?P<avail>\d+)\s+ (?P<cap>\d+)% \s+ (?P<mnt>\S+)
              ''', df, re.X)
if m:
    gd = m.groupdict()
    print(gd)
    print("{0[mnt]} ({0[fs]}) has {0[avail]} ({0[cap]}%) free".
          format(gd))
          
print()
