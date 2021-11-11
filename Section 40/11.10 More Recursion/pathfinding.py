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


def make_visited_list(rows, cols):
    new_visited_list = []
    for r in range(rows):
        new_visited_list.append([False] * cols)
    return new_visited_list


def pathfinding(current_pos, prev_pos, final_pos, the_grid, visited):
    """
        what is the base case?
            if you find the final_pos, meaning that current_pos == final_pos
    """
    
    print(prev_pos, ' -> ', current_pos)
    
    if current_pos == final_pos:
        return [final_pos]
    
    # make all choices
    y, x = current_pos
    
    if visited[y][x]:
        return False
    
    visited[y][x] = True
    
    up = False
    right = False
    down = False
    left = False
    # up
    if 0 <= y - 1 < len(the_grid) and the_grid[y - 1][x] != FORBIDDEN:
        up = pathfinding((y - 1, x), current_pos, final_pos, the_grid, visited)
        if up:
            the_grid[y][x] = 'M'
            return [current_pos] + up
    # right
    if 0 <= x + 1 < len(the_grid[y]) and the_grid[y][x + 1] != FORBIDDEN:
        right = pathfinding((y, x + 1), current_pos, final_pos, the_grid, visited)
        if right:
            the_grid[y][x] = 'M'
            return [current_pos] + right
    # down
    if 0 <= y + 1 < len(the_grid) and the_grid[y + 1][x] != FORBIDDEN:
        
        down = pathfinding((y + 1, x), current_pos, final_pos, the_grid, visited)
        if down:
            the_grid[y][x] = 'M'
            return [current_pos] + down
    
    # left
    if 0 <= x - 1 < len(the_grid[y]) and the_grid[y][x - 1] != FORBIDDEN:
        left = pathfinding((y, x - 1), current_pos, final_pos, the_grid, visited)
        if left:
            the_grid[y][x] = 'M'
            return [current_pos] + left
    
    return False


rows = 8
cols = 5
my_grid, end_point = make_grid(rows, cols)
display_grid(my_grid, (0, 0))
visited_list = make_visited_list(rows, cols)
print(pathfinding((0, 0), None, end_point, my_grid, visited_list))
display_grid(my_grid, end_point)
