
out = open ('data.txt', 'w')
fh  = open ('brands.txt')

for line in fh:
    fields = line.split(',')
    fields[2] = fields[2].rstrip()
    newline = "{0[0]:.4},{0[1]:.4},{0[2]:.30}".format(fields)
    print(newline, file=out)

fh.close()
out.close()