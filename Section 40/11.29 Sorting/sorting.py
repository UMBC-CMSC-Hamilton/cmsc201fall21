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


print(bogo_sort([4, 3, 2, 5, 8, 4, 3, 5, 1, 3]))
