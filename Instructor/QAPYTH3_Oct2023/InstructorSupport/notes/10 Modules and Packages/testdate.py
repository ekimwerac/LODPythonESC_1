import sys

sys.path.append('./DemoModules')
from date import Date

today = Date(13,12,1949)
print (today)

today += 1
print (today)

today += 42
print (today)


cnt = Date.get_count()
print (cnt)

today.mday = 6
print (today)

day = today.mday
print (day)

#print (today.__day)
#today.__validate()