"""
    Complexity Theory/Algorithmic Complexity measures the number of "steps"
        that an algorithm takes.
        
    Generally we use big-O to measure the differences between algorithms.
    
    f(n) is O(g(n)) when there are constants C > 0 n_0 so that:
        f(n) <= C g(n) whenever n >= n_0
        
    Ex.
        Pick a C = 8 and you pick an n_0 = 1
    
        3n^2 + 5n - 2 is O(n^2)
        3n^2 + 5n - 2 <= 8n^2
        n > 1 = n_0
    
    Ex:
        3n^4 is O(n^7)
        
        3n^4 <= C * n^7
        3 <= C * n^3
        
        3/C <= n^3 take the cube root and get n_0 that you need.
        
        C = 1, this should work.
        
        3 <= n^3
        pick n = 1, this is false, but that's ok
             n = 2, now it's true
        3 <= 1^3 (nope)
        3 <= 2^3 = 8 (yep)
        n_0 = 2
    Ex:
        n^5 is not big O(n^2)
        
        n^5 <= C * n^2 do the cancellation
        n^3 <= C
        Look at this for a second, and think...
        This inequality is going to be false for most values, so...
        n^5 is not O(n^2)
        
    Ex:
        17 is O(1) - doesn't depend on input size.
        
        Why?
        
        17 <= C * 1
        
        Pick C = 17 or above, n_0 = anything really.
        
"""


def find_max(a_list):
    """
        if statement is 1 step
        
        assignment is 1 step
        n = size of the list
        
        n steps to go through the list...
        3n steps to go through the list...
            We don't care who is right,
            all we know is that it takes O(n) time.
            
            I don't want to really be specific about what a "step" is.
        1 more step to return
    """
    
    if not a_list:
        return None
    
    current_max = a_list[0]
    for x in a_list:
        if current_max < x:
            current_max = x
    
    return current_max


def do_something(a_list):
    """
        I dunno what it does, but it is O(n^2)
    """
    calc = 0
    # n * O(n) = O(n^2)
    for x in a_list:
        # O(n) time to run this inner loop
        for y in a_list:
            # O(1) - constant time
            calc += (x - y) ** 2
    
    return calc


def logger(n):
    """
        current = 2 * 2 * 2 * 2 * ... * 2 (step times)
                = 2^step > n
        n <= 2^step
        lg(n) ~= step
        ceil(lg(n))
        This algorithm runs in O(lg(n)) time :)
    """
    current = 1
    step = 0
    while current < n:
        current *= 2
        step += 1
    return step


def as_and_bs(length, current):
    """
        O(2^n) time, but why?
        
        every time you get to a recursive call, and the length > 0
            branch twice
            
    """
    if not length:
        print(current)
    else:
        as_and_bs(length - 1, current + 'a')
        as_and_bs(length - 1, current + 'b')


def linear_search(a_list, search_for):
    """
        O(n) algorithm, fine, but not the best if the list is sorted.
    """
    for x in a_list:
        if x == search_for:
            return True
    return False


def binary_search(a_list, search_for):
    """
        [1, 2, 5, 7, 16]
        s_f = 7
        look at the middle element
        [1, 2, 5, 7, 16], m = 5
        if middle < search_for, then the element has to be above it in the list
        if middle > search_for then the element has to be below it in the list
        if middle == search_for return true
        [7, 16], m = 16
        [7] m = 7 search_for = 7, got it return true
        what if the element was 6 instead [1, 2, 5, 6, 16]?
        oh then we wouldn't have found it.  return False
        
        [not down here middle yes - up here]
    
        n / 2^step ~ 1 or 0 something in there
        n ~ 2^step
        lg(n) ~= step
    """
    print(a_list)
    if not a_list:
        return False
    middle_index = len(a_list) // 2
    if a_list[middle_index] < search_for:
        return binary_search(a_list[middle_index + 1:], search_for)
    elif a_list[middle_index] > search_for:
        return binary_search(a_list[0:middle_index], search_for)
    else:
        # has to be equal... trichotomy
        return True


import random

my_list = [random.randint(0, 10000) for _ in range(800)]
my_list.sort()
binary_search(my_list, 25)
