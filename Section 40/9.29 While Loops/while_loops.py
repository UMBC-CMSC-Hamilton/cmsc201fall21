"""
    What do for loops do?
         - What don't for loops do?
        Iterate over a range, a list of objects/elements.
        execute once for each index/element in our range or list.
        
    Password, you want them to be reprompted if they enter an incorrect password.
"""

"""
    While loops are like if statements that repeat
    
        Remember!!!!
            you must update the variables before you recheck the statement.
            
        Infinite loops are where the condition is always true, potentially not good.
            No escape from an infinite loop.
            
    User input validation - we're checking user input to make sure it's "right"
    
"""
if False:
    password_counter = 0
    max_count = 4
    
    the_password = 'password1'
    # priming the input - get an input before you go into a loop
    user_password = input('What is your password? ')
    
    while the_password != user_password and password_counter < max_count:
        user_password = input('Access Denied, Try again meek and organic human. ')
        password_counter += 1
    
    if password_counter <= max_count:
        print('Access Granted, You may now install viruses on this computer.')
    else:
        print('You have exceeded your allowed attempts and are therefore a meany. Goodbye.')

    
    position = input('Tell me a position on the chess board in the format B7: ')
    
    while len(position) != 2 or not('A' <= position[0] <= 'H') or \
        not('1' <= position[1] <= '8'):
        
        # kinda redoing work? yes it is to some small extent, that's ok
        if len(position) != 2:
            print('Invalid Format: Chess positions have two characters. ')
        elif not('A' <= position[0] <= 'H'):
            print('Invalid Format: The first character must be a letter A-H. ')
        elif not('1' <= position[1] <= '8'):
            print('Invalid Format: The second character must be a number 1-8: ')
        else:
            print(position, 'is a valid position.')
    
        position = input('Tell me a position on the chess board in the format B7: ')
    
    
    total = 0
    
    while total < 25:
        total += int(input('Enter an integer: '))
        print('The current value is', total)

"""
No way to do it with a for loop:

total = 0
for i in range(5):
    total += int(input('Enter an integer: '))
    print('The current value is', total)
    print(i)
    if total >= 25:
        i = 6
"""

"""
    Fun fact:
    
    while loops are more general / powerful / capable than for loops
    
        we can make a while loop that does whatever a for loop does.
        
        but we can't make a for loop that mimics any particular while loop.
"""
if False:
    
    for i in range(3, 29, 4):
        print(i, end=" ")
        
    print()
    
    current = 3
    stop = 29
    step = 4
    
    while current < stop:
        print(current, end=" ")
        current += step
    
    
    a_list = ['sleep', 'food', 'shelter', 'water', 'temperatures between 60 and 80 degrees']
    
    for thing in a_list:
        print(thing)
    
    # let's do this with a while loop
    
    index = 0
    while index < len(a_list):
        print(a_list[index])
        index += 1
        

the_number = float(input('Give me a number and I\'ll take the square root of it: '))
guess = 2
next_guess = 1

while guess != next_guess:
    guess = next_guess
    next_guess = (1/2) * (guess + the_number / guess)
    print(next_guess)
