dog_names = ['pupper']

# 'Thor' in dog_names and 'Loki' not in dog_names
print('Thor' in dog_names and 'Loki' not in dog_names)

name = 'THIS IS A STRING STOP YELLING'

print(name == name.upper())

"""
ye olde chart

0 0000  4 0100  8 1000  C 1100
1 0001  5 0101  9 1001  D 1101
2 0010  6 0110  A 1010  E 1110
3 0011  7 0111  B 1011  F 1111

80d -> hex easy
hint: 5 * 16 = 80

while the_num != 0:
    the_digit = the_num % 16
    the_num //= 16

80 % 16 = 0
80 // 16 = 5
next step:
5 % 16 = 5
5 // 16 = 0

hex = 0x50

80 (even)-> 40 (even) -> 20 (even) -> 10 (even) -> 5 (odd) -> 2 (even)
-> 1 (odd) -> 0
binary = 0101 0000

211 -> binary first
211 // 16 ? 13
211 mod 16 ? 3

211 odd-> 105 odd -> 52 (even) -> 26 (even) -> 13 (odd) -> 6 (even)
-> 3 (odd) -> 1 (odd)
binary = 1101 0011
hex = 0xD3

1001 1001
0x99
16(9) + 9 = 16(10 - 1) + 9
128 + 16 + 8 + 1
153

0x8A57DF02
from table...
1000 1010 0101 0111 1101 1111 0000 0010

\\\nEnjoy break!\\\\

\
Enjoy Break!\\

Who_is__best? there are two of them together... __
"""

"""
hello(15) -> print('hello')
hello(7) -> print('hello')
hello(10) -> print('hello')
hello(2) -> print('hello')
hello(5) -> print('hello')
print(-3)
"""


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


def square_area(side_length):
    return side_length ** 2


if __name__ == '__main__':
    print(square_area(square_area(2)))

"""
[
    [ 0
        [201] 0,
        [202, 203] 1
    ],
    [
        [331, 341],
        [304, 313]
    ]
]
"""
threeD = [[[201], [202, 203]], [[331, 341], [304, 313]]]

print(threeD[0][0][0])  # 201
print(threeD[0][1][0])  # 202
print(threeD[1][0][1])  # 341


def func(first, second):
    if first <= 0:
        return -1
    if first == 1:
        return second
    return second + func(first - 1, second)


"""
    func(3, 9) = 9 + func(2, 9)
    func(2, 9) = 9 + func(1, 9)
    func(1, 9) = 9

    total = 27 = 9 + 9 + 9
"""

if __name__ == '__main__':
    ans = func(3, 9)
    print(ans)

if __name__ == '__main__':
    a = [1, 2]
    b = a
    b[0] += 3
    print(a)

if __name__ == '__main__':
    a = [1, 2]
    b = list(a)
    b[0] += 3
    print(a)

"""
5 missing parenthesis
5-6 swap these lines
8 sentence[i]
10 add return count
16 replace my_file with line_list
19 remove a tab
"""

"""
4 add my_list as a parameter
10 change to my_list[1:]
14 max_rest without [0]
16 add colon
18 the_list is not declared declare it there
19 while temp_val != 0:
23 recurMax should be recur_max
24 either you cast the list_max to string or change + into ,

"""


def is_power_2(the_num):
    if the_num == 0:
        return False
    
    if the_num == 1:
        return True
    
    if the_num % 2 == 0:
        return is_power_2(the_num // 2)
    
    return False


def create_2d_list(height, width, symbol):
    the_list = []
    
    for h in range(height):
        new_row = []
        for w in range(width):
            new_row.append(symbol)
        the_list.append(new_row)
    
    return the_list
