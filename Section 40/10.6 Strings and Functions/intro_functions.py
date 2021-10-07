"""
             _
    x |---> |f| |---> f(x)
    
    functions / methods
"""

# def = keyword
# name of the function
# in parens - parameter list
# colon - python syntax
# tabbed in

def my_first_function(x):
    if 'a' in x:
        print('Captain, we got a\'s here.')
    else:
        print('Im givin it all shes got.')

my_first_function('aaaaaaaa')

my_first_function('bbbbbbbbuuuuhhhh')

my_first_function('After thinking about it this sting might have a\'s in it.')


def square_me(x):
    # local scope = variables inside of functions
    #   they live only as long as the function call
    #   then they die
    #   only way to get them is to return them
    # the name "the_square" only exists in here
    the_square = x ** 2
    print(x ** 2)
    # butwhen we return the value here, the name is lost
    # the value of that variable lives on
    return the_square

square_me(5)
# square_me(5) is gone, gone forever, gone :(
# we didn't stick it into a variable
square_me(17)
anything = square_me(4)
# we remember square_me(4)
square_me(79843298743243279829898243987432978432798432)
print(anything)

# global scope = anything that lives as long as the program.

