"""
    if statements:
    
    You can have as many elifs as you want to
    You can have an else or not.
    
    
    
"""
if False:
    condition = True
    other_condition = False
    if condition and other_condition:
        print('the condition was true')
    else:
        print('the condition was false')
    
    x = int(input('Tell me a number'))
    if x == 1:
        print('x was 1')
    elif x == 2:
        print('x was 2')
    elif x == 3:
        print('x was 3')
    elif x == 4:
        print('x was 4')
    elif x == 5:
        print('x was 5')
    elif x == 2:
        print('robot revolution')
    else:
        print('x was not between 1 and 5 inclusively')

    a = False
    b = False
    c = True

    if (a and b) or c:
        print('it is on')
    else:
        print('it is off')
    
    if a and (b or c):
        print('yes')
    else:
        print('no')


a = True
b = False
c = False
d = True
e = False

# a = b = False
# a = True, b = False
# a = False, b = True
if not((a and b) or (not d or e) or c):
    print('something happened')
else:
    print('nothing happened')

# not (a or b) = not a and not b
# not (a and b) = not a or not b
if not (a or b):
    print('demorgan!')

if not a and not b:
    print('also demorgan!')


a = False
b = False
c = True
d = True
e = True

if (a and not b) or not (c and d and e):
    print('what the heck is this? ')
# a = True as long as b = True
