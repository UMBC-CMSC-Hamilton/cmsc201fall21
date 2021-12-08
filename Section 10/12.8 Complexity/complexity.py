"""
    Algorithmic complexity is a measure of how fast an algorithm runs
        based on the size of the input set.

    Big-O
    
    f(n) is O(g(n)) when:
        There is a constant C > 0 and a constant n_0 so that:
        f(n) <= C * g(n) for n >= n_0.
    
    Ex:
        3n^2 + 5n + 2 is O(n^2)
        3n^2 + 5n + 2 <= 10 n^2
        for n > 0.
        
    Ex:
        n lg(n) is O(n^2)
        n lg(n) < (C = 1)n^2 why is that?
        Divide by n,
        Basic fact:
            lg(n) < n
    
    Ex:
        3n^7 is not O(n^3)
        Why not?
        
        There is some constant C so that:
            3n^7 <= C * n^3
        But here's the problem:
            divide by n^3:
            
            3n^4 <= C
            
        No, it can't be true. What if we didn't pick the right C?
            Does that matter? Eventually a function that grows to infinity
            will cross any C.
            
    Ex: (Any constant function/number is O(1))
        17 is O(1)
        
        Pick C = that number  + 1= 17 in this case + 1
        
        17 <= C?
        yes. C = 18 which is bigger.
"""

a = 3
b = 7

a += b  # this is one operation


# well no, it's actually 4 operations
# retrieve a, retrieve b, add them, store them too


def find_max(a_list):
    """
        the list is length = n
        best case: we only assign x once, half of the number of operations
        worst case: assign x every time [1, 2, 3, 4, 5, 6, 7...]
        average case: we probably find somewhere near n / 2 new maxes.
        
        How many steps does it take to run this?
            best case: n steps for-if not doing assignment
            worst case: 2n steps for-if-assign
        Good news:
            all of that is O(n)
    """
    
    if not a_list:
        return None
    
    current_max = a_list[0]
    for x in a_list:
        if x > current_max:
            current_max = x
    
    return current_max


def variance(a_list):
    """
        var = sum (x - avg)^2
        
        n steps + n steps = 2n steps
        
        2n is O(n)
    """
    if not a_list:
        return 0
    
    the_average = 0
    for x in a_list:
        the_average += x
    the_average /= len(a_list)
    
    the_var = 0
    for x in a_list:
        the_var += (x - the_average) ** 2
    
    return the_var


def covar(a_list):
    if not a_list:
        return 0
    
    nonsense = 0
    # this is going to run n times
    for x in a_list:
        # this is going to run n times
        for y in a_list:
            # who knows, it's O(1)
            nonsense += (x - y) ** 2
    
    # n * n * O(1) = O(n^2)
    
    return nonsense


def logger_of_n(n):
    """
    
        We know that 2^lg(n) == n
        
        1, 2, 4, 8, 16, 32, ... until we get bigger than n
        The number of steps is going to be approx lg(n)
        
        ceil(lg(n))= round-up(lg(n))
        
        O(lg(n))
    """
    
    current = 1
    
    step = 0
    while current < n:
        current *= 2
        step += 1
    
    return step


""" binary search, a lg(n) story

idea:
    if the list is sorted (must be sorted)
    
    ask: what is the middle element?
    
    [1, 2, 3, 3, 7, 8, 10] searching for 8
    if we find a number less than the search value, we go up
    if we find a number greater than the search value, we go down
    if we find the search number, we return True
    
    [1, 2, 3, 3, 7, 8, 10], s = 8, m = 3
    [7, 8, 10], s = 8, m = 8 we found it!, return True
    
    [1, 2, 3, 3, 7, 8, 10], s = 5, m = 3
    [7, 8, 10], s = 5, m = 8 we have to go down
    [7] s = 5, m = 7 nope, return False

"""


def binary_search(a_list, search_val):
    """
    Because it divides the size of the list in half every time...
        #steps == same as previous problem
        n / 2^steps ~= 1 or 0
        n ~= 2^steps
        lg(n) ~= steps
        
        O(lg(n))
        
        Why is this better?
            Original search without sorting takes O(n) time
            
    """
    print(a_list)
    if not a_list:
        return False
    mid_pt = len(a_list) // 2
    if a_list[mid_pt] == search_val:
        return True
    elif a_list[mid_pt] > search_val:
        return binary_search(a_list[0: mid_pt], search_val)
    elif a_list[mid_pt] < search_val:
        return binary_search(a_list[mid_pt: len(a_list)], search_val)


def linear_search(a_list, search_val):
    """
     Because we expect to search n/2 things before we find search_val
     
     We say... you are an O(n) algorithm
     
     So, you're worse than a log algorithm.
    """
    
    for x in a_list:
        if x == search_val:
            return True
    
    return False


import random

my_random_list = [random.randint(0, 100) for _ in range(100)]
my_random_list.sort()

print(binary_search(my_random_list, 25))


def fib(n):
    """
        O(phi^n)
        phi = (1 + sqrt(5)) / 2
        phi = 1.618...
        
        In CS:
        that sounds like O(2^n)
    """
    if n <= 1:
        return 1
    
    return fib(n - 1) + fib(n - 2)


