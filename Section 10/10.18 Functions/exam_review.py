the_int = int(input('What int do you want to check? '))

the_sum = 0
for i in range(1, the_int):
    if the_int % i == 0:
        the_sum += i

if the_sum == the_int:
    print('It is perfect')
else:
    print('nope')
