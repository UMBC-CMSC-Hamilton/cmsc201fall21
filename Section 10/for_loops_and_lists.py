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

"""
for some_index in range(start, stop, step):
    do something here

I want to compute the Fibonacci numbers

Start at 1, 1
Add two previous numbers
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
5 + 8 = 13
8 + 13 = 21
13 + 21 = 34
...

1, 1, 2, 3, 5, 8, 13, 21, 34
"""
current = 1
previous = 1
before_that = 1

fib = int(input('What Fibonacci number do you want? '))

# sqrt(5) ** n
for i in range(fib - 2):
    current = previous + before_that
    # update the previous and the before_that
    before_that = previous
    # set before_that before we overwrite previous
    previous = current
    
print(current)

