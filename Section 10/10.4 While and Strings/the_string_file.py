if False:
    my_string = input('Tell me a story: ')
    
    # a string is iterable, "next object" gives characters
    #   if you put it in a for-each loop
    count = 0
    for c in my_string:
        if c.lower() == 'a':
            print('we found an a')
            count += 1
        print(c)
        
    print(count)
    
    """
        strip()
            - removes whitespace from the beginning and end of the string
        split()
             - split on a separator or on whitespace if no sep is given.
        join()
             - join a list back into a string
    """
    
    
    # whitespace = tab, newline, carriage return, spaces
    my_favorite_string = '\t\r\t\t\n\n\nHello there\t\t\n   \n   \n\t '
    # only deletes whitespace from the outside of the string not from the "middle"
    print(my_favorite_string, end='Z\n')
    
    # this doesn't change the original string
    print(my_favorite_string.strip(), end='Z\n')
    
    # here's proof the original string is not changed
    print(my_favorite_string, end='a')
    # string are "immutable" - unchangeable
    print()

if False:
    my_string_list = 'abcdef'
    print(my_string_list[2])
    # item assignment : my_string_list[index] = 'something' doesn't work
    my_string_list[2] = 'r'
    print(my_string_list)

    # python only gets "interpreted" as it runs
    # compiled languages get changed into machine code
    # python gets changed into python byte code which is run by python.exe/python3


"""
    split() - creates a list from the string, separates based on whitespace
"""
if False:
    new_list = []
    it_split = input('Tell me a string').split('it')
    for whatever in it_split:
        comma_split = whatever.split(',')
        for the_string in comma_split:
            new_list.append(the_string)
            
    print(new_list)
    
    
    my_list = []
    s = input('Tell me s: ')
    while s.lower() != 'quit':
        my_list.append(s)
        s = input('Tell me s: ')
    
    separator = input('Tell me the separator: ')
    
    print(separator.join(my_list))

"""
    palindrome
    
    racecar
    tacocat
    gnudung
    a man a plan a canal panama
"""

test_pal = input('Tell me a palindrome')
# smashes everything together
test_pal = ''.join(test_pal.lower().split())
print(test_pal)

is_pal = True
for i in range(len(test_pal)):
    if test_pal[i] != test_pal[len(test_pal) - 1 - i]:
        is_pal = False

print(is_pal)
