my_spisok = [False, 'one', 3.33, 4, 'two']
print(my_spisok)
del my_spisok[3]
# my_spisok.pop(-2)
print(my_spisok)
print(len(my_spisok))

print('reverse')
my_spisok.reverse()
print(my_spisok)

my_spisok2 = ['duo', 2]
print(my_spisok2)

my_spisok.extend(my_spisok2)

print(my_spisok)
