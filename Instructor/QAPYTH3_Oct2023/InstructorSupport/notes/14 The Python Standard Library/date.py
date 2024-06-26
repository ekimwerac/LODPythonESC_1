import sys
from datetime import *
from calendar import *
import time   ##

print (date.today().strftime("%A %d %B %Y"))

sBirth = input("Enter birthday (dd/mm/yyyy):")
try:
    (day, month, year) = sBirth.split('/')
    dBirth = date(int(year), int(month), int(day))
except ValueError:
    print ("Invalid date:",sBirth, file=sys.stderr)
    exit(1)
    
print (day,month,year)
# We should not include today, it is not yet over!
dYesterday = date.fromtimestamp(time.time()- (24 * 60 * 60))

#dToday = date.today()
diff = dYesterday - dBirth

diff = diff.days - leapdays(int(year),dYesterday.year)
years = diff // 365
print ("Client is",years,"years old")


