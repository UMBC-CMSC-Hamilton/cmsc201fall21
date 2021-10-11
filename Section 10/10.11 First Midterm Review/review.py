if False:
    my_list = [1, 2, 3, 4, 5]
    
    # for x in my_list:
    #    x = x * 2 - 3
    
    for i in range(len(my_list)):
        my_list[i] = my_list[i] * 2 - 3
    
    print(my_list)
    
    x = 2
    x *= 5
    print(x)
    
    x = int(input('Tell me x: '))
    while x != 3:
        x *= 2
        print(x)
    
    """ boolean flag is just a boolean variable

    """
    the_list = []
    
    found_seventeen = False
    
    for i in range(len(the_list)):
        if the_list[i] == 17:
            found_seventeen = True
    
    # just so that the vars are defined
    age = 0
    height = 0
    
    # age >= 15 and height > 50 is the expression
    if age >= 15 and height > 50:
        pass
    
    # not on exam
    best_activities = []
    
    len(best_activities) >= 7 and best_activities[0] == 'nap' \
    and 'chicanery' not in best_activities
    
    list_one = [1, 2, 3, 4, 5]
    
    list_two = [1, 2, 3, 4, 5]
    
    if list_one == list_two:
        print('ok')
    
    if list_one is list_two:
        print('huh?')
    
    for i in range(len(list_one)):
        if list_one[i] % 2 == 0:
            list_one[i] *= 3
    
    for i in range(10, 2, -2):
        print(i)

if __name__ == '__main__':
    list_of_five = []
    for i in range(5):
        # because i'm lazy
        list_of_five.append(int(input('Enter a number: ')))
    
    for x in list_of_five:
        if x % 2 == 0:
            print(x)
    
    for i in range(5):
        if list_of_five[i] % 2 == 0:
            print(list_of_five[i])

the_int = int(input('Number! '))

count = 0
while the_int != 1:
    the_int //= 2
    count += 1

print("You can divide 8 by 2:  {} times.".format(count))
