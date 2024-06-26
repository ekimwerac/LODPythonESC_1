mydict1 = {'Australia':'Canberra', 'Eire'   : 'Dublin',
          'France'   :'Paris',    'Finland':'Helsinki', 
          'UK'       :'London',   'US'     :'Washington'}
print (mydict1['UK'])

mydict2 = dict(Australia='Canberra', Eire='Dublin',
          France='Paris', Finland='Helsinki', 
          UK='London',US='Washington')
print (mydict2['UK'])


nebula = {'M42':'Orion',
          'C33':'Veil',
          'M8' :'Lagoon',
          'M17':'Swan'}

for kv in nebula.items():
    print (kv)

lkeys = list(nebula.keys())
print (lkeys)

jelly = nebula.keys() | {'M37', 'M5'}
print (jelly)

input ("Press <RETURN> to continue")