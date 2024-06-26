import re, sys, os

drink = 'A glass of Coors'
if re.search (r'Bud|Miller|Coors', drink):
    print ("It's a beer!") 

pattern = r'A (glass|bottle|barrel) of (Bud|Miller|Coors)'
if re.search (pattern, drink): 
    print ("This drink is suitable for Americans")

#name, old, new = sys.argv[1:];
#print (name, old, new)
#new_name = name;
#new_name = re.sub(r'\.'+old, '.'+new, new_name)
#print ("Renaming",name,"to",new_name)

#os.rename (name, new_name)
#os.rename (new_name, name)


txt = 'Stranger in a strange land';
m = re.search(r'range\b',txt)
print (m.start())
#
txt = 'Stranger in a strange land';
m = re.search(r'range\B',txt)
print (m.start())

port = 'ttyp3'
m = re.search(r'^ttyp\d$',port)

name = 'JoHn'
m = re.search(r'(?i)john',name)
print (m.start())
m = re.search(r'[A-Za-z][A-Za-z][A-Za-z]',name)
m = re.search(r'(?i)[a-z][a-z][a-z]',name)

line = ':fred'
m = re.search(r'[:;,]?\s*\w+', line)
if m: print ('A:',m.start())
sound = 'kkkkboinkkkk'
m = re.search(r'boink+', sound)
if m: print ('B:',m.start()) 
m = re.search(r'(boink)+', sound) 
if m: print ('C:',m.start()) 

phone = 'Telephone number: 619-456 1234'
m = re.search(r'\d{3}-\d{2,4}\s?\d{4,8}', phone)
if m: print ('tel:',m.start()) 