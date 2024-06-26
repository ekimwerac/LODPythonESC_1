import sys

from date import Date

today = Date(13,12,1949)
print (today)

today += 1
print (today)

today += 42
print (today)

cnt = Date.get_count()
print ("Count:",cnt)

today.mday = 6
print (today)

day = today.mday
print (day)

#print (today.__day)
#today.__validate()

print(type(today)) 
print(today.__class__.__name__)
print(today.__class__)

#del today.mday
print('end')
print(today)
today = today + 1
tomorrow = today + 1
print(tomorrow)

today =today
print(today)