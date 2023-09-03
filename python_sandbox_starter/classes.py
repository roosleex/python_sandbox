# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# create class
class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

#extend class
class Customer(User):
    #constructor
    def __init__(self, name, email, age, balance):
        self.name = name
        self.email = email
        self.age = age
        self.balance = balance

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


#init user object
brad = User('Brad Simons', 'test@test.com', 40)
print(type(brad))
print(f'brad.name = {brad.name}')
print(brad.greeting())

#init a customer object
lisa = User('Lisa Gilmort', 'testlisa@test.com', 20)
lisa.set_balance(100)
print(type(lisa))
print(f'lisa.name = {lisa.name}')
print(lisa.greeting())