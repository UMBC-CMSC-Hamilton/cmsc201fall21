features = {"ben": "sleepy", "eric": "tenacious", "monali": "gremlin"}
features[1] = 'numbers'
print(features)
print(features['monali'][1:6])
features["charlie"] = features["ben"]
print(features["charlie"])

# no errors will be visible
the_string = '012happy broccoli'

expr = the_string[3:8] == 'happy' or 'broccoli' not in the_string

print(expr)

the_grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 12]]

expr_2 = the_grid[0][0] == 1 or the_grid[1][1] == 1 or the_grid[2][2] == 1

"""
    Shallow vs deep:

        a shallow copy is a reference (not a copy)
        
        a deep copy is a copy
"""

a_list = [1, 2, 3, 4, 5]
# a shallow copy (mutable, references)
b_list = a_list
# b_list is a secret alias for a_list
b_list[2] = 17
print(a_list)

# how do you make a deep copy then?
deep_list = list(a_list)
deep_list[2] = 82
print(deep_list)
print(a_list)

wombats = []
# shallow
marsupials = wombats
# deep
marsupials = list(wombats)

if False:
    a = 'a'
    b = 3
    print(a + b)
    
    
    def get_the_important_string():
        return None
    
    
    the_string = get_the_important_string()
    split_string = the_string.split()
    
    """
    Global Constants are global variables which don't change
    if you're allowed to change the variable, then we'd just call it a global variable
        global = outside of any function
        local = inside of a function
    """
    
    """
    A boolean flag is a bool variable which tracks a certain event/change/state
    
        not_found = True as long as whatever we're looking at hasn't found the thing we are looking for the
        encountered_error
        received_quit_message
    """
    
    not_quit_found = True
    
    while not_quit_found:
        s = input()
        if s == 'quit':
            not_quit_found = False
        
    # better:
    s = input()
    while s != 'quit':
        s = input()
    

nicknames = {
    "Eric": "eric8",
    "Min": "Mino",
    "Sean": "Seanathon",
    "Joshua": "Slaughter",
    "Marzuq": "Fire Lord Zuq-o!"
}
names = nicknames
# names is a shallow copy of nicknames (not a copy)
# names "references" nicknames
del names["Eric"]
print(nicknames.get("Eric", 0))
# keyerror
#print(nicknames['Eric'])
# K8BL8eK8hK8...

utterance = "Behold Anglatron, the mighty!"
print("K8".join(utterance.split("Anglatron")))

def get_corner_values(big_list):
    the_corners = []
    if not big_list:
        return the_corners
    
    if big_list[0]:
        the_corners.append(big_list[0][0])
        the_corners.append(big_list[0][len(big_list[0]) - 1])
        # the_corners.append(big_list[0][- 1])
    
    last_index = len(big_list) - 1
    if big_list[last_index]:
        the_corners.append(big_list[last_index][0])
        the_corners.append(big_list[last_index][-1])
    return the_corners

# [[0], [], [4]]


def get_max_values(list_of_lists):
    list_of_maxima = []
    for my_list in list_of_lists:
        current_max = -1
        for x in my_list:
            if x > current_max:
                current_max = x
        list_of_maxima.append(current_max)
    
    return list_of_maxima