"""
    What is a dictionary?
    
        Generally what is this symbol called in the modern age?
         --> # <-- pound not that one, hash tag
         
         I was totally wrong about everything
         
         everybody says the word hash-tag

        there was a special kind of list
        
        it used indexing like old lists, so in that sense it's good
        
            you can use any 'immutable' type as the index -> key
        
"""

my_dictionary = {}
my_other_dictionary = dict()

my_dictionary['hello'] = 5
my_dictionary['goodbye'] = 17
my_dictionary['robot attack'] = 57
print(my_dictionary)

print(my_dictionary['hello'])

my_dictionary[3.14] = 'pi'
my_dictionary[17289] = 'what?'
# immutable = string, float, int, bool
print(my_dictionary)

print(my_dictionary.keys())
# keys are unique
my_dictionary['hello'] = 12
print(my_dictionary)


grades = {}

grades['Eric'] = [100, 24, 12, 1314,23]
grades['Sammie the TA'] = [100, 43,54, 65, 76]
grades['Sean Jordan'] = [100, 12, 23, 45, 56, 670]
print(grades)

pyopoly_board = \
    {'Park Place': {'value': 350, 'owner': 'Robert', 'color': 'dark blue'}
    , 'Baltic Ave': {'value': 60, 'owner': None, 'color': 'purple'}}

print(pyopoly_board['Baltic Ave']['value'])
