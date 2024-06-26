import re, sys, os

line='The Zen of Perl'
lang = re.subn(r'Perl', r'Python', line)
if lang[1]:
    print (lang[0])


reobj = re.compile (r"(I).*(\1)")
for line in file:
    m = reobj.match (line)
    if m:
        print (m.string[m.start():m.end()])
