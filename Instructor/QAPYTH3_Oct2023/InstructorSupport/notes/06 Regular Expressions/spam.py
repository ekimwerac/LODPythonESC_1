import re

menu = 'Sausage SpamSpamSpam Baked beans'
s = re.search (r"(Spam){2,4}", menu)
print (s.string)