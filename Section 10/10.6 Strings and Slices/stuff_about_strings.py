"""
    Compare and Contrast:
        Strings:
            Specifically characters
            Immutable - cannot be changed (creates copies of that string)
                Strip a string, the original is unmodified.
                New version of that string which has the whitespace removed.
        Lists:
            Anything can be stored in lists
            Mutable - can be changed (.append(), .remove(), del)
            
        Both:
            Index <-- they work the same for both
            
"""

"""
    String slices, list slices

    Special to Python, Ruby

    A slice is a substring that we get by index
        we need two indices to specify a slice
"""
if False:
    a_string = "hello, I am very much a string"
    
    print(a_string[0: 5])
    
    print(a_string[7: 14])
    
    the_big_string = input('Tell me a string: ')
    the_little_string = input('Tell me yet another string: ')
    
    if the_little_string in the_big_string:
        print('it is in there')
    else:
        print('nope')
    
    for i in range(len(the_big_string)):
        if the_little_string == the_big_string[i: i + len(the_little_string)]:
            print(i, 'found it')
        
        
    test_string = 'abcdefghi'
    # yes it prevented an error, but also you didn't get a string of the length
    # you expected
    print(test_string[7:1000])
    # we will never require you to use negative steps in slices
    print(test_string[8:3:-3])
    
    
    a_palindrome_maybe = input('tell me a potential palindrome: ').strip().lower()
    
    print(a_palindrome_maybe[len(a_palindrome_maybe) - 1::-1])
    
    if a_palindrome_maybe == a_palindrome_maybe[::-1]:
        print('yes it is')
    else:
        print('no its not')
    
    a_list = [
        'bread',
        'eggs',
        'milk',
        'dog',
        'cat',
        'ground beef',
        'stupid'
    ]
    
    print(a_list[2:5])
    
