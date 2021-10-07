"""
    
    Strings vs lists:
    
        Strings:
            immutable
                .strip()-> new string doesn't actually change the old string
            collections of characters
            
        Lists:
            made of "elements" int,float, bool, string, list, dict, class
            mutable
                (append, remove, del)
        Both:
            index into both.
            len(me)
            for each loop (both iterable)
                iterable - "exists a next thing"
"""
if False:
    my_range_object = range(1, 200000000)
    print('I made the range object', my_range_object)
    
    my_range_thing = range(1, 11)
    print(my_range_thing)
    my_list = list(range(1, 11))
    print(my_list)
    
    # fun errors will result:
    # print(list(my_range_object))
    
    a_string = "When in the course of human events, it becomes necessary for one people to dissolve..."
    
    print(a_string[5])
    
    # a substring has a start and an end
    
    # slice
    print(a_string[5: 17] + a_string[20:25])
    # start index up to but doesn't include the end index
    
    # must be a colon inside of a slice
    print(a_string[30: 77])
    
    list_of_five = [1, 2, 3, 4, 5]
    
    print(list_of_five[2:5])
    # python philosophy violation - no error here
    print(list_of_five[2:1000])
    
    big_string = input('Tell me a story: ')
    little_string = input('Find this word in the story: ')
    
    if little_string in big_string:
        print('it is there')
    else:
        print('it does not exist')
        
    
    # try to figure out how we can use slices to pretend to be in keyword
    
    count = 0
    for i in range(len(big_string) - len(little_string) + 1):
        print(big_string[i: i + len(little_string)])
        if little_string == big_string[i: i + len(little_string)]:
            print(i, 'it is here')
            count += 1
    
    print(count)
    
    palindrome_thing = input('tell me palindrome: ')
    # if you do this on your homework you will get a mega-zero
    if palindrome_thing == palindrome_thing[::-1]:
        print('it is')
    else:
        print('nope')

list_of_twenty = list(range(1, 21))
print(list_of_twenty[5:])

# slice_list[start: stop: step]
# no start, start = 0
# no stop, stop = len(slice_list)
# step = 1 by default
print(list_of_twenty[5::2])



