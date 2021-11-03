"""

takes in a list and finds the max of that list.

1) input a list of integers
2) find the maximum of that list

i didn't talk about declaring variables, you'll have to make it work
get new input
loop while input is not stop:
    add the input to the list of integers
        i didn't say anything about casting, integer (probably casting)
    get new input

set max = -1
scan through the list:
    if list element > max:
        set max = list element

print(max)

"""


def max_of_ints():
    my_list_of_ints = []
    new_string = input('Enter a number or STOP')
    while new_string != 'STOP':
        my_list_of_ints.append(int(new_string))
        new_string = input('Enter a number or STOP')
    
    current_max = -1
    for x in my_list_of_ints:
        if x > current_max:
            current_max = x
    
    print(current_max)


"""
    how do you write tetris?
    
make a rectangle 20 down 10 wide

-- code in the shapes somehow - we'll figure this out

rotation for the shapes ... ugh

shapes have to descend

collision detection

add it to the group of shapes already there

kill filled lines, shift down

count score or something (make this up)

if a shape finalizes in a position where it exceeds the top of the
grid then we lose

we can't win there's no such thing as winning...

can we store shapes? maybe
can we display the next one? much easier


# this is done
board = build a grid array 2D 5 rows higher than is visible
# still need to do this
shapes = build our shape arrays 2D arrays, a list of 2D lists

while not game_over(board):

    display_board(board) # done
    
    if not current_shape:
        new current_shape = random.choice(shapes)
        
    push_shape_down(current_shape, pos_x, pos_y, board)
    finalize_shape(current_shape, pos_x, pos_y, board)
    
    for line in board:
        if full_line(line):
            kill_line(line)
    
    user_input = get user input
    if user_input == rotate:
        rotate_shape(current_shape, board)
    elif user_input == down:
        mash_shape_down(current_shape, pos_x, pos_y, board)
    
"""

"""
    game_over(board)
     check a board and determine whether there is anything in the
    top 5 lines.
"""

# number of lines above the game that are not visible but detect end of game

# all of these are "constants"
# put them under your header, any imports before your functions
"""
header
import

constants

declare functions
def f1():
    pass
def f2():
    pass

if name == main:
    main code
"""
TOP_LINES = 5
GAME_ROWS = 20
GAME_COLS = 10
FILLED = '*'
EMPTY = '.'


def make_board(rows, cols):
    board = []
    for r in range(rows):
        new_line = []
        for c in range(cols):
            new_line.append(EMPTY)
        board.append(new_line)
    return board


def display_board(board, top_lines):
    for i in range(len(board)):
        if i >= top_lines:
            print(''.join(board[i]))


"""
    game_over(board, TOP_LINES, GAME_COLS)
    
    is anything in the top lines not empty?
"""


def game_over(board, top_lines, cols):
    for i in range(top_lines):
        for c in range(cols):
            if board[i][c] != EMPTY:
                return True
    
    return False


"""
push_shape_down(current_shape, pos_x, pos_y, board)

"""


def can_push_shape_down(current_shape, pos_x, pos_y, board):
    for i in range(len(current_shape)):
        for j in range(len(current_shape[i])):
            if current_shape[i][j] == FILLED:
                if pos_y + i + 1 < len(board) and pos_x + j < len(board[i]):
                    if board[pos_y + i + 1][pos_x + j] == FILLED:
                        return False
    
    return True


"""
    Tests:
    empty board, current_shape not at bottom --> True
    board that blocks the shape, not at bottom -> False
    test where the shape is at the bottom --> False
    test where the shape is one from the bottom / two from the bottom
    
    "unit testing" - test one thing at a time
        if one test fails, you know what happened
        put all the unit tests together , ideally it should be
            a working function
            
    if you put two different functions in where they both pass
        all tests the rest of the code shouldn't fail
"""

if __name__ == '__main__':
    the_board = make_board(TOP_LINES + GAME_ROWS, GAME_COLS)
    display_board(the_board, TOP_LINES)
    # empty board test
    print(game_over(the_board, TOP_LINES, GAME_COLS) == False)
    the_board[13][5] = FILLED
    print(game_over(the_board, TOP_LINES, GAME_COLS) == False)
    the_board[2][3] = FILLED
    print(game_over(the_board, TOP_LINES, GAME_COLS) == True)
