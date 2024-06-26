import os
import sys
import random
import showcard

numbers = list(range(1,52))
random.shuffle(numbers)

while True:
    for number in numbers:
        showcard.display_file("BMP"+str(number)+".gif")
    


