"""

S.#..
#...#
##..#
..#..
F..#.
##...


"""

import random

ALLOWED = '.'
FORBIDDEN = '#'
PLAYER = 'P'
START = 'S'
FINISH = 'F'


def make_grid(rows, cols):
    the_grid = []
    for r in range(rows):
        new_row = random.choices([ALLOWED, FORBIDDEN], weights=[3, 1], k=cols)
        the_grid.append(new_row)
    finish_y = random.randint(0, rows - 1)
    finish_x = random.randint(0, cols - 1)
    the_grid[finish_y][finish_x] = FINISH
    return the_grid, (finish_y, finish_x)


def display_grid(the_grid, our_position):
    y, x = our_position
    for row in range(len(the_grid)):
        if row == y:
            copy_row = list(the_grid[row])
            copy_row[x] = PLAYER
            print(' '.join(copy_row))
        else:
            print(' '.join(the_grid[row]))


def make_visited_list(dim_y, dim_x):
    # pure laziness
    return [[False for _ in range(dim_x)] for _ in range(dim_y)]


def pathfind(current_pos, prev_pos, final_pos, the_grid, visited):
    """
    :param current_pos:
        check all of the positions around current position
    :param final_pos:
    :param the_grid:
    :param visited:
    :return:
        
        We're going to immediately go out of bounds
        
        check bounds
        check forbidden positions
        check all directions (not forbidden, not visited, in bounds)
        return the path
    
    """
    y, x = current_pos
    
    if current_pos == final_pos:
        # we found it
        return [final_pos]
    
    if visited[y][x]:
        return False
    print(prev_pos, ' -> ', current_pos)
    
    visited[y][x] = True
    
    up = False
    down = False
    left = False
    right = False
    
    if 0 <= y - 1 and the_grid[y - 1][x] != FORBIDDEN:
        up = pathfind((y - 1, x), current_pos, final_pos, the_grid, visited)
    if y + 1 < len(the_grid) and the_grid[y + 1][x] != FORBIDDEN:
        down = pathfind((y + 1, x), current_pos, final_pos, the_grid, visited)
    if x + 1 < len(the_grid[y]) and the_grid[y][x + 1] != FORBIDDEN:
        right = pathfind((y, x + 1), current_pos, final_pos, the_grid, visited)
    if x - 1 >= 0 and the_grid[y][x - 1] != FORBIDDEN:
        left = pathfind((y, x - 1), current_pos, final_pos, the_grid, visited)
    
    if up:
        return [current_pos] + up
    elif down:
        return [current_pos] + down
    elif right:
        return [current_pos] + right
    elif left:
        return [current_pos] + left
    else:
        return False
    
    # return up or down or left or right


num_rows = 5
num_cols = 5
a_grid, finish_position = make_grid(num_rows, num_cols)
display_grid(a_grid, (0, 0))

print(pathfind((0, 0), (0, 0), finish_position, a_grid, make_visited_list(10, 20)))
