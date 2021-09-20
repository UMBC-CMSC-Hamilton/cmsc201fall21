"""
    Leap year example

        if year is divisble by 4 - yes
            unless its divisible by 100 - no
                unless it's also divisible by 400 - yes
                
        2012, 2016, 2020, yes
        1900, 1800, 1700, no
        1600, 2000, 2400, yes
"""
if False:
    year = int(input('Enter the year: '))
    
    if year % 400 == 0:
        print('Yes')
    elif year % 100 == 0:
        print('Nope')
    elif year % 4 == 0:
        print('Yes again')
    else:
        print('no way')
    
    """
        Only the first true one gets evaluated
        unlimited elifs
        1 if, 1 else
    """
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('yes')
            else:
                print('no')
        else:
            print('no')
    else:
        print('nope')
    

a = True
b = False
c = True
d = False
e = False

if ((a and b) or (c and d)) or e:
    print('hi')

if not (a or b):
    # a or b = True or False = True# not True = False
    # Law of Excluded Middle
    print('hello there')

# not is higher precedence to and/or
if not a or b:
    print('what about me?')


if a or not b:
    print('yay')

"""
a = True
b = False
c = True
d = True
e = False
"""
if a or (not b and c):
    print('what about this one? ')

# exclusive or
if (not c and d) or (not d and c):
    print('huh?')

