import pickle

for line in open('country.txt') :
    row = line.split(',')
    name = row.pop(0)
    country_dict[name] = row

outp = open('country.p', 'wb')
pickle.dump(country_dict, outp)
outp.close()
