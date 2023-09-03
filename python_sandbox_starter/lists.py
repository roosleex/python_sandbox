# A List is a collection which is ordered and changeable. Allows duplicate members.

#create list
numbers = [1,2,3,4,5,6,7]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

#use a constructor
numbers2 = list((1,2,3,4,5,6,7))

print(numbers, numbers2)

#get a value
print(fruits[1])

#length
print(len(fruits))

fruits.append('Mangos')
print(fruits)

fruits.remove('Grapes')
print(fruits)

fruits.insert(2,'Lemons')
print(fruits)

#remove 'Lemons'
fruits.pop(2)
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

#reverse sort
fruits.sort(reverse=True)
print(fruits)

fruits[0] = 'FirstFruit'
print(fruits)