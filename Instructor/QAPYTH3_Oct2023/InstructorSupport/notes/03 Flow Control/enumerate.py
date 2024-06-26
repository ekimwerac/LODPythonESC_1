
for pos, char in enumerate("Hello world"):
    print (pos, char)

for nr,line in enumerate(open('brian.txt'), start=3) :
    print (nr+1,line, end="")

some_list = [45, 2, 8, 34, 66, 1, 90]
    
for i,num in enumerate(some_list):
    if num > 42:
        some_list[i] = 42
        
print (some_list)

        

