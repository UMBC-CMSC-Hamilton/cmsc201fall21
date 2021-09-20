"""
    print/input
    variables
    if statements
        no control of program flow.
    nothing currently repeats... is there a way to repeat things?
        yes...
"""

# i can be called index variable, loop var, dummy var
"""
    In computer science*, indexing starts at zero.
        range(n) gives us 0, 1, 2, 3, 4, ... (n - 1)
        Never includes the endpoint at the top.
    
    * = 99% of the time
"""
if False:
    # Add up all numbers from 1 to n.
    endpoint = int(input('How high do we need to add? '))
    total = 0
    for i in range(endpoint):
        # total = total + i
        total += (i + 1)
        # start at i = 0 ,i + 1 = 1
        # end at endpoint - 1 + 1 = endpoint
        # that's right
    
    print(total)
    # 1 + 2 + 3 + 4 + 5 = 6 + 6 + 3 = 15, not right. :(
    
    total = 0
    for i in range(endpoint + 1):
        # total = total + i
        total += i
        print(i, total)
    
    # range(start, end) start, start + 1, start + 2, start + 3, ..., end - 1
    for i in range(2, 9):
        print(i)
    
    # 0, 1, 2, 3, ... 9 there are actually 10 numbers in this group
    for j in range(10):
            print(j)
    
    count = 0
    for index in range(7, 27):
        count += 1
    
    print(count)
    
    # don't use the variable outside of the loop, it will probably cause you issues
    print(index)
    
    stop = int(input('tell me the stop: '))
    for index in range(stop):
        print(index)

    # range(start, stop, step)
    for index in range(5, -1, -1):
        print(index)
    
    for no_go in range(17, 2, 5):
        print(no_go)
    
    # all things in range must be integers
    for index_2 in range(3, 22, 2):
        print(index_2)
    

prime_test = int(input("what do you want to test for primality? "))
# prime checker
# i started at 2 because you can't mod by zero, it's the same as dividing by zero.
# why can't you start at 1? because the remainder whatever/1 = whatever R 0

# sentinel variable
watch_stander = True

for i in range(2, prime_test):
    if prime_test % i == 0:
        watch_stander = False

if watch_stander:
    print('It was prime')
else:
    print('It was composite')

