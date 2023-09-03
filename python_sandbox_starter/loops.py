# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

print('=========== FOR =============')

people = ['John', 'Paul', 'Sara', 'Susan']

for person in people:
    print(f'Current person: {person}')

print('========================')

for person in people:
    if person == 'Sara':
        break
    print(f'Current person: {person}')

print('========================')

for person in people:
    if person == 'Sara':
        continue
    print(f'Current person: {person}')

print('========================')

#range
for i in range(len(people)):
    print(f'i={i}')

print('========================')

#range
for i in range(len(people)):
    print(f'people[{i}] = {people[i]}')

print('========================')

#range
for i in range(0, 10):
    print(f'i={i}')

print('========================')



# While loops execute a set of statements as long as a condition is true.

print('=========== WHILE =============')

i = 0
while i <= 10:
    print(f'i = {i}')
    i += 1

print('========================')