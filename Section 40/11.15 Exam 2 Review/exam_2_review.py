def get_three():
    return 3

print(get_three())


#LHS = RHS
#get_three() = 4

features = {"ben": "sleepy", "eric": "tenacious", "monali": "gremlin"}
features["charlie"] = features["ben"]
print(features)
print(features["charlie"])

the_string = '012happybroccoli'
exp_ans = the_string[3: 8] == 'happy' or 'broccoli' not in the_string
print(exp_ans)

"""
    diagonal elements are where row == col
    3x3
    [0][0]
    [1][1]
    [2][2]
    
    what about the anti-diag
    
    row = len - 1 - col

"""

the_grid = [
    [4, 5, 9],
    [1, 8, 2],
    [3, 0, 7]
]

# don't need grid_bool
grid_bool = the_grid[0][0] == 1 or the_grid[1][1] == 1 or the_grid[2][2] == 1

my_list = [1, 2, 3, 4, 5]
# shallow copy - reference
# shallow is a new name for the same object that is in my_list
# do this assignment with a mutable thing this is what happens
shallow = my_list
shallow[2] = 17
print(my_list)
# shallow copy is not a copy

# deep copy
real_copy = list(my_list)
real_copy[2] = 555
print(real_copy)
print(my_list)

wombats = []
# shallow
marsupials = wombats
# deep
marsupials = list(wombats)

if None:
    a = None
    b = 17
    print(a + b)
    
    def get_a_string():
        return None
    
    get_a_string().split()

"""
    global = not declared in a function
        if name == main
        above it is also global
        constants are technically global variables
    local = declared in a function

"""


"""`
A boolean flag tracks a change of some kind.
    letter_a_found
    message_received
    positive_number_entered
    overflow_flag
    
    once the flag is set, it stays set (generally) until we check to see what happened
"""

nicknames = {
    "Eric": "eric8",
    "Min": "Mino",
    "Sean": "Seanathon",
    "Joshua": "Slaughter",
    "Marzuq": "Fire Lord Zuq-o!"
}
names = nicknames
if "Eric" in nicknames:
    print('Eric is in there')
del names["Eric"]
if "Eric" in nicknames:
    print('Eric is in there')
else:
    print('not')
print(nicknames.get("Eric", 0))


a_list = [[1, 2, 3],
          [3, 4, 5],
          [5, 6, 7]]

for x in range(3):
    print(a_list[(2 * x + 1) % 3][(5 * x) % 3])

"""
    Let's think about how to do this:
    
    x = 0
    [2(0) + 1 mod 3][5 * 0 mod 3]
    [1][0] --> 3
    
    [2(1) + 1 mod 3][5 * 1 mod 3]
    [0][2] --> 3
    
    [2 * 2 + 1 mod 3][5 * 2 mod 3]
    [2][1] --> 6

"""

utterance = "Behold Anglatron, the mighty!"
"""

['Behold ', ', the mighty!']

"""
print("K8".join(utterance.split("Anglatron")))
"K8BK8eK8hK8oK8lK8dK8..."
print('K8'.join(list(utterance)))

def get_corners(the_grid):
    corners = []
    if not the_grid:
        return []
    
    if the_grid[0]:
        corners.append(the_grid[0][0])
        corners.append(the_grid[0][-1])

    if the_grid[-1]:
        corners.append(the_grid[-1][0])
        corners.append(the_grid[-1][-1])

    return corners


def get_max_values(list_of_lists):
    max_list = []
    
    for my_list in list_of_lists:
        # get the max from that list
        current_max = my_list[0]
        for x in my_list:
            if x > current_max:
                current_max = x
        
        max_list.append(current_max)
    
    return max_list


def count_a_keys(my_dict):
    total = 0
    for key in my_dict:
        if key and key[0] == 'a':
            for x in my_dict[key]:
                total += x
                
    return total


def sum_row_col(grid, x, y):
    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if row == x or col == y:
                total += grid[row][col]
    return total

print(sum_row_col([[8, 2], [5, 7]], 1, 0))
print(sum_row_col([[1,2,3], [2,3,4], [3, 7, 9]], 0, 0))
print(sum_row_col([[1,2,3], [2,3,4], [3, 7, 9]], 2, 1))
