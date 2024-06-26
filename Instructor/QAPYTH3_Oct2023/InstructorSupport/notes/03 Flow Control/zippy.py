import sys

farms     = ['Home Farm', 'Muckworthy', 
             'Scales End', 'Brown Rig']
squirrels = [42, 12, 2, 0]
rabbits   = [395, 68, 57, 32]
moles     = [12, 8, 0, 29]

for (f, s, r, m) in \
    zip(farms, squirrels, rabbits, moles):
    print ('Total for',f,':',s+r+m)
    
keys = ['Australia','Eire','France','Finland',
        'UK','US']
vals = ['Canberra','Dublin','Paris','Helsinki', 
        'London','Washington']
mydict = dict(zip(keys,vals))
print (mydict)


zlist = list(zip(keys,vals))
print ('zlist:',zlist)

mlist = list(keys+vals)
print ('mlist:',mlist)

