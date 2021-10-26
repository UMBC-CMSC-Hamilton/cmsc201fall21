"""
    What is a dictionary?
    
    --> # <-- what is this thing?  octothorpe, pound sign,
        hash tag

        What is a hash?
"""

# curly braces?
my_first_dictionary = {}
# dict constructor
my_other_dictionary = dict()

# my_list[3] = 'hi'

my_first_dictionary['hi'] = 17
my_first_dictionary['byte'] = 8
my_first_dictionary['pi'] = 3.14
my_first_dictionary['cool'] = 1729
my_first_dictionary['least cool'] = 3
print(my_first_dictionary)
#print(my_first_dictionary[1729])
my_first_dictionary[14] = 'robots attack'
my_first_dictionary[8.88] = 'eight point eight eight'
print(my_first_dictionary)
# why do keys have to be immutable?
# what if they weren't?

"""
    a hash table - what dictionaries are made of
"""

my_explicit_dictionary = {2: 5, 3: 7, 4: 17}
my_other = {4: 'hello', 17: 'congestion', 19: 'shoes'}
print(my_other[4], my_other[17], my_other[19])
my_other[4] = 'the terminator'
print(my_other)
# key values are unique

# keys MUST MUST MUST be immutable
# values can be whatever
people_map = {12: ['Eric', 'sushi'], 17: ['Sean', 'steak with peppers and mushrooms'], 445: ['Bob', 'vegan'], 654: ['Alice', 'vindaloo'], 432: ['Eve', 'apple']}

for ssn in people_map:
    print(ssn)
    print(people_map[ssn])
    print('Favorite Food', people_map[ssn][1])

pyopoly_map = {'Park Place': {'value': 350, 'color': 'dark blue'},
               'Baltic Ave': {'value': 60, 'color': 'purple'},
               'Marvin Gardens': {'value': 220, 'color': 'yellow'}}

for property in pyopoly_map:
    print(property, pyopoly_map[property]['value'])
