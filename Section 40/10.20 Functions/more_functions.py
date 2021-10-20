"""
    
    mutability
    
        int, float, bool, string - immutable
        lists, [future: dicts, classes, etc] - mutable
"""

"""
    ints get passed 'by value' - all immutable things
        analogous to for each loops
    a copy of them is made when they get passed into the function
"""


def change_an_int(x):
    x += 17
    print(x)
    return x


def change_a_string(my_string):
    my_string += ' and also this'
    print(my_string)
    return my_string


"""
    lists, [dicts, classes]
    pass by "reference"
    instead of making a copy, the variable in the function is basically a
        temporary "renaming" / alias
"""


def change_my_list(the_list):
    the_list.append('and now this')
    the_list.append('and now for something completely different')
    print(the_list)


def test_changes():
    my_int = 5
    change_an_int(my_int)
    print(my_int)
    
    the_str = 'i don\'t know, something cool'
    change_a_string(the_str)
    print(the_str)
    
    a_list = ['a', 'b', 'c']
    print(a_list)
    change_my_list(a_list)
    print(a_list)


"""
    Philosophy of functions:
        should have one purpose
        shouldn't print stuff unless you need them to
            return anything you need back to the "user" - programmer who calls the functions
"""


def count_the_as(a_string):
    count = 0
    for c in a_string:
        if c.upper() == 'A':
            count += 1
    return count


def count_as_list(a_list_of_strings):
    list_count = 0
    for the_string in a_list_of_strings:
        list_count += count_the_as(the_string)
    
    return list_count


my_list = []
s = input('Enter string: ')
while s != 'quit':
    my_list.append(s)
    s = input('Enter string: ')

print(count_as_list(my_list))

import random


def display_grid(the_grid):
    for row in range(len(the_grid)):
        for col in range(len(the_grid[row])):
            print(the_grid[row][col], end='\t')
        print()


def can_move(a_grid, new_x, new_y):
    if a_grid[new_x][new_y] != '*':
        return True
    
    return False


the_grid = [[random.choice([' ', '*']) for _ in range(10)] for _ in range(10)]
display_grid(the_grid)

two_ints = input('Enter x y')
x = int(two_ints.split()[0])
y = int(two_ints.split()[1])
while x != -1:
    print(can_move(the_grid, x, y))
    two_ints = input('Enter x y')
    x = int(two_ints.split()[0])
    y = int(two_ints.split()[1])
    