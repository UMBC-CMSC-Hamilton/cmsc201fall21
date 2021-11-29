"""
Sorting is divided into two categories

Quadratic sorts = run time increases with the square of the input size
    Bubble
    Selection
    Insertion
    
    
N lg(N) sorts
    ln = log_e
    log = log_10
    lg = log_2
    
    Merge
    Quick
"""

import random


def bubble_sort(a_list):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for j in range(len(a_list) - 1):
            if a_list[j] > a_list[j + 1]:
                is_sorted = False
                # swap thing in j , j + 1
                temp = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = temp
        
    return a_list


def selection_sort(a_list):
    """
        We want to do bubble sort but all we care about is tha the last element
         is the biggest, we only do one swap per iteration
    
        Scan a list, find the max, stick it at the end = len(a_list) - 1 .
        scan the list except the last element, stick that at the end - 1 (penultimate)
        scan the list except the last 2 elements, stick that at the end - 2 (penultimate)
    """
    
    for i in range(len(a_list)):
        min_index = i
        for j in range(i, len(a_list)):
            if a_list[j] < a_list[min_index]:
                min_index = j
                
        # swap the thing in min_index with the thing at index i
        if min_index != i:
            temp = a_list[min_index]
            a_list[min_index] = a_list[i]
            a_list[i] = temp
        
    return a_list
    

def insertion_sort(a_list):
    """
        insertion not really what it is doing...
        pull back sort
        for i in range(n):
            pull back element i until it's in sorted order
        [3, 1, 2, 5, 4]
        
        [3, 1, 2, 5, 4]
        [1, 3, 2, 5, 4]
        [1, 2, 3, 5, 4]
        [1, 2, 3, 5, 4]
        [1, 2, 3, 4, 5]
    """
    for i in range(1, len(a_list)):
        j = i - 1
        while j >= 0 and a_list[j] > a_list[j + 1]:
            temp = a_list[j]
            a_list[j] = a_list[j + 1]
            a_list[j + 1] = temp
            j -= 1
        
    return a_list



def quick_sort(a_list):
    """
        pick a "pivot" a_list[0] by default
        
        3 lists less_list, equal_list, greater_list
    """
    if len(a_list) <= 1:
        return a_list
    
    less_list = []
    greater_list = []
    equal_list = []
    
    for x in a_list:
        if x < a_list[0]:
            less_list.append(x)
        elif x > a_list[0]:
            greater_list.append(x)
        else:
            equal_list.append(x)
    
    less_list = quick_sort(less_list)
    greater_list = quick_sort(greater_list)

    return less_list + equal_list + greater_list


def make_list(size):
    return [random.randint(0, 10) for _ in range(size)]
# random_list = [''.join(random.choices(['a', 'b', 'c'], k=3)) for _ in range(10)]


import time

def run_quadratic_tests():
    for size in [10, 100, 1000, 10000]:
        random_list = make_list(size)
        
        start_time = time.time()
        bubble_sort(list(random_list))
        print(f'Bubble sort on {size} took {time.time() - start_time}')
        start_time = time.time()
        selection_sort(list(random_list))
        print(f'Selection sort on {size} took {time.time() - start_time}')
        start_time = time.time()
        insertion_sort(list(random_list))
        print(f'Insertion sort on {size} took {time.time() - start_time}')
    

for size in [10, 100, 1000, 10000]:
    my_list = make_list(size)
    print(my_list)
    result = quick_sort(list(my_list))

    print(result)
    my_list.sort()
    if result == my_list:
        print('Yay')
    else:
        print('boo')

