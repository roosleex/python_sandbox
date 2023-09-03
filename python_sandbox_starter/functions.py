# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

#create function
def say_hello(name):
    print(f'Hello {name}')

say_hello('world')   



#create function
def say_hello_default(name='user'):
    print(f'Hello {name}')

say_hello_default()   



def get_sum(num1, num2):
    total = num1 + num2
    return total

num = get_sum(3, 4)
print('sum = ' + str(num))



# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

get_sum = lambda num1, num2: num1 + num2
print('sum = ' + str(get_sum(4, 6)))