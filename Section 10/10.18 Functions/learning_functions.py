"""
    What is a function?
        "call a function" - tell the function to execute

    What are the parts of a function?
    
"""


# signature requires 3 variables to be input
def compute_volume(x, y, z):
    # print(x * y * z)
    return x * y * z


# signature of the function
# see the parameter list (just an integer)
# anything that is inside of a function is "local scope"
def is_perfect(an_int):
    # banned because it's dangerous
    # global the_sum
    
    the_sum = 0
    for i in range(1, an_int):
        if an_int % i == 0:
            the_sum += i
    
    if the_sum == an_int:
        print('It is perfect')
        # as soon as you hit this return, the function ends
        return True
    else:
        print('nope')
    
    # unreachable because it's after the return statements
    print(the_sum)
    # right here an_int and the_sum (the local one) go away
    return False


def get_books():
    book_list = []
    s = input('Tell me a book or (quit): ')
    while s != 'quit':
        book_list.append(s)
        s = input('Tell me a book or (quit): ')
    return book_list


def get_day_of_november(day):
    the_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return the_days[day % 7]


def is_prime(n):
    for i in range(2, int(n ** (1 / 2) + 1)):
        if n % i == 0:
            return False
    
    return True


def factor_me(n):
    prime_list = []
    for i in range(2, 50):
        if is_prime(i):
            prime_list.append(i)
    
    factor_list = []
    for prime in prime_list:
        while n % prime == 0:
            factor_list.append(str(prime))
            n //= prime
    
    return factor_list


if __name__ == '__main__':
    the_sum = 0
    # global scope
    the_int = int(input('What int do you want to check? '))
    # is_perfect(the_int)
    print(is_prime(the_int))
    print('*'.join(factor_me(the_int)))
    print('after the function', the_sum)
    # print(an_int, the_sum)
    if False:
        the_volume = compute_volume(5, 2, 7)
        print(the_volume)
    # this will cause a TypeError because compute_volume needs 3 arguments, not 2
    # compute_volume(2, 2)
    # also a problem
    # the_volume = compute_volume(5, 2, 7, 5, 4, 2, 2)
    
    
        # book_list goes nowhere it dies :(
        my_book_list = get_books()
        for x in my_book_list:
            print('A book called: {}'.format(x))
        
        another_list = get_books()
        print(another_list)
    
    d = int(input('What number of day is it? '))
    while d != 0:
        print(get_day_of_november(d))
        d = int(input('What number of day is it? '))
