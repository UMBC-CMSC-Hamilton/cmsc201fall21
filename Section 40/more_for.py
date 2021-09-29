"""
    for loops come in two flavors...
    
        for - i[ndex] loops
            i traditional index,
            the variable of the loop represents an index or a count
            range( something )
            range( len(some_list))
            range(17)
            range(my_favorite_int)
            
        for - each loops
            elements of a list
"""
if False:
    
    the_sum = 0
    n = int(input('Tell me how many squares you want to sum: '))
    
    for an_int in range(n):
        # an_int is an index
        the_sum += an_int ** 2
        
    my_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    
    for an_index in range(len(my_list)):
        print(my_list[an_index])
    
    # for-each loop why?
    #   they represent elements
    #   even if i replace two_powers with i
    for two_powers in my_list:
        print(two_powers)
        
    
    num_steps = int(input('How many steps do you want to run? '))
    
    the_list = []
    for step in range(num_steps):
        command = input('Tell me what to do to the list: ')
        # add element
        # remove element
        # delete index
        split_command = command.split()
        # split_command[0] is going to be the command whatever that is
        if split_command[0] == 'add':
            the_list.append(split_command[1])
        elif split_command[0] == 'remove':
            if split_command[1] in the_list:
                # remove always works by "value"
                the_list.remove(split_command[1])
            else:
                print('Hey that wasn\'t in the list, you should be more careful')
        elif split_command[0] == 'delete':
            # del always works by index
            index = int(split_command[1])
            # let's check the index to make sure it's a valid one
            # if 0 <= index and index < len(the_list):
            #   they are the same
            if 0 <= index < len(the_list):
                del the_list[index]
            else:
                print('Hey you know better than that... Use the force...')
        
        print(the_list)
        

length_of_list = int(input('Tell me the number of integers to input: '))

int_list = []
for i in range(length_of_list):
    temp_int = int(input('Tell me an integer: '))
    int_list.append(temp_int)
    
"""
    What is the minimum of a list?
"""
print(int_list)

# lists are true if they're non-empty
if int_list:
    current_min = int_list[0]
    for x in int_list:
        # for each loop
        if x < current_min:
            current_min = x
            print(current_min)

    print(current_min)