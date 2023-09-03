# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 5

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

if x > y:
    print(f'{x} is greater than {y}')

a = 4
b = 5
if a > b:
    print(f'{a} is greater than {b}')
else:
    print(f'{b} is greater than {a}')

i = 5
j = 5
if i > j:
    print(f'{i} is greater than {j}')
elif i == j:
    print(f'{i} is equal to {j}')
else:
    print(f'{j} is greater than {i}')

#nested if
if x >= 10:
    if x < 20:
        print('Nested if is triggered')


# Logical operators (and, or, not) - Used to combine conditional statements

if i > 4 and j < 10:
    print(f'{i} > 4 and {j} < 10')

if i > 4 or j > 10:
    print(f'{i} > 4 or {j} > 10')

if not(i == x):
    print(f'{i} is not equal to {x}')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,10,5]
if x in numbers:
    print(f'{x} in {numbers}')

xx = 123
if xx not in numbers:
    print(f'{xx} not in {numbers}')

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

if i is j:
    print(f'{i} is {j}')

if i is not x:
    print(f'{i} is not {x}')