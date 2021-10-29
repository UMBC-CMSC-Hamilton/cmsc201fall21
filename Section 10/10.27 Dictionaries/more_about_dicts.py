"""
    What is a dictionary?
        
        Hash Map or a Hash Table

    How do you declare one?

"""

new_dict_1 = dict()
new_dict_2 = {}


"""
key: value
key's are immutable - int, bool, string, float (avoid)
                    None, datetime <-- oddly enough

values can be "whatever" - immutable or mutable types
        they can even be lists or dictionaries themselves
"""
new_filled_dictionary = {'hello': 17, 'urban': 3, 'considerate': 381,
                         'love': 999, 'hate': 433, 'for': None}

# way to access a dictionary is the index operator:
print(new_filled_dictionary['hello'])

# is there a way to "fix this?"
#
# print(new_filled_dictionary['zebra'])
if 'zebra' in new_filled_dictionary:
    print(new_filled_dictionary['zebra'])
else:
    print('it wasn\'t there')

"""
    .get() will not result in KeyErrors, it will return None
        or whatever second argument you pass into the function
"""
print(new_filled_dictionary.get('love'))
# not in the dictionary returns None
print(new_filled_dictionary.get('zebra', ['x', 'y']))
# it was in the dictionary but the value was None
print(new_filled_dictionary.get('for', -1))

for my_key in new_filled_dictionary:
    print(my_key, new_filled_dictionary[my_key])
    new_filled_dictionary[my_key] = 'robot'


print(new_filled_dictionary)
"""
    list vs dict?
    
    do i want to associate the key with the value?
    
        no - list
    
        yes - name -> phone number, address, grades, something else about that person
            use dictionary
"""

even_newer_dict = {'aab': 14, 'aac': 12, 'aaa': 1, 'aba': 13}
# basically a list,
print(even_newer_dict.keys())
print(list(even_newer_dict.keys()))

print(list(even_newer_dict.values()))

book_map = {'Dune': {'pages': 532, 'author': 'Frank Herbert'},
            'Harry Potter': {'pages': 450, 'author': 'J.K. Rowling'},
            'Hunger Games': {'pages': 321, 'author': 'Suzanne Collins'},
            'The Giver': {'pages': 777, 'author': 'Lois Lowery'}}

print(book_map.keys())
print(book_map.values())

print(book_map['The Giver']['pages'])
book_map['The Giver']['pages'] = 381
print(book_map['The Giver']['pages'])

for book_name in book_map:
    print(book_name, book_map[book_name])

# TypeError unhashable type
# print(book_map[{'pages': 532, 'author': 'Frank Herbert'}])

"""
    What does hash mean?
        shredded
        
    A dictionary is secretly a list
        indices are determined by some kind of function
        string -> converts it into some kind of number
"""

def fake_hash(a_string):
    hash = 0
    prime = 41
    for i in range(len(a_string)):
        # ord gives the ascii / unicode value
        hash += ord(a_string[i]) * prime ** i
    
    return hash

s = input('tell me a string to fake hash')
while s != 'quit':
    print(fake_hash(s))
    s = input('tell me a string to fake hash')
