#1 Используя функцию map() переписать функцию
#items = [1, 2, 3, 4, 5]
#squared = []
#for i in items:
#    squared.append(i**2)

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)


#2 Используйте функцию reduce() и перепишите код
#product = 1
#list = [1, 2, 3, 4]
#for num in list:
#    product = product * num

from functools import reduce
last = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, last)
print(product)

#3 Используйте функцию map() и перепишите код
#numbers = [1, 2, 3, 4, 5]
#squared = []
#for num in numbers:
#       squared.append(num ** 2)
#print(squared)


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

#4 Объедините списки x = [1, 2, 3] и y = [4, 5, 6] с помощью функции zip()
x = [1, 2, 3]
y = [4, 5, 6]
zipped = list(zip(x, y))
print(zipped)

#5 Используйте функцию zip() чтобы преобразовать код:
name_hero = [
    'Hulk',
    'Mr. Fantastic',
    'Invisible Woman',
    'Doctor Strange',
    'Doctor Octopus',
    'Spider-Man',
]

name_real = [
    'Bruce Banner',
    'Reed Richards',
    'Sue Storm',
    'Stephen Strange',
    'Otto Octavius',
    'Peter Parker',
]

for hero, real in zip(name_hero, name_real):
    print(hero, '-', real)


#6 С помощью функции filter() переместите из списка numbers = [1, 2, 4, 5, 7, 8, 10, 11] нечетные элементы в новый список.

numbers = [1, 2, 4, 5, 7, 8, 10, 11]
# Используем функцию filter() для выбора нечетных чисел
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)















