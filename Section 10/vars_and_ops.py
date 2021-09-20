"""

    4 + 1 data types
    
        integer - whole numbers, negatives of whole numbers, zero
        float - things with decimal points
        bool - True or False
        string - a sequence of characters
        
        None

Let's talk about variables first...

What is a variable?
    A named slot where you can store data.
        storage goes into RAM
    variables values can change

Literals = hard coded values
"""

# first assignment IS the declaration
# declaration is telling Python that you want a specific name to have a
#   variable attached
# you don't need to specify the type of variable, python figures that out.
x = 4
y = x

# LHS needs to be "simple" 1 variable name
z = 12
# z + 5 = 17

print(x)

y = 2
x = 5 + y

print(x)

# python not a typed language

x = "i am an integer"
print(x)
x = 7.2
x = True

"""
    Operators
        
        Arithmetic
            (), +, -, *, /, //, %, **, NEVER ^
        Comparison
            <, >, ==, <=, >=, != (not equals)
        Logical
            and, or, not
"""

print(2 ** 4)
# this is non-standard but in Python, ** == power
x = 3
y = 5
print(x ** y)

#sqrt == 1/2 power also 0.5
print(5 ** (1/2))

if False:
    # / vs //
    print(5/2, 5//2)
    num = int(input('Tell me numerator: ' ))
    denom = int(input('Tell me denominator: ' ))
    print(num/denom, num // denom)
    # mod short for modulus, it's basically the remainder
    print(num % denom)

a = int(input('tell me a: '))
b = int(input('tell me b: '))

print(a == b, a < b, a > b, a <= b, a >= b, a != b)

print("hello" == "hello", "hello" == "HELLO")

s = input('go or quit: ')
print(s.lower() == 'quit')

# "alphabetical" = lexicographic
print("apple" < 'blueberry')
print("aardvark" > "apple")

