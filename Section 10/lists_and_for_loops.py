"""

    What is a list?

        a ordered collection of elements
        
        There is an element 0, element 1, element 2, ...

    Syntax of a list is square brackets

"""
if False:
    
    our_first_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]
    print(our_first_list)
    
    # things to notice
    # no range
    # for "each" loop
    # each fib that gets pulled out of the list is NOT an index it is an element.
    for fib in our_first_list:
        print(fib)
    
    # indices start at 0
    print(our_first_list[7])
    # IndexError - out of range
    # print(our_first_list[12])
    
    give_me_index = int(input('Which element do you want? '))
    # need to know the list's length in order to prevent user from doing anything naughty.
    if 0 <= give_me_index < len(our_first_list):
        print(our_first_list[give_me_index])
    else:
        print('You would have got an error here.  Bad Human.')
    
    """
        len(a_list) returns the length of a list (int)
    """
    # len -> int
    # range(int) 0 up to but not including that length
    for index in range(len(our_first_list)):
        print(our_first_list[index])
    
    fruit_list = ['apple', 'orange', 'tomato', 'raspberry', 'pumpkin', 'banana*']
    
    # fruit is a copy of the element in the list, NOT the element itself
    for fruit in fruit_list:
        print('A fruit is', fruit)
        fruit = 'pineapple'
        print('A fruit is', fruit)
    # after this loop the list is not changed, because the fruit var is a copy
    
    # index loop (for-i loops)
    for index in range(len(fruit_list)):
        print(index, 'A fruit is', fruit_list[index])
        fruit_list[index] = 'pineapple'
        # the list is changed because we are accessing individual indices
    
    print(fruit_list)
    
    movie_list = []
    for i in range(8):
        the_movie = input('Tell me a movie: ')
        # append adds the_movie to the end of the list
        movie_list.append(the_movie)
    
    print(movie_list)
    
    another_list = []
    another_list.append(5)
    another_list.append('hello there')
    another_list.append(3.14)
    another_list.append(True)
    print(another_list)
    
    # be careful!!!!
    # for x in another_list:
    #     print(x + 5)
    
    # 2d-array / 2d-list
    a_nested_list = [[1, 2, 3], [4, 5], []]
    print(a_nested_list[0])
    print(a_nested_list[0][2])
    print(a_nested_list)
    
    a_3d_list = [[[1, 2, 3], [2, 3, 4]], [[1, 2, 3], [2, 3, 4]], [[1, 2, 3], [2, 3, 4]]]
    # list-ception
    
    """
        Remove method
            remove by element
                list.remove(value)
            remove by index
                del list[index]
    """
    alphabet = ['a', 'b', 'c', 'd', 'c', 'c', 'e', 'f', 'c', 'g', 'h', 'i', 'j']
    print(alphabet)
    alphabet.remove('c')
    print(alphabet)
    if 'm' in alphabet:
        alphabet.remove('m')
    else:
        print('m wasnt there')
    
    count = 0
    
    for letter in alphabet:
        if letter == 'c':
            count += 1
    # don't touch the list in here
    for index in range(count):
        alphabet.remove('c')
    
    print(alphabet)
    
    # kill element 5
    del alphabet[3]
    print(alphabet)
    del alphabet[5]
    print(alphabet)

square_dim = int(input('How big is the square? '))
for i in range(square_dim):
    for j in range(square_dim):
        print('(', i, ',', j, ')', end='')
    print()
