nebula = {'M42':'Orion',
          'C33':'Veil',
          'M8' :'Lagoon',
          'M17':'Swan'}

for kv in nebula.items():
    print(kv)

jelly = nebula.keys() | {'M37', 'M5'}
print("View:",jelly)

jelly = nebula.keys() | nebula.values()
print("View:",jelly)

jelly = {'M37', 'M5'} | nebula.keys() 
print("View:",jelly)
