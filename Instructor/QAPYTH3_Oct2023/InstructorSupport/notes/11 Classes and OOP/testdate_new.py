import sys
from types import MethodType
from date import Date

class Proxy:
    def __init__(self, obj):
        self._wrapped = obj          # save the object to be wrapped
        

    def __getattr__(self, attr):
        return getattr(self._wrapped, attr)

    def __setattr__(self, attr, value):
        return setattr(self._wrapped, attr, value)
    
    def some_method(self):
        print('proxy some_method')
        pass   


today = Date(13,12,1949)
print(today)

today += 1
print(today)

today += 42
print(today)

cnt = Date.get_count()
print(cnt)

today.mday = 6
print(today)

day = today.mday
print(day)

#print (today.__day)
#today.__validate()

stuff = Proxy(today)
print("stuff:",stuff)
stuff.some_method()

