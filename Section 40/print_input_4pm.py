print('stuff')
print("stuff")

print(17)
print(42)

print(3.14159265358979)
print(1.618)
print(6.9)
print(-8.75)
print(18.0)
# float = double high precision

print(True, False)
print(True * False)

"""
    Multi-line comment
        Python compiler/interpreter doesn't read this
    Data types:
        string - a "list" of characters / text / raw input
        integers - whole numbers, negative whole numbers, zero
        float - decimal points
        Boolean - True or False
        
        None
"""
print(None)

# single line comment

print("Python", "is", "a", "fun", "language")
# print("Python", "is", "a", "fun", "language", sep='a')
# you can print multiple types in the same print statement
print("hello there", 56, 1.618, True)

# you can concatenate
print("this is" + " " + "concatenation")

# casting allows us to convert between data types
print("hello my favorite number is: " + str(17))

"""
    What other kind of casting can we do?

    str -> int
    str -> float
    
    float->str
    int->str
    
    float->int
"""

print(int(3.14), int(3.99))

# value error, do not uncomment
# float("hello there")

print(float(57))

# save the result from input
# s = input()
# if you need to print it out
# print(s)

# print(input())

# other_string = input('Tell me an adjective: ')

an_integer = int(input('Tell me an integer: '))
print(type(an_integer))
a_floaty = float(input('Tell me as many digits of e as you know: '))

# non-typed language Python is a language without type specifiers required for each variable
# a language where you can assign new types to old variables
an_integer = "this is now a string"
print(an_integer)
print(5 * an_integer)


"""
    Variable Declarations
        Something we stick into ram
        RAM = Random Access Memory
            Every place in RAM has a numerical address
        Programming languages hide the addresses from us and use names instead
        
        Rules:
        
            1) Start with an underscore or letter (not number)
            2) only composed of uppercase, lowercase letters numbers and underscores
            
        lowercase letters separated by underscores (PEP8 style)
"""

A_sTrInG = 'this is a pretty cursed variable name'

__my_integer = 3

my_variable = 6
