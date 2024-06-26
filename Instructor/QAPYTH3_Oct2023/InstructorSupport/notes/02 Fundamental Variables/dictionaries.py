mydict = {'Australia':'Canberra', 'Eire'   : 'Dublin',
          'France'   :'Paris',    'Finland':'Helsinki', 
          'UK'       :'London',   'US'     :'Washington'}
print (mydict['UK'])
country = 'Iceland'
mydict[country] = 'Reykjavik'

mydict=dict(Sweden = 'Stockholm',  Norway = 'Oslo')
for country in mydict.keys():
    print (country, ': ', mydict[country])



mydict = {'UK':['London','Wigan','Macclesfield','Bolton'], 
        'US':['Miami','Springfield','New York','Boston']}
print (mydict['UK'][2])

homer = 1
print (mydict['US'][homer])

mydict['FR'] = ['Paris', 'Lyon', 'Bordeaux', 'Toulouse']
for country in mydict.keys():
    print (country, ': ', mydict[country])

