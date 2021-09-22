"""
    how for loops work (with range)

    range(stop)
    range(start, stop)
    range(start, stop, step)
"""

if False:
    for i in range(2, 9):
        print(i)
    
    for i in range(5, 100, 3):
        print(i)
    
    # negative step sizes are allowed
    for j in range(10, 0, -17):
        print(j)
    
    first_student = 'Aaron Aaronson'
    second_student = 'Adam Adamson'
    # this is not a great way to do it
    student_120 = 'Zadam'
    
    # this is an empty list
    student_list = ['Charles', 'Nick', 'Benjamin', 'Zachary', 'Eric', 'Dennis']
    other_empty = list()
    
    print(student_list)
    print(student_list[2])
    student_list[2] = "Josh"
    print(student_list)
    
    # IndexError
    # print(student_list[17])
    
    """
        for each loops - if it spits out elements of the list (each)
        for-i loops (indices, then we call it for-i)
    """
    for name in student_list:
        print('one of the students is called', name)
    
    for index in range(0, len(student_list) // 2):
        print(student_list[index])
    
    # print(student_list[6])
    
    my_movie_list = []
    for i in range(8):
        movie_name = input('Tell me a movie: ')
        my_movie_list.append(movie_name)
    
    print(my_movie_list)
    
    my_fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 111, 200]
    
    for index in range(2, len(my_fibs)):
        # if you put a negative index in, it'll probably work...
        if my_fibs[index] == my_fibs[index - 1] + my_fibs[index - 2]:
            print(my_fibs[index], 'is Fibonacci')
        else:
            print(my_fibs[index], 'isn\'t Fibonacci')
    
    my_ints = [1, 2, 3, 4, 5]
    for an_int in my_ints:
        an_int **= 2
        print(an_int)
    
    print(my_ints)
    
    # if you want to modify a list, you need to access the element by its index
    # you cannot just change the element in a for-each loop like above.
    for index in range(len(my_ints)):
        my_ints[index] **= 2
        
    # int, string, float, bool are "immutable"
    print(my_ints)
    
    first_list = ['a', 'b', 'c']
    second_list = ['1', '2', '3']
    new_list = []
    
    for i in range(len(first_list)):
        new_list.append(first_list[i])
        new_list.append(second_list[i])
    
    print(new_list)
    
    the_square_size = int(input('Square size: '))
    for i in range(the_square_size):
        for j in range(i + 1):
            print('*', end='')
        print() # gives us that endline that we killed in the other print statement
    
    
for i in range((-1) * the_square_size, the_square_size + 1):
    for j in range((-1) * the_square_size, the_square_size + 1):
        if i ** 2 + j ** 2 <= the_square_size ** 2:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()


the_square_size = int(input('Square size: '))
for i in range(the_square_size):
    for j in range(the_square_size - i):
        print(' ', end='')

    for j in range(the_square_size):
        print('*', end='')
    print()  # gives us that endline that we killed in the other print statement


