dog_names = ['pupper']

print('Thor' in dog_names and 'Loki' not in dog_names)
# dog_names.get('Thor', 'No God Here')

name = "IAMVERYANGRY"

another = 'helloiamastring'

name == name.upper()  # nice

"""
while current != 0
    next digit = Mod by the base
    divide by the base to get the new number

80d
16 * 5 = 80

80 % 16 = 0
80 // 16 = 5

5 % 16 = 5
5 // 16 == 0

0x50


0 0000
1 0001
2 0010
3 0011
4 0100
5 0101
6 0110
7 0111
8 1000
9 1001
A 1010
B 1011
C 1100
D 1101
E 1110
F 1111

80d = 50hex = 0101 0000b

211d -> bin
    1101 0011
    0xD3
105 odd -> 52 even -> 26 even -> 13 odd -> 6 even -> 3 odd

1001 1001
0x99
128 + 16 + 8 + 1 = 152 + 1 = 153


0101 1111
0x5F
64 + 16 + 8 + 4 + 2 + 1 = 95
geometric series -> sum^n 2^i = 2^{n + 1} - 1

8A57DF02
1000 1010 0101 0111 1101 1111 0000 0010

\\\nEnjoy break!\\\\
\
Enjoy Break!\\


"""

question = "Who_is_the_best_TA?"

print(question[: 7], end="")
print(question[10: 15], end="")
print(question[len(question) - 1])


def hello(count):
    if count < 0:
        return
    print("hello")
    if count % 5 == 0:
        hello(count - 8)
    else:
        hello(count + 3)


if __name__ == '__main__':
    hello(15)
"""

count(15)
count(7)
count(10)
count(2)
count(5)
count(-3)
"""


def square_area(side_length):
    return side_length ** 2


if __name__ == '__main__':
    print(square_area(square_area(2)))

threeD = [[[201], [202, 203]], [[331, 341], [304, 313]]]
print(threeD[0][0][0])
print(threeD[0][1][0])
print(threeD[1][0][1])

"""
func(3, 9)
9 + func(2, 9)
9 + 9 + func(1, 9)
9 + 9 + 9
 = 27
"""


def func(first, second):
    if first <= 0:
        return -1
    if first == 1:
        return second
    return second + func(first - 1, second)


if __name__ == '__main__':
    ans = func(3, 9)
    print(ans)

if __name__ == '__main__':
    a = [1, 2]
    # shallow copy (terrible name)
    # reference
    b = a
    # other version, deep copy = actual copy
    c = list(a)
    # b[0] += 3
    c[0] += 3
    print(a)

"""
Errors:

5   missing parenthesis
5-6 Flip these lines
8   sentence[i].upper()
10  add a return
16  my_file -> line_list
19  tab that output back

4 add my_list parameter
10 change 2-> 1 in the slice
14 remove index [0]
16 no colon there, add it
18 define the_list
19 temp_val != 0
23 change function name to actual name (accident)
24 cast list_max or whatever to string
"""


def is_power_of_two(the_num):
    # you don't need this one the actual exam because...
    # it says the_num is POSITIVE!!! :)
    if the_num == 0:
        return False
    
    if the_num == 1:
        return True
    
    if the_num % 2 == 0:
        return is_power_of_two(the_num // 2)
    
    return False


for i in range(100):
    print(i, is_power_of_two(i))


def create_2d_list(height, width, symbol):
    new_list = []
    
    for i in range(height):
        new_row = []
        for j in range(width):
            new_row.append(symbol)
        new_list.append(new_row)
    
    return new_list
    
    # new_list = [[symbol for _ in range(width)] for _ in range(height)]


print(create_2d_list(4, 3, '?'))

