import re

str='/dev/sd3d 135398 69683 52176 57% /home/stuff';
nums = re.findall(r'\b\d+\b', str)
print(nums)

for num in re.finditer(r'\b(\d+)\b', str):
    print(num.groups())
