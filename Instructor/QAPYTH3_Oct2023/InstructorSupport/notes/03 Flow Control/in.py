lang = ['Perl', 'Python', 'PHP', 'Ruby']

if 'Python' in lang:
    print "Python is in lang"
    
    
slang = "We luv Python";
if 'Python' in slang:
    print "Python is in slang"

dlang = {'Perl':'sigils',    'Python':'indentation', 
         'PHP' :'functions', 'Ruby'  :'Rails'}
if 'Python' in dlang:
    print "Python is there: " + dlang['Python']
