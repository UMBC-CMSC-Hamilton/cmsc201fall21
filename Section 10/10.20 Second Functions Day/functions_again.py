"""
    Declaration of the function
    def [name of function] [parameters]
    
    Yes you must fill out all the parameters/arguments of a function
    
"""


def grade_exams(exam_list):
    for x in exam_list:
        if not x.is_graded():
            x.grade()


# things like radius are the 'parameters'
def compute_circle_area(radius):
    return 3.14 * radius ** 2


# things that get plugged in, like 5 are "arguments"
print(compute_circle_area(5))
my_var = int(input('Tell me a radius: '))
print(compute_circle_area(my_var))


# TypeErrors "positional arguments required"
# compute_circle_area()
# too many positional arguments
# compute_circle_area(5, 10, 15, 20)

# ideas -> working code
# logic bugs, syntax error
# IDEs take time off from error checking

def count_the_as(my_string):
    count = 0
    for c in my_string:
        if c.lower() == 'a':
            count += 1
    return count


# if you don't use a variable to 'take' the value of the return then it's lost
# because it doesn't have a name anymore
a_count = count_the_as('aabaaacaaaaaadedadadadda')
# return is not print
print(a_count)

"""
    Philosophy - rather than rules
    
    functions that don't have inputs generally don't need prints either
        unless the function is "display_thing(thing)"
        always try to return the answer
"""


def lots_of_strings(string_list):
    total_as = 0
    for the_string in string_list:
        total_as += count_the_as(the_string)
    return total_as


my_list = []
s = input('Tell me thing: ')
while s != 'stop':
    my_list.append(s)
    s = input('Tell me thing: ')

print(lots_of_strings(my_list))

"""
    Why function is better than copy-pasted or slightly modified code
    
    All the functionality is in one place.
        You only have to test one thing to make sure it works.
        If you have to make a change, you make the change once...
        
"""

"""
    Remember mutability.
    
    A variable can be changed.
    
    Some local variables in functions don't change the outside variable/value
    Some of them do...
        Entirely dependent on type
        
    int, bool, float, string are all passed by "value"
        the function makes a copy of the original variable
        we can only modify the copy
        
    lists, [dictionary, classes] - mutable which means they can be changed.
        When you pass them into a function, they can actually change.
        "pass by 'reference'"
"""


def square_the_number(x):
    x **= 2
    print('inside', x)
    return x


x = 15
square_the_number(x)
print('outside', x)


def modify_the_string(my_string):
    my_string += ' is happy'
    print(my_string)
    return my_string


eric_name = 'Eric'
modify_the_string(eric_name)
print(eric_name)

"""
    Do we expect the global variable to change?

        int, string, float, bool are all ->IM<-MUTABLE
        
        This all behaves like what i described with regard to local/global

        passing by value == 'deep copy' (an actual copy)
        
    Now let's look at lists
"""

"""
    my_list is a list, then it is not a copy
        "shallow copy" (not a copy)
        Just a "renaming"
"""


def add_a_bunch_of_ones(my_list, k):
    for i in range(k):
        my_list.append(1)
    
    print(my_list)
    # not even going to return my_list, definitely not,


big_list = [1, 2, 3, 4, 5]
add_a_bunch_of_ones(big_list, 5)
print(big_list)


def do_something(x, y):
    x.append(15)
    y += 5


listy_list = [5, 4, 3, 2, 1]
my_global_y = 17
do_something(listy_list, my_global_y)
print(listy_list, my_global_y)


my_ascending_list = []
a_number = int(input('Enter a number: '))

first_go = True

while first_go or a_number > my_ascending_list[len(my_ascending_list) - 1]:
    first_go = False
    my_ascending_list.append(a_number)
    a_number = int(input('Enter a number: '))

print(my_ascending_list)


def what_i_saw():
    my_ascending_list = []
    a_number = int(input('Enter a number: '))
    
    first_go = True
    keep_going = True
    
    while first_go or keep_going:
        first_go = False
        my_ascending_list.append(a_number)
        a_number = int(input('Enter a number: '))
        if a_number < my_ascending_list[len(my_ascending_list) - 1]:
            keep_going = False
    
    print(my_ascending_list)
