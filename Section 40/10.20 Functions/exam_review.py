"""
An expression that evaluates to True if and only if the variable
has_coat is True and either the variable prob_rain is greater than 50% (0.5)
or prob_snow is greater than 25%.

An expression that evaluates to True if and only if all three of the conditions here are met:
the num_cats is greater than zero, the num_dogs is less than 20, and
the cat_name string is not empty.
"""

has_coat = True
prob_rain = 0.7
prob_snow = 0.2
# answer to 16
has_coat and (prob_rain > 0.5 or prob_snow > 0.25)

cat_name = 'Whiskers'
num_cats = 6
num_dogs = 1
#answer to 17
cat_name and num_cats > 0 and num_dogs < 20


"""
    Talk about:
    Explain why x < y and 4 is different from x < y and x < 4.
    
    1) 4 evaluates to true
    2) the second one compares x to 4
"""


my_list_of_nums = []
new_num = int(input('Tell me a number: '))
prev_num = -1

while new_num > prev_num:
    my_list_of_nums.append(new_num)
    prev_num = new_num
    new_num = int(input('Tell me a number: '))

print(my_list_of_nums)


n = int(input('Number! '))
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i

if total == n:
    print('perfect')
else:
    print('imperfect')
