import shelve

caps = {'Australia':'Canberra', 'Eire'   : 'Dublin',
        'France'   :'Paris',    'Finland':'Helsinki', 
        'UK'       :'London',   'US'     :'Washington'}

db = shelve.open('capitals')
db['UK'] = 'London'
db.close()


db = shelve.open('capitals')
print (db['UK'])
db.close()
