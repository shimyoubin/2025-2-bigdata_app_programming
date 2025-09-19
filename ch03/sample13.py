from types import new_class

my_book = 2005, 'pyton', 100, '2class'
your_book = [2010, 'java', 200, '2class']

#new_book = [your_book[1], your_book[2]]
#new_book = your_book[1:3]
#new_book = your_book[:4]
#new_book = your_book[1:]

#new_book = your_book[-1:]
new_book = your_book[len(your_book) -1]

print(new_book)
print(your_book)
print(my_book)
print('-'*30)

