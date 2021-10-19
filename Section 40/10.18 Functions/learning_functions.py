"""
    What is a function?
    
    A way to allow us to repeat code whenever we "call" a specific name.

"""


# definition / signature
# def keyword = python keyword that says "here is a function"
# function name = print_hello
# parameter list = variables that get input into the function.
def print_hello(number):
    for i in range(number):
        print('hello there')


def repeat_hellos():
    n = int(input('Tell me a number: '))
    while n != 0:
        print_hello(n)
        n = int(input('Tell me a number: '))


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            # as soon as we call this return, the function stops
            return False
    # way to communicate from inside a function to outside again
    return True


def factor_me(n):
    """
        When you declare variables inside of a function
        they only live as long as the function is running
        when the function returns then they are all 'reset'
        next time you call the function the values will be back to
        their original values
    """
    prime_list = []
    for i in range(2, 50):
        if is_prime(i):
            prime_list.append(i)
    
    factor_list = []
    for the_prime in prime_list:
        while n % the_prime == 0:
            factor_list.append(the_prime)
            n //= the_prime
    
    return factor_list


def get_food():
    all_the_food = []
    s = input('Tell me some kind of food to eat? ')
    while s != 'quit':
        all_the_food.append(s)
        s = input('Tell me some kind of food to eat? ')
    return all_the_food


def test_functions():
    n = int(input('Tell me a number: '))
    while n != 0:
        # it's a different name than factor_list
        # does that matter? no you can call the returned variable whatever
        # my_factors has all the data from the factor_list, but 'we' forget
        # the name
        my_factors = factor_me(n)
        # remember if you want the data to display there's two steps
        # 1) save the data in a variable like we did above
        # 2) print it out or whatever you want
        print(my_factors)
        n = int(input('Tell me a number: '))
    
    # print(get_food())
    student_food = []
    student_list = ['Eric', 'Sean', 'Dennis', 'Jean Luc', 'Toja']
    for student in student_list:
        print(student, 'it is your turn to be fed')
        student_food.append(get_food())
    print(student_food)


def tic_tac_toe_horizontal(the_grid):
    # horizontal cases first:
    for i in range(3):
        symbol = the_grid[i][0]
        all_match = True
        for j in range(3):
            if the_grid[i][j] != symbol:
                all_match = False
        if all_match and (symbol == 'x' or symbol == 'o'):
            return symbol
    
def tic_tac_toe_veritcal(the_grid):

    for i in range(3):
        symbol = the_grid[0][i]
        all_match = True
        for j in range(3):
            if the_grid[j][i] != symbol:
                all_match = False
        if all_match and (symbol == 'x' or symbol == 'o'):
            return symbol

def tic_tac_toe_game_over(the_grid):
    winner = tic_tac_toe_horizontal(the_grid)
    # if winner == 'x' or winner == 'o':
    if winner in ['x', 'o']:
        return winner
    
    winner = tic_tac_toe_veritcal(the_grid)
    # if winner == 'x' or winner == 'o':
    if winner in ['x', 'o']:
        return winner

    if the_grid[0][0] == the_grid[1][1] == the_grid[2][2]:
        if the_grid[0][0] in ['x', 'o']:
            return the_grid[0][0]
        else:
            return 'no winner'
    
    if the_grid[0][2] == the_grid[1][1] == the_grid[2][0]:
        if the_grid[0][2] in ['x', 'o']:
            return the_grid[0][2]
        else:
            return 'no winner'
    
    return 'no winner'


if __name__ == '__main__':
    print(tic_tac_toe_game_over([
        ['x', 'x', 'o'],
        ['o', 'o', 'o'],
        ['x', 'x', 'x'],
    ]))
    
    print(tic_tac_toe_game_over([
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]))
    
    print(tic_tac_toe_game_over([
        ['x', ' ', ' '],
        [' ', 'x', ' '],
        [' ', ' ', 'x'],
    ]))
    
    print(tic_tac_toe_game_over([
        ['x', 'x', 'o'],
        ['x', 'o', 'x'],
        ['o', 'x', 'x'],
    ]))

    print(tic_tac_toe_game_over([
        ['x', 'x', 'o'],
        ['x', 'o', 'x'],
        ['x', 'o', 'x'],
    ]))