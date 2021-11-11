"""
    What is recursion?
        When a function calls itself

        Base cases - non-recursive stop the recursion from being infinite
        Recursive Cases - where you call the function

"""


def count_the_as(a_string):
    """
        What should our base case be?
    """
    if not a_string:
        return 0
    print(a_string)
    if a_string[0].lower() == 'a':
        return 1 + count_the_as(a_string[1:len(a_string)])
    else:
        return count_the_as(a_string[1:len(a_string)])


def recursive_palindrome(test_string):
    """
        Base Case:
            length 0 or 1 are palindromes
        Recursive Case:
            if the first equals the last, keep going
        Base Case 2:
            if not, stop and return false
    """
    if len(test_string) in [0, 1]:
        return True
    
    # test_string[-1] == test_string[len(test_string) - 1]
    if test_string[0] == test_string[-1]:
        return recursive_palindrome(test_string[1: -1])
    else:
        return False

"""
    Passing by value - makes a copy of the data in the variable
        prevents the function from making any changes to the variable's value
        in python: immutable
    Passing by reference - does not make a copy
        it has a local name but it refers to the global variable itself
        can change that
        in python: mutable
"""


def better_way_palindrome(test_string):
    for i in range(len(test_string) // 2):
        if test_string[i] != test_string[len(test_string) - 1 - i]:
            return False
    
    return True


s = input()
while s != 'quit':
    print(recursive_palindrome(s))
    s = input()


def add_one(x):
    """
        Because x is an int, it passes by value so doesn't get modified
    :param x:
    :return:
    """
    x = x + 1
    return x


def add_something_to_list(my_list):
    """
        Lists are passed by reference, dictionaries, classes
    """
    my_list.append('something')


x = 5
print(add_one(x))
print(x)

the_big_list = ['hi', 'bye', 'turnip', 'sandwich', 'marshmallow']
# lists are mutable, therefore they will change in the function
add_something_to_list(the_big_list)
print(the_big_list)
