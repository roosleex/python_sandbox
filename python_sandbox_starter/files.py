# Python has functions for creating, reading, updating, and deleting files.

#open a file
my_file = open('myfile.txt', 'w')

#get some info
print('Name: ', my_file.name)
print('is closed: ', my_file.closed)
print('opening mode: ', my_file.mode)

#write to a file
my_file.write('I love python')
my_file.write('and some other languages')
my_file.close()



#append to a file
my_file = open('myfile.txt', 'a')
my_file.write('and also candies')
my_file.close()



#read from a file
my_file = open('myfile.txt', 'r+')
text = my_file.read(100)
print(text)
my_file.close()