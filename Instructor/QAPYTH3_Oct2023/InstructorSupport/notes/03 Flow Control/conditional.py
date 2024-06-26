
i = 42
j = 3

if i > j:
    print ("The i's have it")
else:
    print ("Why oh why")
    
print ("The i's have it") if i > j else print ("Why oh why")

print ("The i's have it" if i > j else "Why oh why")

a = 54
answer = a + 5 if a < 42 else 0
print (answer)

answer = a + (5 if a < 42 else 0)
print (answer)