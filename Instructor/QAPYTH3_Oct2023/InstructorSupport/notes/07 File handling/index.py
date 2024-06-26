
fh = open ('data.txt', 'r+')

index={}
while True:
    line = fh.readline()
    if not line: break
    fields = line.split(',')
    index[fields[2].rstrip()] = fh.tell() - len(line) -1

key = input ('Enter a key:')  
fh.seek(index[key])
print (fh.readline())

fh.close()
