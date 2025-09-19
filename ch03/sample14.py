from types import new_class

my_book = 2005, 'pyton', 100, '2class'
your_book = [2010, 'java', 200, '2class']

new_book = your_book[:]
new_book = your_book #

your_book[0]=2025

print(new_book)
print(your_book)
print(my_book)
print('-'*30)

