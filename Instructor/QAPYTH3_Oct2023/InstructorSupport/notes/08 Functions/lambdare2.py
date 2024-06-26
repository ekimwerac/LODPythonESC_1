
import re
codes = {}

names = ['zero','wun','two','tree','fower','fife','six','seven',
         'ait','niner','alpha','bravo','charlie','delta','echo',
         'foxtrot','golf','hotel','india','juliet','kilo','lima',
         'mike','november','oscar','papa','quebec','romeo',
         'sierra','tango','uniform','victor','whisky','xray',
         'yankee','zulu']

for key in (range(0,10)):
    codes[str(key)] = names[key]
    
for key in (range(ord('A'),ord('Z')+1)):
    codes[chr(key)] = names[key - ord('A')+10] 

reg = 'WG09 OKD'

result = re.sub(r'(\w)', 
                lambda m: codes[m.groups()[0]]+' ', reg)

print (result)