# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

#create tuple
fruits = ('Apples', 'Oranges', 'Grapes') 
fruits2 = tuple(('Apples', 'Oranges', 'Grapes')) 

fruits3 = ('Apples')
print(fruits3, type(fruits3))

fruits4 = ('Apples',)
print(fruits4, type(fruits4))

print(fruits, fruits2)

print(fruits[1])

#error, the tuple is unchangeable!!!
#fruits[1] = 'Mango'

#delete tuple
#del fruits2
#fruits2 is not defined already
#print(fruits2)

print(len(fruits))



# A Set is a collection which is unordered and unindexed. No duplicate members.

#create a set
fruits_set = {'Apples', 'Oranges', 'Grapes'} 
print(fruits_set)

print('Apples' in fruits_set)

fruits_set.add('Grapess')
print(fruits_set)

fruits_set.remove('Grapess')
print(fruits_set)

#clear set
fruits_set.clear()
print(fruits_set)