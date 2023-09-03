# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 1 #int
y = 2.5 #float
name = 'John' #string
name2 = "John" #string
is_cool = True #bool

#multiple assignment
x, y, name, is_cool = (1, 2.5, 'John', True)

print(x)
print(x, y, name, is_cool)

#basic math
res = x + y
print(res)

#get type
print(type(res))

#casting to string
res = str(res)
print(type(res))

#casting to int
res = int(x)
print(type(res))

#casting to float
res = float(res)
print(type(res))