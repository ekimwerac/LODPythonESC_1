#======================================================================
#
#  Filename:     stest1.cpp
#  Description:  Simple test harness to exercise the stack class.
#
#======================================================================

import sys
from stack import stack

num = input ("What is the maximum size of the stack? ")

st = stack(num)                       # Create stack of appropriate size
    
option = 0
    
while option != 3:                    # Loop until 'Quit'
    
    option = int(input ("\n1. Push value onto stack\n" \
             "2. Pop  value from stack\n" \
             "3. Quit\n\n" \
             "Which service do you require? "))
 
    if option == 1:
        num = input ("Please enter a value... ")
        st.push(num)
    elif option == 2:
        num = st.pop()
        print ("Value popped from stack ... " + str(num) )  
    elif option == 3:
        break
    else:
        print ("Invalid option", option)