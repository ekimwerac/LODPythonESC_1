
def getnum(end=10):

    i = 1
    while i < end+1:
        val = yield i
        if val:
            i   = val[0]
            end = val[1]
        else:
            i += 1
            

gen = getnum()

num = next(gen)
print(num)

num = next(gen)
print(num)

num = gen.send((20,25))
print(num)

for num in gen:
    print(num)
