"""
    Second midterm is next week. (Wed 17th)
    Project 2 is out.
        -- Youtube Video about the project.
        
    Recursion:
        Turtles all the way down
        
        functions that call themselves
        
        We need a base case... tells us where to stop
"""


def countdown(x):
    if x < 0:
        print('Blast off')
        return
    else:
        print(f'T = {x}')
        countdown(x - 1)


# countdown(42)


"""
    Factorials :)
    
    0! = 1
    
    abc, acb, bac, bca, cab, cba 3! = 6 = 3(2)(1)
    
    n!= n * (n - 1) * (n - 2) * (n - 3) * .. * 3 * 2 * 1 *0!
    better way to say it:
    n! = n * (n - 1)!
    
    fact(n) = n * fact(n - 1)

    0! = 1, 1! = 1, 2! = 2 * 1 = 2
    3! = 3 * 2 * 1 = 6
    4! = 4 * 3 * 2 * 1 = 4 * 6 = 24
    5! = 5 * 4 * 3 * 2 * 1 = 5 * 24 = 120
"""


def iterative_fact(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer


def fact(n):
    if n == 0:
        return 1
    
    temp = n * fact(n - 1)
    return temp


def fib(n, tab_level):
    """
        Base case: fib(0) = fib(1) = 1
    
        Recursive case:
            fib(n) = fib(n - 1) + fib(n - 2)
    """
    print('\t' * tab_level, n)
    # if n == 0 or n == 1:
    if n in [0, 1]:
        return 1
    else:
        return fib(n - 1, tab_level + 1) + fib(n - 2, tab_level + 1)


# print('The fibonacci you wanted was', fib(30, 0))


"""
    Time for strings
    
    L = 0 that have a's and b's only
        ''
    L = 1 that have a's and b's only
        a, b
    L = 2
        aa, ab
        ba, bb
    L = 3
        aaa, aab
        aba, abb
        baa, bab
        bba, bbb
    L = 4
        aaaa, aaab
        aaba, aabb
        abaa, abab
        abba, abbb
        baaa, baab
        baba, babb
        bbaa, bbab
        bbba, bbbb
        
    How did i do this?
        copy paste all the answers of length n - 1
        add either an a or b
"""


def make_ab_strings(length, current):
    if length == 0:
        print(current)
    else:
        make_ab_strings(length - 1, current + 'a')
        make_ab_strings(length - 1, current + 'b')


make_ab_strings(4, '')


def make_into_ab_binary(num, length):
    answer = ''
    # change this to a for to pad this with a's/0's
    for t in range(length):
        if num % 2 == 0:
            answer = 'a' + answer
        else:
            answer = 'b' + answer
        
        num //= 2
    return answer


def make_ab_iteratively(length):
    for i in range(2 ** length):
        print(make_into_ab_binary(i, length), bin(i))


make_ab_iteratively(4)

"""
    Need recursion: pathfinding on a grid

No diagonals

...#
.S#F
.#..
....

Answer: search all possible directions

search(current_pos):
    r1 = search(up(current_pos))
    r2 = search(left(current_pos))
    r3 = search(right(current_pos))
    r4 = search(down(current_pos))

if any of the r1... r4 have found the finish,
    then that was a path to the finish and we win.
    
"""

def search(the_grid, current_pos):
    
    y, x = current_pos
    if the_grid[y][x] == 'F':
        return current_pos
    
    search(the_grid, (y - 1, x))
    search(the_grid, (y, x - 1))
    search(the_grid, (y, x + 1))
    search(the_grid, (y + 1, x))
    