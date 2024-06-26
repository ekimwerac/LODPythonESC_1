import re, sys, os

drink = 'A bottle of Miller'

pattern = \
    'A (glass|bottle|barrel) of (Bud|Miller|Coors)'
m = re.search (pattern, drink)
if m: print m.groups()

pattern = \
    'A (?:glass|bottle|barrel) of (?:Bud|Miller|Coors)'
m = re.search (pattern, drink)
if m: print m.groups()

print

#      0123456789012345678901234567890123456789012345
txt = '2 456 first 3456 second third 98765 fourth 123'
m = re.search(r'(\d+) ([a-z]+) (\d+)',txt)
if m:
   print m.groups()
   print [ m.start(i) for i in xrange(1,m.lastindex+1)]
   print [ m.end(i)   for i in xrange(1,m.lastindex+1)]

print

df = '/dev/sd3d  135398  69683  52176  57%  /home/stuff'
m = re.search('''
              ^(?P<fs>\S+)   \s+ (?:\d+)       \s+ (?:\d+) \s+
               (?P<avail>\d+)\s+ (?P<cap>\d+)% \s+ (?P<mnt>\S+)
              ''',df,re.X)

if m:
    gd = m.groupdict()
    print gd
    print "%s (%s) has %s (%s%%) free" % \
          (gd['mnt'],gd['fs'],gd['avail'],gd['cap'])
          
print 

passwd = 'user1:x:501:501:QA User:/home/users:/bin/ksh'

new_pw = re.sub('.*?:','eric:',passwd,1)
print new_pw
new_pw = re.sub('.*:','eric:',passwd,1)
print new_pw

print
line = 'Perl for Perl Programmers'
txt = re.subn('Perl', 'Python', line)
if txt[1]:
    print txt[0]

txt = re.subn('Perl', 'Python', line, 1)
if txt[1]:
    print txt[0]

print


all = open('names.txt').read()

m = re.search(r'(^dpm|^james)',all,re.I)
if m:
    print "File starts with",m.groups()

m = re.search(r'(^dpm|^james)',all,re.I|re.M)
if m:
    print "A line in the file starts with",m.groups()

print

txt = '123 999'
m = re.search(
    '''
      \d{3}      # 3 digits
      \s         # space
      \d{3,5}    # 3-5 digits
    ''',
    txt,re.X)
if m:
    print 'found'

m = re.search(
    r'\d{3}(?# 3 digits)\s(?# space)\d{3,5}(?# 3-5 digits)',
    txt)
if m:
    print 'found'
    
print

var = '<h1>This is a header</h1>'

m = re.search(r'<([hH]\d)>.*</\1>',var)
print "Matched: ",m.group();

m = re.search(r'(?<=<([hH]\d)>).*(?=</\1>)',var)
print "Matched: ",m.group();

print
   
for line in open('log.txt'):
   nline = re.sub(
     '(?:(?<=\.log,)(\d+)(?=,root,))|(?:(?<=\.dat,)(\d+)(?=.*,system$))',
     lambda m: str(int(m.group(1))-1) if m.group(1) \
               else str(int(m.group(2))-1),
     line,re.X)                           
    
   print nline,


