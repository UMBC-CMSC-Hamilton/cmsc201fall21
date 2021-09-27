if False:
    width = int(input('Width: '))
    height = int(input('Height: '))
    
    for y in range(height, 0, -1):
        print(y, '\t', end="")
        for x in range(width):
            if (y) / (x + 1) <= (height + 1) / (width + 1):
                print('*', end="")
            else:
                pass
        print()
    radius = int(input('Choose radius: '))

    for i in range(-1 * radius, radius + 1):
        for j in range(-1 * radius, radius + 1):
            if i ** 2 + j ** 2 <= radius ** 2:
                print('*', end="")
            else:
                print(' ', end="")
        print()

    # I generally add a space to the end of the input prompt string
    dist = int(input('Tell me side length: '))

    for y in range(dist):
        for space_int in range(y):
            print(' ', end="")
        for x in range(dist):
            print('*', end="")
        print()

    steps = int(input('How many steps do you want to run? '))
    my_list = []
    # for loops only run a prescribed number of times, can't really change it
    #       during the for loop.
    for step in range(steps):
        command = input('What do you want to do? ')
        split_command = command.split()
    
        print(split_command)
    
        if split_command[0].lower() == 'add':
            my_list.append(split_command[1])
        elif split_command[0].lower() == 'remove':
            # tests to make sure the item is in the list
            # if it is remove will work
            # if it isn't, remove will fail, so don't do that...
            if split_command[1] in my_list:
                my_list.remove(split_command[1])
            else:
                print(split_command[1], 'was not in the list, please don\'t do that...')
        print(my_list)

if __name__ == '__main__':
    how_many = int(input('how many integers? '))
    int_list = list()
    # int_list = []
    for i in range(how_many):
        # int_list.append(int(input('Tell me an int: ')))
        temp_int = int(input('Tell me an int: '))
        int_list.append(temp_int)
    
    print(int_list)
    """
        What is the max of a list?
        
        no max keyword
    """
    
    # if len(int_list) > 0:
    # lists are true if they're non-empty
    # lists are also false if they are empty.
    if int_list:
        # we set int_list[0] to current_max to prevent the bug where
        # negative numbers don't work
        # causes new bug == empty lists
        current_max = int_list[0]
        
        for x in int_list:
            if x > current_max:
                current_max = x
                print('current max is ', x)
        
        print(current_max, 'is the max')
