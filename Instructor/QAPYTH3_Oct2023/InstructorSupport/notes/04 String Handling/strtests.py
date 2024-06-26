
str = 'hello world';

print (str.count('o'));
print (str.count('o', 5));

if str.startswith('hell'):
    print ("It's hell in there")
    
if str.isalpha():
    print ('string is all alpha')
    
str = ' \t\r\n'
if str.isspace():
    print ('string is whitespace')