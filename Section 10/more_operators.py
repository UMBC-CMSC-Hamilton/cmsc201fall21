"""
    Operators

        Arithmetic (highest precedence - it goes first)
            (), +, -, *, /, //, %, **, NEVER ^
        Comparison (middle precedence - it goes after arithmetic)
            <, >, ==, <=, >=, != (not equals)
            (all comparisons are equal)
        Logical (logic always goes last)
            not happens first
            and, or - happen last
"""

a = 5
b = 2
c = 7
print(a > b and b < c)

print(a >= 5 or 'happy' == 'sad')

print((a == 4) or 6)
# operator precedence

# anything is true as long as it's not zero
if -5:
    print('hello there')

if 0:
    print('yep its also true')

if "but what about strings?":
    print('strings are ... true?')
    
if " ":
    print('space is true')

if "":
    print('empty string is true')

if "False":
    print("false is true")
    
if a == 4 or 6:
    print('4 or 6')

if a == 4 or a == 6:
    print('why do we have to do this?')

if a == (4 or 6):
    print('oh god...')
