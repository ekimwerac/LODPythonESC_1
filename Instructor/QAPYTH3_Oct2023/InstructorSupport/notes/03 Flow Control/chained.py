number = 21
distance = 20

if 0 < number < 42:
    print (number,"is within range")
else:
    print (number,"is out of range")
    
if 0 < number and number < 42:
    print (number,"is within range")
else:
    print (number,"is out of range")

if 0 < number < 42 < distance:
    print (number,"is within range")
else:
    print (number,"is out of range")
    
if 0 < number < 42 and number != 21:
    print (number,"is within range")
else:
    print (number,"is out of range")