"""
    - pseudocode
        What is it?
            pseudo - fake/false
            pseudocode is like "fake code" or "almost code"
            
            get the ideas of the eventual code that you are going to
                write
                
            don't worry about syntax as much.
    - top down design
    
    - testing

"""

"""
    Example:
        Come up with a program which determines the number of
            even numbers in a list

Kinda pseudocode
1) input a list of integers
2) count the even ones

split_list = split the input('Enter a list of integers')
int_list = a new list ([])
for each thing in the split_list
    cast it to an integer and append into int_list

set count = 0 [if you question for 0.2 ns, write this]

for each number in the int_list:
    if the number is even:
        increment the count
        [count is technically undefined]
        [is it clear that we need to create it and set it to zero?]

"""


def count_evens():
    split_list = input('Enter a list of integers').split()
    int_list = []
    
    for x in split_list:
        int_list.append(int(x))
    
    count = 0
    
    for n in int_list:
        if n % 2 == 0:
            count += 1
    
    print(count)


"""
find_root(a, b, c)
    if a == 0 and b == 0 and c != 0:
        return 'impossible'
        
    elif a == 0:
        return -c/b
    
    if b^2 - 4ac < 0:
        avoid doing the square root
        return "complex solution"
    
    else find the solution using the quadratic equation
    s1 = the solution with plus
    s2 = the solution with minus
    
    return [s1, s2]
    
"""


def find_root(a, b, c):
    if a == 0 and b == 0:
        if c != 0:
            # 0 x^2 + 0 x + c = 0
            return 'impossible'
        else:
            # 0 x^2 + 0 x + 0 = 0
            return 'all x works'
    elif a == 0:
        return -c / b
    
    if b ** 2 - 4 * a * c < 0:
        return 'complex'
    
    disc = b ** 2 - 4 * a * c
    s1 = (-b + disc ** (1 / 2)) / (2 * a)
    s2 = (-b - disc ** (1 / 2)) / (2 * a)
    
    return [s2, s1]


def test_find_root():
    """
        Unit Testing:
            Each test tests one specific thing
            
                - when a test fails, we know what went wrong
                    - where to go to fix it
            Try to build as many tests as you want
                in order to test all the different paths of the function
            
    """
    print(find_root(0, 0, 0) == 'all x works')  # all x now but maybe not
    print(find_root(0, 0, 5) == 'impossible')  # impossible
    print(find_root(0, 2, 5) == -2.5)  # -5/2 = -2.5 [2x + 5 = 0]
    print(find_root(1, 4, 3) == [-3, -1])  # -3, -1
    print(find_root(1, 1, 7) == 'complex')  # complex
    print(find_root(1, -4, 3) == [1, 3])  # 1, 3
    print(find_root(1, 0, -1) == [-1, 1])  # -1, 1
    print(find_root(1, -1, -1) == [(1 - 5 ** (1 / 2)) / 2, (1 + 5 ** (1 / 2)) / 2])  # -0.618, 1.618


test_find_root()


"""
    pseudocode practice
    
    >imagine< project 2 was tetris
    
    Desc: Write Tetris.
    

    board rectangular board
        rows, cols
    shapes, rotate somehow
    
    if a row is filled, kill it
    
    if a shape finalizes in a position higher than the board, that's the lose condition
    
    count score
    
    move shape down
    when the shape can't move down it 'finalizes'
    
    user input:
        if down:
            push the shape as far down and then finalize
        elif up:
            rotates the shape
        elif right:
            can you shift the shape right?
        elif left:
            can you shift the shape left?
"""

TOP_ROWS = 5
NUM_ROWS = 20
NUM_COLS = 10
FILLED = '\u2610'
EMPTY = ' '

"""
    if it's not declared in the if_name_ block
        and not a constant
    then: pass it as a parameter into each function
"""


"""
the_board = a grid (2d list) which is a 25 rows and 10 cols
shapes = [a list of the shapes]


def game_over(the_board, TOP_ROWS):
    check to see if anything is in the first TOP_ROWS
        if it is, return True
    
    return False


row = y position of the shape
col = x position of the shape

while not game_over(the_board):
    if can_push_shape_down(shape, row, col, the_board):
        row += 1
    else:
        finalize_shape(shape, row, col, the_board)
        shape = random.choice(shapes)
        row = 0
        col = 4
    
    for i in range(len(the_board)):
        if filled_row(i, the_board):
            kill_row(i, the_board)
    
    get user input
    etc etc
    
    

"""
print(FILLED)