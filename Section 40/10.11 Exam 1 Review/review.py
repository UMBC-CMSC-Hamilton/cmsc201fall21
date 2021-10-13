test_list = [1, 2, 3, 4, 5]
for x in test_list:
    x *= 3

print(test_list)

for i in range(len(test_list)):
    test_list[i] *= 3

print(test_list)

index = 0

while index < len(test_list):
    test_list[index] *= 3
    # don't forget
    index += 1

print(test_list)

x = 5

if x % 2 == 0:
    print('x is even')

if not (x % 2):
    print('x is even')

found = False

for x in test_list:
    if x == 3:
        found = True

age = 17
height = 71

# answers don't need if don't declare the variables (assume that's been done)
not (age < 15) and height > 50
age >= 15 and height > 50

best_activities = []

len(best_activities) > 6 and best_activities[0] == 'nap' and \
'chicanery' not in best_activities

len(best_activities) >= 7 and best_activities[0] == 'nap' and \
'chicanery' not in best_activities

my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)):
    if my_list[i] % 2 == 0:
        # this is the important thing
        my_list[i] *= 3
print(my_list)

for i in range(10, 2, -2):
    print(i)

"""
line 8 - no len in the range
		for i in range(len(characters)):
line 9 - = is assignment not comparison
	SyntaxError
	    if i % 2 = 0: should be     if i % 2 == 0:
line 13 - no colon at the end of the line
	for j in range(len(characters))
		Missing colon very confused
line 14 - On this line, i == j is going to always compare the same
		'creature' with itself which is probably not what the programmer
		intended.
		
	            if i != j and j % 2 == 0:
line 20 - print statement missing
line 21 - first of two else statements, clearly we don't want that.
	replace the first else with elif p1_power < p2_power:
"""

L = []
for i in range(5):
    L.append(int(input('Enter a number ')))

for x in L:
    if x % 2 == 0:
        print(x)
        
the_number = int(input('Number! '))
count = 0
while the_number != 1:
    the_number //= 2
    count += 1

print(count)