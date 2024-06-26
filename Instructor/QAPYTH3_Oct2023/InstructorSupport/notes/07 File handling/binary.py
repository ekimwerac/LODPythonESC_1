lines = open('brian.txt', 'rb').read()

llines= open('brian.txt', 'rb').read()
llines.decode().split('\n')

linelist = open('brian.txt', 'rb').readlines()

for line1 in open('lines.txt', 'rb').readlines():
    print (line1.decode(), end="")
    
print ()

for line2 in open('lines.txt', 'rb') :
    print (line2.decode(), end="")

print("\n\nWriting...")

fo = open('out.dat','wb')
fo.write(b'Single bytes string')
s = "Native string as a line\r\n"
fo.write(s.encode())
fo.close()

for line in open('out.dat','rb'):
    print(line)
        

