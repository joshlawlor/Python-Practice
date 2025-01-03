import random

def is_leap(year):
    leap = False
    
    # Write your logic here
    #IF year is divisible by 4 AND cannot be divided by 100 = leap year true
     #ELSE IF year is also evenly divisible by 400 = leap year true
    #ELSE = leap year false
    
    
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False
   
    return leap

year = random.randint(1900, 25000)
random.randint(1900, 25000)