import re

str = 'hello world';

print len( re.findall (r"(o)",str))
print len( re.findall (r"(o)",str[5:]))

if re.match (r"^hell", str):
    print "It's hell in there"
    
if re.match (r"^[A-Za-z]+$", str):
    print 'string is all alpha'
    
str = ' \t\r\n'
if re.match (r"^\s+$", str):
    print 'string is whitespace'