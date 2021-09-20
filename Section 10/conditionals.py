"""
    In programming, what is a condition?
        We don't always want to execute all of our code all of the time.
    
    If statements check a condition to allow/avoid execution
"""
if False:
    an_integer = int(input('Tell me an integer: '))
    if an_integer != 0:
        print(200 / an_integer)
        input('Tell me something else')
        print(an_integer ** 2 + 3 * an_integer + 2)
        # white space sensitive cares about spaces, tabs, newlines
    
    a_string = input("tell me a string: ")
    if a_string == "Monday" or a_string == "Tuesday" or a_string == "Wednesday" or a_string == "Thursday" or a_string == "Friday":
        print('That is a weekday')
    
    # next week
    if a_string in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        print('Yep.')
    
    if an_integer != 0:
        print(200 / an_integer)
    else:
        print("hey don't divide by zero")
    
    if a_string in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        print('Yep.')
    else:
        print('You didn\'t enter a day of the week')

    day_of_month = int(input('Tell me a day of the month: '))
    
    # 10 = 1(7) + 3 , 1R3 <-- mod cares about the remainder
    # 17 = 2(7) + 3 , 2 R 3
    print(day_of_month % 7)
    
    # day_of_month = day_of_month % 7
    day_of_month %= 7
    
    # var (op)= something
    # var = var (op) something
    """
    a = 2
    a += 3
    # a = a + 3
    a *= 31
    print(a)
    """
    
    if day_of_month % 7 == 0:
        print('The day is Tuesday')
    elif day_of_month % 7 == 1:
        print('The day is Wednesday')
    elif day_of_month % 7 == 2:
        print('The day is Thursday')
    elif day_of_month % 7 == 3:
        print('The day is Friday')
    elif day_of_month % 7 == 4:
        print('The day is Saturday')
    elif day_of_month % 7 == 5:
        print('The day is Sunday')
    elif day_of_month % 7 == 6:
        print('The day is Monday')
    
    my_favorite_integer = int(input('tell me int!!! '))
    
    """
        def of even number - a) divisible by 2
            n = 2k for some k
            18 = 2(9)
            0 = 2(0)
        def of an odd number - not divisible by 2
            n = 2k + 1 for some integer k
            -5 = 2(-3) + 1, k = -3
    """
    
    if my_favorite_integer % 2 == 0:
        print('I am even!')
    else:
        print('I am odd!!')
    
        
    """
        Nesting - putting one block of code into another block of code...
    """
    
    a_jedi = input('Are you a jedi? ')
    if a_jedi == 'yes':
        green_and_small = input('are you green and somewhat small? ')
        if green_and_small == 'yes':
            print('Yoda, you are.')
        else:
            mega_old = input('Are you mega old?')
            if mega_old == 'yes':
                print('You are Obi Wan')
            else:
                print('You are Luke')
    else:
        large_and_furry = input('Are you large and furry?')
        if large_and_furry == 'yes':
            print('I seriously hope you are a wookie, Chewbacca maybe?')
        else:
            shoot_first_ask_later = input('Did you shoot greedo first, be honest...')
            if shoot_first_ask_later == "yeah i did":
                print('Very good, Han, we know you did')
            else:
                alderaan = input('Are you from alderaan?')
                if alderaan == 'yes':
                    print('You are Princess Leia')
                else:
                    print('You are a porg.  ')


year = int(input('What year do you want to check? '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('A mega-leap-year.')
        else:
            print('Not a leap year')
    else:
        print('A leap year.')
else:
    print('Not a leap year')

if year % 400 == 0:
    print('A leap year')
elif year % 100 == 0:
    print('Not a leap year')
elif year % 4 == 0:
    print('A leap year')
else:
    print('Not a leap year')