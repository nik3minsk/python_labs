#
# ------------------------------------------------------------------------------------------
# 1.	Используя функцию map() переписать функцию
# --------------------------------------------------------------------------------------------
# items = [1, 2, 3, 4, 5]
# squared = []
# for i in items:
#     squared.append(i**2)
# print(squared)


# items = [1, 2, 3, 4, 5]
# squared = []
# def degree_2(x):
#     return x**2
# squared = list(map(degree_2, items))
#
# print(items)
# print(squared)
#



# ---------------------------------------------------------------------------------------------------
# 2.	Используйте функцию reduce() и перепишите код
# ---------------------------------------------------------------------------------------------------
# product = 1
# list = [1, 2, 90, 5]
# for num in list:
#     product = product * num
#

# from functools import reduce
# product = 1
# list = [1, 2, 90, 5]
#
# def multiply(a, b):
#     return a * b
#
# product = reduce(multiply,list)
# print(product)

# ------------------------------------------------------------------------------------------------------------
# 3.	Используйте функцию map() и перепишите код
# --------------------------------------------------------------------------------------------------------------
# numbers = [1, 2, 3, 4, 5]
# squared = []
# for num in numbers:
#        squared.append(num ** 2)
# print(squared)
#
#  ЗАДАНИЕ АНАЛОГИЧНО №1

# 4.	Объедините списки x = [1, 2, 3] и y = [4, 5, 6] с помощью функции zip()

# x = [1, 2, 3]
# y = [4, 5, 6]
#
# z = zip(x, y)
# print(list(z))
#
# 5.	Используйте функцию zip() чтобы преобразовать код:
#
# name_hero = [
#     'Hulk',
#     'Mr. Fantastic',
#     'Invisible Woman',
#     'Doctor Strange',
#     'Doctor Octopus',
#     'Spider-Man',
# ]
#
# name_real = [
#     'Bruce Banner',
#     'Reed Richards',
#     'Sue Storm',
#     'Stephen Strange',
#     'Otto Octavius',
#     'Peter Parker',
# ]
#
# for i in range(len(name_hero)):
#     print(name_hero[i], '-', name_real[i])

# name_hero = [
#     'Hulk',
#     'Mr. Fantastic',
#     'Invisible Woman',
#     'Doctor Strange',
#     'Doctor Octopus',
#     'Spider-Man',
# ]
#
# name_real = [
#     'Bruce Banner',
#     'Reed Richards',
#     'Sue Storm',
#     'Stephen Strange',
#     'Otto Octavius',
#     'Peter Parker',
# ]
#
#
# persons = zip(name_hero, name_real)
# print(list(persons))

#
#
# 6.	С помощью функции filter() переместите из списка numbers = [1, 2, 4, 5, 7, 8, 10, 11] нечетные элементы в новый список.
#
# numbers = [1, 2, 4, 5, 7, 8, 10, 11]
# print(numbers)
# new_numbers = filter(lambda num: num % 2 == 0, numbers)
# print(list(new_numbers))
# print(list(numbers))