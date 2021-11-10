# second project is out
# second midterm is next week
# next monday is a review
# next wednesday is the EXAM don't miss that
import sys

"""
    What are functions?
    
        pieces of code (repeatable)
            take input, generally they return output of some kind
"""


def sub_one(x):
    return x - 1


"""
Call stack:

subtract_till_zero(4) ... running
subtract_till_zero(5) ... waiting
"""


def subtract_till_zero(x):
    print(f'Entering x ={x}')
    if x > 0:
        temp = subtract_till_zero(x - 1)
        print(f'Leaving x ={x}')
        return temp
    else:
        print(f'Reached the base case x ={x}')
        return 0


# print(subtract_till_zero(5))

def compute_factorial(n):
    value = 1
    for i in range(1, n + 1):
        value *= i
    return value


def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        temp = n * recursive_factorial(n - 1)
        return temp


def recursive_fibonacci(n):
    """
    Use the mathematical formula as stated:
        if n < 2: just say 1
        
        if n >= 2 then use the general formula:
            Fib(n) = Fib(n - 1) + Fib(n - 2)
    
    :param n:
    :return:
    """
    print(f'Calculating fibonacci of {n}')
    if n < 0:
        raise ValueError('Dont do that!')
    if n < 2:
        return 1
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def forever_recursion(x):
    if x == 0:
        return 1
    print(x)
    return forever_recursion(x)


"""
    What if you get a RecursionError in this class?
    
        Your base case is wrong. (75%)
        Other case -> not subtracting from the recursive case (25%)
"""

"""

    order matters aab != aba
    L = 1
    a, b
    L = 2
    aa, ab, ba, bb
    L = 3
        aaa, aab, aba, abb
        baa, bab, bba, bbb
    L = 4
        aaaa, aaab, aaba, aabb
        abaa, abab, abba, abbb
        baaa, baab, baba, babb
        bbaa, bbab, bbba, bbbb
"""


def make_as_and_bs(length, current):
    """
    If i want to make all the strings of length N of a's and b's
        let's say i know all strings of length N - 1
        'a' + all the length N - 1 strings
        'b' + all the length N - 1 strings
        
        that's how we get all the length N strings.
    
    Remember the base case:
        when you stop the recursion
        if the length == 0, you know the strings of that length
        there is one of them, it's ''
    
    :param length:
    :param current:
    :return:
    """
    if length == 0:
        print(current)
    else:
        make_as_and_bs(length - 1, current + 'a')
        make_as_and_bs(length - 1, current + 'b')


def get_binary(num, length):
    the_answer = ''
    for i in range(length):
        if num % 2 == 0:
            the_answer = 'a' + the_answer
        else:
            the_answer = 'b' + the_answer
        
        num //= 2
    return the_answer


def make_as_and_bs_iteratively(length):
    for i in range(2 ** length):
        print(get_binary(i, length))
        




"""      #
         #
   #### ##
Y  #
   # S
   #
"""

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, etc
# print(recursive_fibonacci(int(input('What number? '))))
# make_as_and_bs(12, '')
make_as_and_bs_iteratively(5)
