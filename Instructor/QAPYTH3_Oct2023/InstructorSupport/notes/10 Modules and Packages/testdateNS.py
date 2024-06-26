import sys

sys.path.append('./NamespacePackages1')
sys.path.append('./NamespacePackages2')
from MyNamespace.date import Date

print(dir(Date))
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

from MyNamespace.person import Person

me = Person ("Clive Darke", 'm')
print (me)