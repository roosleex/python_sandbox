# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

#create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}
print(person, type(person))
print(person['first_name'])
print(person.get('last_name'))

#add key/value
person['phone'] = '555-555-5555'
print(person)

print(person.keys())
print(person.items())

person2 = dict(first_name='John', last_name='Doe')
print(person2, type(person2))

#copy dict
person3 = person.copy()
person3['city'] = 'Kyiv'
print(person3)

#remove item
del(person3['city'])
print(person3)

#remove item
person3.pop('phone')
print(person3)

#length
print(len(person3))

#clear items
person3.clear()
print(person3)



#list of dictionaries
people = [
    {'name': 'Maria', 'age': 25},
    {'name': 'Alex', 'age': 27}
]
print(people)
print(people[1]['name'])




