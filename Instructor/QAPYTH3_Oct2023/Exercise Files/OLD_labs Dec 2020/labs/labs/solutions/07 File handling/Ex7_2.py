#! /usr/bin/python
import pickle
import gzip

# Using a compressed pickle.
country_dict = {}

for line in open('country.txt', 'r') :
    name, *row = line.split(',')
    country_dict[name] = row

outp = gzip.open('country.p', 'wb')
pickle.dump(country_dict, outp)
outp.close()

# Using a shelve.
import shelve
db = shelve.open('country')
for country in country_dict.keys():
    db[country] = country_dict[country]

db.close()

db = shelve.open('country')
print (db['Belgium'])
db.close()

