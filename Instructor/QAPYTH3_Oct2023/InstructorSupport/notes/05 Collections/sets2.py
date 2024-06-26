cheese = ['Cheddar', 'Stilton', 'Cornish Yarg', 
          'Oke', 'Stilton', 'Cheshire']
          
cheese = list(set(cheese));   
print (type(cheese), ' ', cheese)

cheese = list(set(cheese) - {'Stilton', 'Oke'});
print (type(cheese), ' ', cheese)
