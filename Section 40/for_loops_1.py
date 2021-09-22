"""
    print / input
    variables
    arithmetic/algebra
    if statements (elif, else)
    for loops <-- code that repeats
"""
if False:
    # i is the index of the loop, dummy variable, loop variable
    for i in range(10):
        print(i)
        
    # lists next time
    
    endpoint = int(input('How many times do you want to loop? '))
"""
the_sum = 0
for j in range(endpoint + 1):
    the_sum += j

the_sum = endpoint
for j in range(endpoint):
    the_sum += j
"""
if False:
    the_sum = 0
    for j in range(endpoint):
        the_sum += j + 1
    
    print(the_sum)
    
    # what is a factorial?
    endpoint = int(input('How many times do you want to loop? '))
    factorial = 1
    for k in range(1, endpoint + 1):
        factorial *= k
        
    print(factorial)
    
    
    # fibonacci numbers
    which_fib = int(input('Which fibonacci number do you want to calculate? '))
    previous_fib = 1
    previous_previous_fib = 1
    current_fib = 1
    for i in range(2, which_fib):
        current_fib = previous_fib + previous_previous_fib
        print(current_fib, previous_fib, previous_previous_fib)
        previous_previous_fib = previous_fib
        previous_fib = current_fib
        
    print(current_fib)


# a prime number is divisible by 1 and itself (only)
# 4 = 2 * 2
# 5 = 1 * 5? no other factorization

test_int = int(input('What number do you think is prime? '))

is_prime = True
# skip 0 because of division by zero, skip 1 because everything is div by 1
for i in range(2, test_int):
    if test_int % i == 0:
        # print(i, 'not prime')
        is_prime = False

if is_prime:
    print('it is prime')
else:
    print('it is not prime')
