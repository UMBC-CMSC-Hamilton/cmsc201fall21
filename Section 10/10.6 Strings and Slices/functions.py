"""
    What is a function?
                  _
        x |--->  |f| |---> f(x)
                  f(x) = x^2
        3 ----> |f| --> f(3) = 9
        
    In computer science, functions are even more powerful really...
    
    Run specific piece of code over and over, but can change the input each time
"""


# def something():
# def other_function(x, y, z):

def my_first_function(x):  # signature of the function
    print(x, x ** 2, x ** 3)


# jump to the definition of the function
# set the "parameters" in the function signature
my_first_function(2)

my_first_function(17)

my_first_function(31)

my_first_function(78438743)

# p1 = [a, b]
# p2 = [c, d]
def distance(p1, p2):
    # variables declared inside this function are called "local scope"
    # they only live as long as the function is currently running
    the_distance = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** (1/2)
    # print(the_distance)
    return the_distance


my_dist = distance([1, 2], [1, 8])
print(my_dist)
# print(the_distance)
# the_distance doesn't exist here, not a thing
the_dist = distance([-3, 7], [14, 1])
# doesn't have to be the same name as the returned variable
# not returning the variable name, it's returning the VALUE
print(the_dist)

# new problem, we're happy printing things but what if we want to save the distance?


def get_movies():
    my_list = []
    movie = input('Tell me your favorite movie or some other thing: ')
    while movie.strip().lower() != 'quit':
        my_list.append(movie)
        movie = input('Tell me your favorite movie or some other thing: ')
    return my_list


the_movie_list = get_movies()
print(the_movie_list)


def function_b():
    print('I am in function b now')
    my_var = 3
    print(my_var)

def function_a():
    print('I am in function a now')
    function_b()
    
def definitely_exists():
    print('i am here!')
    function_a()

definitely_exists()


print = 3
print('hello')
