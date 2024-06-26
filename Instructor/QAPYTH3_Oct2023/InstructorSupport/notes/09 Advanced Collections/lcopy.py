fruit  = ['Apple', 'Pear', 'Orange']

lunch = fruit
lunch[1] = 'Eggs'
print('fruit:',fruit)
print('lunch:',lunch)
print()

fruit  = ['Apple', 'Pear', 'Orange']

lunch = fruit[:]
lunch[1] = 'Eggs'
print('fruit:',fruit)
print('lunch:',lunch)
print()

cheese = ['Cheddar', 'Stilton', 'Cheshire']

fruit = ['knife','plate',['Apple', 'Pear', 'Orange']]
lunch = fruit[:]
lunch[2][1] = 'Eggs'
print('fruit:',fruit,'\nlunch:',lunch)
print()

import copy
fruit = ['knife','plate',['Apple', 'Pear', 'Orange']]
lunch = copy.deepcopy(fruit)
lunch[2][1] = 'Eggs'
print('fruit:',fruit,'\nlunch:',lunch)
print()

