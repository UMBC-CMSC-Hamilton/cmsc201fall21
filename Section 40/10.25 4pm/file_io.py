# by default this will open in read mode
# file object is returned
"""
    No mode, default mode is read not write
        don't accidentally delete everything
"""
my_file = open('test_file.txt')

for the_line in my_file:
    # secretly doing this:
    # the_line = my_file.readline()
    # print(the_line.strip())
    # newlines are coming from the file not from the print function
    print(the_line, end='')

my_file.close()

my_file = open('test_file.txt')
print(my_file.readline(), end='')
print(my_file.readline(), end='')
my_file.close()

# don't call a read on a closed file
# print(my_file.readline(), end='')

my_file = open('test_file.txt')
print(my_file.readlines())

print(my_file.readline(), end='hi')
my_file.close()

"""
    for loop (secretly doing readline())
    file.readline() - string
    file.readlines() - List of strings
    file.read() - string (entire file at once)
"""

my_file = open('test_file.txt')
print(my_file.read())
my_file.close()
"""
 Garbage:
import random
import string

# note that the 'w' means write mode
big_file = open('my_big_file.txt', 'w')
for i in range(200000):
    big_file.write(''.join([random.choice(string.ascii_lowercase) for _ in range(100)] + ['\n']))

big_file.close()

print('file made, read starting')
big_file = open('my_big_file.txt', 'r')
big_file.read()
print('read complete')

"""

my_input_file = open('write_test.txt', 'w')

s = input('tell me: ')
while s != 'quit':
    # just remember that you need a new line here
    my_input_file.write(s + '\n')
    s = input('tell me: ')

my_input_file.close()

"""
The other write command is writelines

remember that open(file, 'w') this will blank the file

set it to size = 0



"""

my_input_file = open('write_test.txt', 'w')
my_input_file.writelines(['able', 'baker', 'charlie', 'dog'])
my_input_file.close()

"""
append mode is write mode... EXCEPT it doesn't blank the file out
it will move the cursor to the EOF = end of file
"""
my_input_file = open('write_test.txt', 'a')

s = input('tell me: ')
while s != 'quit':
    # just remember that you need a new line here
    my_input_file.write(s + '\n')
    s = input('tell me: ')

my_input_file.close()

