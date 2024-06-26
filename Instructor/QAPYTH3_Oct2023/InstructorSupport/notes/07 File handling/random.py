fh = open('country.txt', 'rb')

index={}
while True:
    line = fh.readline()
    if not line: break
    fields = line.decode().split(',')
    index[fields[0]] = fh.tell() - len(line) 
    
import pprint
pprint.pprint(index)

key = input('Enter a country:')  
fh.seek(index[key])
print(fh.readline().decode(), end="")
