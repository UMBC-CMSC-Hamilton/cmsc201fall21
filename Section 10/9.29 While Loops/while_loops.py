"""

    What does it really mean to be a for loop?
    
        Either have a range object, or something to iterate over.
        
        Iterate - to repeat with the idea of a next object/element/index
            When we run out of next things, we stop.

        You have some list, range, some kind of thing like that.
        
    What if you don't know how many times you want to repeat some kind of statement?
    
    while-loops are like if statements, except they repeat while the if
        statement is true
"""
if False:
    # priming the input
    password = input('Tell me your password: ')
    
    # password = ''
    # loop should repeat when the password is NOT equal to the correct answer...
    counter = 0
    while password != 'asdf1234' and counter < allowed_tries:
        password = input('That wasn\'t right, try again.  Tell me your password: ')
        counter += 1
    # if the condition is false they don't run, get skipped
    # if the condition is true then they start running until it's false
    
    print('You got it!')
    
    # i want to repeat this until we get the right password
    
    """
        In chess, A-H 1-8
    
        strings are not lists.
        but... strings are kinda like lists
        
            you can use the index notation to get specific characters!
            
            SHIFT + CTRL + ARROW = multiple select
    """
    position = input('Tell me a position on the Chess board form (B7): ').upper()
    while len(position) != 2 or not('A' <= position[0] <= 'H') or \
            not ('1' <= position[1] <= '8'):
        if len(position) != 2:
            print('The length of a position is always 2, try again please.')
        elif not('A' <= position[0] <= 'H'):
            print('The first letter should be A through H.')
        elif not ('1' <= position[1] <= '8'):
            print('The number should be 1 through 8.')
            
        position = input('Tell me a position on the Chess board form (B7): ').upper()
    
    print('we accept a valid position at', position)
    

    # if you have a game...
    while not game_over():
        play_game()


    total = 0
    while total < 25:
        some_int = int(input('Tell me an integer: '))
        total += some_int
        print(total, 'is the current total.')
    
    print('The total is', total, 'after the loop')
    
    
    x = float(input('What number should we compute the square root of: '))
    allowed_error = float(input('How much error should we allow? '))
    
    next_guess = 1.0
    guess = allowed_error + 5
    
    while abs(guess - next_guess) > allowed_error:
        guess = next_guess
        next_guess = (1 / 2) * (guess + x / guess)
        print(next_guess)
    
"""
    Fact of the universe:
        a) all for loops can be rewritten as while loops
        b) not all while loops can be made into for loops
"""

for i in range(2, 84, 7):
    print(i, end=" ")
    
print()

current = 2
stop = 84
step = 7

# this was as written is an infinite loop
"""
while current < stop:
    print(current, end=' ')

    we needed to add the incrementing for step
"""

while current < stop:
    print(current, end=' ')
    # 20 more lines...
    current += step
