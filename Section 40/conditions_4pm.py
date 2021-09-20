if False:
    print(5 / 3)
    print(5 // 3)
    print(24 // 5)
    print(17 // 6)
    print(-5 // 7)
    print(-12 // 7)
    
    """
        Let's talk about mod
    
        Short for "modulus"
    
        denoted by the %
    """
    
    print(5 % 3)
    print(271 % 5)
    print(-17 % 5)
    print(63 % 9)
    print(4 % 2, 2 % 4)
    
    an_integer = int(input('Tell me an integer: '))
    
    # conditional control flow
    if an_integer != 0:
        print(1729 // an_integer)
        print('hello there')
        print('something else')
        print('more stuff')
    
    # sequential control flow
    print('not in the if statement')
    
    
    if an_integer % 2:
        print(' our integer is ... odd!!!!')
        
    if an_integer % 2 == 0:
        print('our integer is even!?!?!?')
        
    
    # guarantees that if the first statement is TRUE, it WONT execute
    # guarantees that if the first statement(s) are false, it WILL execute.
    if an_integer % 2:
        print(' our integer is ... odd!!!!')
    else:
        print('our integer is even! (not odd)')
        
    day_of_month = int(input('What day of the month is it? '))
    """
        Calculate the day of the week
        a) Wednesday = 1
        b) day +/- 7 = same day
            b.1) day % 7 is that always the same?
    
        else if = english version
        elif = python version
    """
    
    if day_of_month % 7 == 1:
        print('This is Wednesday')
    elif day_of_month % 7 == 2:
        print('This is Thursday')
    elif day_of_month % 7 == 3:
        print('This is Friday')
    elif day_of_month % 7 == 4:
        print('This is Saturday')
    elif day_of_month % 7 == 5:
        print('This is Sunday')
    elif day_of_month % 7 == 6:
        print('This is Monday')
    elif day_of_month % 7 == 0:
        print('This is Tuesday')
    else:
        print('huh?')
    
    your_name = input('Tell me your name: ')
    if '^' in your_name:
        print('still no don\'t do that')
    elif '$' in your_name:
        print('We dont allow that character.')
    elif '@' in your_name:
        print('not that one either')
    else:
        print('all good')
        
        
    """
        Nesting if statements
            if you stick an if statement into an if-statement
    """

    # original series
    
    human = input('Are you human?')
    if human == 'yes':
        are_you_giving_it_all_shes_got_captain = input('Are you giving it all she\'s got?')
        if are_you_giving_it_all_shes_got_captain == 'yes':
            print('You are Montgomery Scott')
        else:
            drinking_how_is_that = input('do you like to drink a lot? ')
            if drinking_how_is_that == 'yes':
                print('You are Dr. McCoy')
            else:
                sword_fighting = input('Do you like swords or something...?')
                if sword_fighting == 'yes':
                    print('You are Sulu')
                else:
                    print('Kirk out!')
    else:
        vulcan = input('Are you vulcan? ')
        if vulcan == 'yes':
            print('You are Spock. ')
        else:
            print('You are Uhura')

"""
    Leap Years
    
        If year div by 4, leap year....
            except if it's divisible by 100 ... not
                except if it's divisible by 400 ... is again...
"""

year = int(input('Tell me the year:  '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            # 1600, 2000, 2400
            print('This is the big leap year')
        else:
            # 1900, 1800, 1700
            print('This is a 100-not-leap-year')
    else:
        # 2004, 2008, 2012, 2016, 2020
        print('This is a leap year')
else:
    print('Not a leap year')


if year % 400 == 0:
    print('Big leap year')
elif year % 100 == 0:
    print('Not leap year, 100 year exception')
elif year % 4 == 0:
    print('yep leap year')
else:
    print('not leap year')