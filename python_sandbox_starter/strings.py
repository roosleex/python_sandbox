# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'rus'
age = 36



# String Formatting

#concatenate
print('Hello, my name is ' + name + '. I am ' + str(age) + ' years old')

#arguments by position
print('Hello, my name is {name}. I am {age} years old'.format(name=name, age=age))

#f-strings (3.6+)
print(f'Hello, my name is {name}. I am {age} years old')



# String Methods
s = 'hello world!'
print(s.capitalize())
print(s.upper())
print(s.lower())
print(len(s))