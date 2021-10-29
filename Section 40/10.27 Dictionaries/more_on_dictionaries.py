"""
    What are dictionaries?
        They are Hash Maps or Hash Tables

        They are a data structure that associates keys with values
        
        you can use the index operator to access elements
            but it's more general than a list
            put in a string, float, int bool, None, datetime
"""

# all very bad
"""
list = [4, 5, 6]

int = 5

x = int(input('type an int'))

dict = {'a': 3}
print(dict)
"""

my_new_dictionary = {'a': 3, 'b': 31, 'c': 67, 'd': 5, 'e': 12, 'f': 2.7182818459}
print(my_new_dictionary)

print(my_new_dictionary['d'], my_new_dictionary['a'])

# insert something new (use the index operator)
my_new_dictionary['g'] = 15
print(my_new_dictionary)

# we can cycle/iterate through them with a for loop
for the_key in my_new_dictionary:
    # the_key is an 'element' of the dictionary
    # key not a value
    # we can access the values using the keys
    # we can change them
    print(the_key, my_new_dictionary[the_key])
    if the_key in ['c', 'd', 'e']:
        print('special')
    if my_new_dictionary[the_key] % 5 == 0:
        print(the_key, 'is zero mod 5')
    
    # my_new_dictionary[the_key] = 983287

print(my_new_dictionary)

# how do you delete an element from a dictionary?
del my_new_dictionary['f']
print(my_new_dictionary)

my_sample_dictionary = {'a': 1, 'b': 7, 'c': 1, 'd': 15, 'e': 13, 'f': 1}
print(my_sample_dictionary)
del_list = []
for key in my_sample_dictionary:
    if my_sample_dictionary[key] == 1:
        del_list.append(key)
print(my_sample_dictionary)
for key in del_list:
    del my_sample_dictionary[key]
print(my_sample_dictionary)

print(my_sample_dictionary.keys())
print(my_sample_dictionary.values())
# if you ever feel fear that a dict_values, dict_keys may not be a list
print(list(my_sample_dictionary.keys()))
# don't use it because if you need it, you probably only needed a list
print(list(my_sample_dictionary.values()))

my_sample_dictionary.keys()

book_map = {'Hunger Games': {'author': 'Suzanne Collins', 'pages': 456},
            'The French Lieutenant\'s Woman': {'author': 'who cares', 'pages': 800000},
            'All Quiet on the Western Front': {'author': 'Eric Remark', 'pages': 400000},
            'There There': {'author': 'Tommy Orange', 'pages': 200}
            }

for book_name in book_map:
    print(book_name, book_map[book_name]['pages'])