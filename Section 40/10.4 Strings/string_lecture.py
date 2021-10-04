"""

    strings are ordered collections of characters
    
"""

if False:
    s = input('Tell me a string: ')
    
    for char in s:
        print(char)
    
    for i in range(0, len(s), 2):
        print(s[i])
    
    """
        3 string operations today.
        strip
            removes whitespace from the beginning and the end of the string
        split
        join
    """
    
    story = input('Tell me a story: ')
    print(story.strip())
    
    five = int('   5    '.strip())
    floaty = float('   3.2   ')
    no_good_float = float('-asdf')
    
    print(five)
    
    the_string = input('Tell me something: ')
    # only looks for the separator no longer checks for whitespace
    print(the_string.split(','))
    
    print('\t\t\t\n\n\n    hello  \t\t\t\n\n\n\n goodbye'.split())
    
    split_list = []
    string_index = 0
    start_word = 0
    inside_word = False
    while string_index < len(the_string):
        if the_string[string_index] not in ['\t','\n', ' ', '\r']:
            if not inside_word:
                inside_word = True
                start_word = string_index
        else:
            if inside_word:
                inside_word = False
                temp_string = ''
                for i in range(start_word, string_index):
                    temp_string += the_string[i]
                split_list.append(temp_string)
        string_index += 1
        
    if inside_word:
        temp_string = ''
        for i in range(start_word, string_index):
            temp_string += the_string[i]
        split_list.append(temp_string)
    
    print(split_list)
    
    s = input('Strange split example: ')
    # print(s.split(''))
    # a list of string character is achieved by casting as a list
    print(list(s))
    
    print(s.split('it'))
    
    """
        split takes a string and makes a list
        join takes a list (of strings) and makes one big string
    """
    
    my_favorite_list = ['banana', 'watermelon', 'apple', 'usb', 'pen', 'pencil', 'turnip', 'ram']
    separator = input('Tell me a separator: ')
    print(separator.join(my_favorite_list))
    
    my_string = 'So Happy Together'
    my_letters = list(my_string)
    print(my_letters)
    print(''.join(my_letters))

"""
    What is a palindrome?
        a string that reads the same forwards and backwards
"""

is_pal = True
test_pal = input('Enter a palindrome: ')
for i in range(len(test_pal)):
    if test_pal[i] != test_pal[len(test_pal) - i - 1]:
        is_pal = False
        
print(is_pal)