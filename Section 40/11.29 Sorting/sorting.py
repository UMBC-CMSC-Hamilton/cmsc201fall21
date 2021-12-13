"""
Quadratic Sorts:
    Bubble
    Selection
    Insertion
N lg(N) sorts:
    Merge
    Quick
N! sort:
    bogo
"""
import time
import random
import itertools


def make_list(size):
    return [random.randint(0, 10) for _ in range(size)]


def bubble_sort(a_list):
    did_swap = True
    while did_swap:
        did_swap = False
        for i in range(len(a_list) - 1):
            if a_list[i] > a_list[i + 1]:
                did_swap = True
                # how do you swap two things?
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
    
    return a_list


def selection_sort(a_list):
    """
        select the minimum from i to the end and put it in the right spot
        for i in range(len(a_list))
            right spot = i
    """
    for i in range(len(a_list) - 1):
        # min scan, start at i to prevent us from scanning old minima
        min_index = i
        for j in range(i, len(a_list)):
            if a_list[min_index] > a_list[j]:
                min_index = j
        if i != min_index:
            temp = a_list[min_index]
            a_list[min_index] = a_list[i]
            a_list[i] = temp
    
    return a_list


def insertion_sort(a_list):
    """
    pull back sort
    for i in range(n)
        idea: start at index i
            pull the element back until it's in sorted order
        
    [5, 2, 8, 4, 9, 1]
    [5, 2, 8, 4, 9, 1]
    [2, 5, 8, 4, 9, 1]
    [2, 5, 8, 4, 9, 1]
    [2, 4, 5, 8, 9, 1]
    [2, 4, 5, 8, 9, 1]
    [1, 2, 5, 5, 8, 9]
    """
    
    for i in range(len(a_list)):
        j = i
        while j > 0 and a_list[j] < a_list[j - 1]:
            temp = a_list[j]
            a_list[j] = a_list[j - 1]
            a_list[j - 1] = temp
            
            j -= 1
    
    return a_list


def bogo_sort(a_list):
    indices = [i for i in range(len(a_list))]
    p = itertools.permutations(indices)
    for perm in p:
        print(perm)
        found = True
        for i in range(len(a_list) - 1):
            if a_list[perm[i]] > a_list[perm[i + 1]]:
                found = False
        
        if found:
            sorted_list = []
            for x in perm:
                sorted_list.append(a_list[x])
            return sorted_list


def quick_sort(a_list):
    """
    Idea: make three lists, less_list, equal_list, greater_list
    pick a pivot = a_list[0]
    """
    if len(a_list) <= 1:
        return a_list
    
    less_list = []
    equal_list = []
    greater_list = []
    
    pivot = a_list[0]
    
    for x in a_list:
        if x < pivot:
            less_list.append(x)
        elif x > pivot:
            greater_list.append(x)
        else:
            equal_list.append(x)
    
    # print(less_list, equal_list, greater_list)
    less_list = quick_sort(less_list)
    greater_list = quick_sort(greater_list)
    
    return less_list + equal_list + greater_list


def merge(a_list, b_list):
    """
    maintain two different indices and then advance them as we take elements
    """
    
    a_index = 0
    b_index = 0
    new_list = []
    # increment until one of the indices hits the end of its list
    while a_index < len(a_list) and b_index < len(b_list):
        if a_list[a_index] <= b_list[b_index]:
            new_list.append(a_list[a_index])
            a_index += 1
        else:
            new_list.append(b_list[b_index])
            b_index += 1
    
    for x in range(a_index, len(a_list)):
        new_list.append(a_list[x])
    
    for y in range(b_index, len(b_list)):
        new_list.append(b_list[y])
    
    return new_list


def merge_sort(a_list):
    """
        you have a list right?
        divide it in half
            merge_sort(first_half)
            merge_sort(second_half)
        
        [5, 3, 8, 2]
        [5, 3] [8, 2]
        [5] [3] [8] [2]
        Merge([5], [3]) = [3, 5]
        Merge([8], [2]) = [2, 8]
        Merge([3, 5], [2, 8])
        
    """
    
    if len(a_list) <= 1:
        return a_list
    half_list = len(a_list) // 2
    return merge(merge_sort(a_list[0: half_list]), merge_sort(a_list[half_list:]))


def test_sizes():
    for size in [10, 100, 1000, 10000]:
        new_list = make_list(size)
        start_time = time.time()
        bubble_sort(list(new_list))
        print(f'Bubble sort took {time.time() - start_time} to sort {size} elements')
        start_time = time.time()
        selection_sort(list(new_list))
        print(f'Selection sort took {time.time() - start_time} to sort {size} elements')
        start_time = time.time()
        insertion_sort(list(new_list))
        print(f'Insertion sort took {time.time() - start_time} to sort {size} elements')


def time_test_sort(sorting_alg):
    for size in [10, 100, 1000, 10000, 10 ** 5, 10 ** 6, 10 ** 7]:
        new_list = make_list(size)
        start_time = time.time()
        sorting_alg(list(new_list))
        print(f'{sorting_alg.__name__} took {time.time() - start_time} to sort {size} elements')


def verify_sort(sorting_alg):
    for size in [10, 100, 1000]:
        test_list = make_list(size)
        test_sorted = sorting_alg(list(test_list))
        test_list.sort()
        if test_sorted == test_list:
            print('Yep')
        else:
            print('Nope')


# verify_sort(merge_sort)

# print(merge_sort([1, 6, 3, 4, 8, 2]) == [1, 2, 3, 4, 6, 8])

# print(merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])

# test_sizes()
time_test_sort(quick_sort)
time_test_sort(merge_sort)
time_test_sort(sorted)


