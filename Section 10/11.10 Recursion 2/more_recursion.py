"""
    What is recursion?
        Whenever a function calls itself.
        
        
        
    Recursive definition:
        a_n = a_{n - 2} + a_{n - 7}

"""


def count_the_a(a_string):
    """
    
    :param a_string: some string with a's or not
    :return: the total number of a's in the string
    """
    if not a_string:
        # base case
        return 0
    
    # now a_string probably has something in it
    if a_string[0].lower() == 'a':
        return 1 + count_the_a(a_string[1:len(a_string)])
    else:
        return count_the_a(a_string[1:len(a_string)])


def right_answer_count_as(a_string):
    count = 0
    for c in a_string:
        if c.lower() == 'a':
            count += 1
    return count


def recursive_palindrome(the_string):
    if len(the_string) < 2:
        # length = 0 and length = 1 are ok
        return True
    
    if the_string[0] == the_string[len(the_string) - 1]:
        # the only recursive case
        return recursive_palindrome(the_string[1: -1])
    else:
        # second base case
        return False


def is_palindrome(a_string):
    """
    Helper to fix the "edge cases for length 1, 0"
    
    """
    if len(a_string) < 2:
        return False
    else:
        return recursive_palindrome(a_string)


def input_helper():
    s = input()
    while s != 'quit':
        print(is_palindrome(s))
        s = input()

